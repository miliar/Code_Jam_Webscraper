{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green116\blue0;\red100\green56\blue32;\red196\green26\blue22;
\red170\green13\blue145;\red92\green38\blue153;\red28\green0\blue207;\red46\green13\blue110;\red63\green110\blue116;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab529
\pard\tx529\pardeftab529\pardirnatural\partightenfactor0

\f0\fs22 \cf2 \CocoaLigature0 //\cf0 \
\cf2 //  main.cpp\cf0 \
\cf2 //  codejam : swinging wild\cf0 \
\cf2 //\cf0 \
\cf2 //  Created by Marc Saunders on 2015-12-19.\cf0 \
\cf2 //  Copyright \'a9 2015 Marc Saunders. All rights reserved.\cf0 \
\cf2 //\cf0 \
\
\cf3 #include \cf4 <iostream>\cf3 \
#include \cf4 <iostream>\cf3 \
#include \cf4 <sstream>\cf3 \
#include \cf4 <string>\cf3 \
#include \cf4 <fstream>\cf3 \
#include \cf4 <stdint.h>\cf3 \
#include \cf4 <unistd.h>\cf3 \
#include \cf4 <math.h>\cf3 \
\cf0 \
\cf3 #include \cf4 <stdio.h>\cf3       \cf2 /* printf */\cf3 \
#include \cf4 <assert.h>\cf3 \
\cf0 \
\
\cf3 #define ha \cf2 //\cf0 \
\
\cf2 // 64bitoperations need 32 bit max numbers\cf0 \
\
\
\cf5 using\cf0  \cf5 namespace\cf0  \cf6 std\cf0 ;\
\
\cf6 string\cf0  testcases ;\
\
\cf5 int\cf0  levels ;\
\cf6 string\cf0  results;\
\cf5 int\cf0  times[\cf7 10000\cf0 ] ;\
\cf5 long\cf0  \cf5 double\cf0  probs [\cf7 10000\cf0 ] ;\
\cf5 long\cf0  \cf5 double\cf0  scales [ \cf7 10000\cf0 ] ;\
\cf5 int\cf0  list ;\
\cf5 int\cf0  indexe[\cf7 2500\cf0 ];\
\
\
\cf5 long\cf0  \cf5 double\cf0  average ;\
\cf5 long\cf0  \cf5 double\cf0  remaining ;\
\
\
\cf5 int\cf0  main(\cf5 int\cf0  argc, \cf5 const\cf0  \cf5 char\cf0  * argv[]) \{\
    \cf2 // insert code here...\cf0 \
    \cf6 std\cf0 ::\cf6 ifstream\cf0  infile(\cf4 "/Users/marcsMac/Desktop/codejam/in.txt"\cf0 );\
    \cf8 freopen\cf0 (\cf4 "/Users/marcsMac/Desktop/codejam/out.txt"\cf0 ,\cf4 "w"\cf0 ,\cf3 stdout\cf0 );\
    \cf6 std\cf0 ::\cf8 getline\cf0 (infile, \cf9 testcases\cf0 ) ; \cf2 // read in string number of test cases\cf0 \
    \cf6 std\cf0 ::\cf6 istringstream\cf0  iss(\cf9 testcases\cf0 );\
    \cf5 int\cf0  N ;\
    iss >> N ;\
    \cf8 fprintf\cf0 (\cf3 stderr\cf0 ,\cf4 "\\n"\cf0 );\
    \cf8 fprintf\cf0 (\cf3 stderr\cf0 ,\cf4 "there are %d tests in this guy\\n"\cf0 ,N);\
    \
    \
    \cf5 for\cf0 (\cf5 int\cf0  n=\cf7 0\cf0 ;n<N ;n++)\
    \{\
        \
        \cf6 std\cf0 ::\cf8 getline\cf0 (infile, \cf9 testcases\cf0 ) ; \cf2 // read in the pattern\cf0 \
        \cf6 std\cf0 ::\cf6 istringstream\cf0  issy(\cf9 testcases\cf0 );\
        \
        issy >> \cf9 levels\cf0  ;\
        \
        \cf5 for\cf0  (\cf5 int\cf0  x = \cf7 0\cf0  ; x < \cf7 2500\cf0   ; x++ )\
\
        \{\
            \cf9 indexe\cf0  [x] = \cf7 0\cf0  ;\
        \}\
    \
        \cf5 int\cf0  q = \cf7 2\cf0 *\cf9 levels\cf0  - \cf7 1\cf0  ;\
        \
        \cf5 for\cf0  (\cf5 int\cf0  x = \cf7 0\cf0  ;  x < q ; x ++)\
        \{\
            \
            \cf6 std\cf0 ::\cf8 getline\cf0 (infile, \cf9 testcases\cf0 ) ; \cf2 // read in the pattern\cf0 \
            \cf6 std\cf0 ::\cf6 istringstream\cf0  issq(\cf9 testcases\cf0 );\
            \
            \cf5 for\cf0  (\cf5 int\cf0  y = \cf7 0\cf0  ; y < \cf9 levels\cf0  ; y ++ )\
            \{\
                issq >> \cf9 list\cf0  ;\
                \cf9 indexe\cf0  [\cf9 list\cf0 ] = \cf9 indexe\cf0  [ \cf9 list\cf0 ] + \cf7 1\cf0  ;\
                \cf5 if\cf0  (\cf9 indexe\cf0 [\cf9 list\cf0 ] == \cf7 2\cf0  )\
                    \cf9 indexe\cf0 [\cf9 list\cf0 ] = \cf7 0\cf0  ;\
            \}\
            \
            \
            \
        \}\
        \
        \cf8 printf\cf0 (\cf4 "Case #%d:"\cf0 ,n+\cf7 1\cf0 );\
        \cf5 for\cf0  (\cf5 int\cf0  x = \cf7 0\cf0  ; x < \cf7 2500\cf0   ; x++ )\
            \
        \{\
            \cf5 if\cf0  ( \cf9 indexe\cf0 [x] == \cf7 1\cf0  )\
            \{\
                \cf8 printf\cf0 (\cf4 " %d"\cf0 ,x);\
            \}\
        \}\
        \cf8 printf\cf0 (\cf4 "\\n"\cf0 );\
        \
    \}\
    \cf5 return\cf0  \cf7 0\cf0  ;\
\}}