#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

if __name__ == "__main__":
    print '-' * 70
    print "DEPRECATED: you are starting the OpenERP server with its old path,"
    print "please use the new executable (available in the parent directory)."
    print '-' * 70

    # Change to the parent directory ...
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    # ... and execute the new executable.
    os.execv('openerp-server.py', sys.argv)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
