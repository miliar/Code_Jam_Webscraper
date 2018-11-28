{\rtf1\ansi\ansicpg936\cocoartf1265\cocoasubrtf190
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red200\green20\blue201;\red180\green36\blue25;\red159\green160\blue28;
\red47\green180\blue29;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural

\f0\fs22 \cf2 \CocoaLigature0 #include\cf3 <iostream>\cf0 \
\cf2 #include\cf3 <iomanip>\cf0 \
\cf4 using\cf0  \cf5 namespace\cf0  std;\
\cf5 int\cf0  main()\
\{\
        \cf5 int\cf0  T;\
        cin >> T;\
        \cf4 for\cf0  (\cf5 int\cf0  i = \cf3 1\cf0 ; i <= T; i++)\
        \{\
                \cf5 int\cf0  N, sum = \cf3 0\cf0 , ans = \cf3 0\cf0 ;\
                cin >> N;\
                string S;\
                cin >> S;\
                \cf4 for\cf0  (\cf5 int\cf0  j = \cf3 0\cf0 ; j <= N; j++)\
                \{\
                        \cf4 if\cf0  (S[j] != \cf3 0\cf0  && sum < j)\
                        \{\
                                ans += (j - sum);\
                                sum = j + S[j] - \cf3 '0'\cf0 ;\
                        \}\
                        \cf4 else\cf0 \
                                sum += S[j] - \cf3 '0'\cf0 ;\
                \}\
                cout<<\cf3 "Case #"\cf0  << i << \cf3 ": "\cf0  << ans <<endl;\
        \}\
        \cf4 return\cf0  \cf3 0\cf0 ;\
\}}