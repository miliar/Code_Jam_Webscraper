SRCDIR  = $(dir $(lastword $(MAKEFILE_LIST))) 
CXXFLAGS=-g -std=c++11 -I$(SRCDIR)
