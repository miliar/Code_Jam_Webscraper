{\rtf1\ansi\ansicpg1252\cocoartf1265
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red100\green56\blue32;\red196\green26\blue22;\red170\green13\blue145;
\red92\green38\blue153;\red28\green0\blue207;\red46\green13\blue110;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab577
\pard\tx577\pardeftab577\pardirnatural

\f0\fs24 \cf2 \CocoaLigature0 #include \cf3 <vector>\cf2 \
#include \cf3 <list>\cf2 \
#include \cf3 <map>\cf2 \
#include \cf3 <set>\cf2 \
#include \cf3 <deque>\cf2 \
#include \cf3 <stack>\cf2 \
#include \cf3 <bitset>\cf2 \
#include \cf3 <algorithm>\cf2 \
#include \cf3 <functional>\cf2 \
#include \cf3 <numeric>\cf2 \
#include \cf3 <utility>\cf2 \
#include \cf3 <sstream>\cf2 \
#include \cf3 <iostream>\cf2 \
#include \cf3 <iomanip>\cf2 \
#include \cf3 <cstdio>\cf2 \
#include \cf3 <cmath>\cf2 \
#include \cf3 <cstdlib>\cf2 \
#include \cf3 <ctime>\cf2 \
#include \cf3 <fstream>\cf2 \
\cf0 \
\cf4 using\cf0  \cf4 namespace\cf0  \cf5 std\cf0 ;\
\
\cf4 int\cf0  main() \{\
    \cf5 ifstream\cf0  fin(\cf3 "/Users/usamaelnily/Desktop/in.txt"\cf0 );\
    \cf5 ofstream\cf0  fout(\cf3 "/Users/usamaelnily/Desktop/out.txt"\cf0 );\
    \cf4 int\cf0  cs, t;\
    fin >> cs;\
    t = cs;\
    \cf4 while\cf0 (cs--) \{\
        \cf4 int\cf0  x, y, a[\cf6 4\cf0 ][\cf6 4\cf0 ], b[\cf6 4\cf0 ][\cf6 4\cf0 ], c = \cf6 0\cf0 ;\
        fin >> x;\
        \cf4 for\cf0 (\cf4 int\cf0  i = \cf6 0\cf0 ; i < \cf6 4\cf0 ; i++) \{\
            \cf4 for\cf0 (\cf4 int\cf0  j = \cf6 0\cf0 ; j < \cf6 4\cf0 ; j++) \{\
                fin >> a[i][j];\
            \}\
        \}\
        fin >> y;\
        \cf4 for\cf0 (\cf4 int\cf0  i = \cf6 0\cf0 ; i < \cf6 4\cf0 ; i++) \{\
            \cf4 for\cf0 (\cf4 int\cf0  j = \cf6 0\cf0 ; j < \cf6 4\cf0 ; j++) \{\
                fin >> b[i][j];\
            \}\
        \}\
        \
        \cf4 for\cf0 (\cf4 int\cf0  i = \cf6 0\cf0 ; i < \cf6 4\cf0 ; i++) \{\
            \cf4 for\cf0 (\cf4 int\cf0  j = \cf6 0\cf0 ; j < \cf6 4\cf0 ; j++) \{\
                \cf4 if\cf0 (a[x-\cf6 1\cf0 ][i] == b[y-\cf6 1\cf0 ][j])\
                    c++;\
            \}\
        \}\
        fout << \cf3 "Case #"\cf0  << t - cs << \cf3 ": "\cf0 ;\
        \cf4 if\cf0 (c == \cf6 0\cf0 )\
            fout << \cf3 "Volunteer cheated!"\cf0  << \cf7 endl\cf0 ;\
        \cf4 if\cf0 (c == \cf6 1\cf0 ) \{\
            \cf4 for\cf0 (\cf4 int\cf0  i = \cf6 0\cf0 ; i < \cf6 4\cf0 ; i++) \{\
                \cf4 for\cf0 (\cf4 int\cf0  j = \cf6 0\cf0 ; j < \cf6 4\cf0 ; j++) \{\
                    \cf4 if\cf0 (a[x-\cf6 1\cf0 ][i] == b[y-\cf6 1\cf0 ][j])\
                        fout << a[x-\cf6 1\cf0 ][i] << \cf7 endl\cf0 ;\
                \}\
            \}\
        \}\
        \cf4 if\cf0 (c == \cf6 2\cf0  || c == \cf6 3\cf0  || c == \cf6 4\cf0 )\
            fout << \cf3 "Bad magician!"\cf0  << \cf7 endl\cf0 ;\
    \}\
    \cf4 return\cf0  \cf6 0\cf0 ;\
\}}