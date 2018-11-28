{\rtf1\ansi\ansicpg1252\cocoartf1344\cocoasubrtf720
{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red63\green127\blue95;\red127\green0\blue85;\red42\green0\blue255;
\red100\green40\blue128;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720

\f0\fs22 \cf2 //============================================================================\cf0 \
\cf2 // Name        : codejam.cpp\cf0 \
\cf2 // Author      : \cf0 \
\cf2 // Version     :\cf0 \
\cf2 // Copyright   : Your copyright notice\cf0 \
\cf2 // Description : Hello World in C++, \ul Ansi\ulnone -style\cf0 \
\cf2 //============================================================================\cf0 \
\
\pard\pardeftab720
\cf3 #include\cf0  \cf4 <iostream>\cf0 \
\cf3 #include\cf4 <string.h>\cf0 \
\cf3 using\cf0  \cf3 namespace\cf0  std;\
\
\
\cf3 int\cf0  main() \{\
\
	\cf5 freopen\cf0  (\cf4 "A-small-attempt0.in"\cf0 ,\cf4 "r"\cf0 ,stdin);\
		\cf5 freopen\cf0 (\cf4 "output5.\ul txt\ulnone "\cf0 ,\cf4 "w"\cf0 ,stdout);\
	\cf3 int\cf0  counter,total;\
	\cf3 int\cf0  t,sMax,i;\
	\cf3 char\cf0  levels[1001];\
	\cf3 int\cf0  answer=0;\
	\cf3 int\cf0  arr[1001];\
	cin>>t;\
	\cf3 for\cf0 (counter=1;counter<=t;counter++)\
	\{\
		total=0;\
		answer=0;\
		cin>>sMax;\
		cin>>levels;\
\
		\cf3 for\cf0 (i=0;i<\cf5 strlen\cf0 (levels);i++)\
		\{\
			arr[i]=levels[i]-\cf4 '0'\cf0 ;\
		\}\
\
		\cf3 if\cf0 (sMax==0)\
		\{\
			cout<<\cf4 "Case #"\cf0 <<counter<<\cf4 ": "\cf0 <<answer<<endl;\
			\cf3 continue\cf0 ;\
		\}\
\
		\cf3 for\cf0 (i=0;i<=sMax;i++)\
		\{\
			\cf3 if\cf0 (i==0)\
			\{\
				total=total+arr[i];\
			\}\
			\cf3 else\cf0 \
			\{\
			\cf3 if\cf0 (arr[i]!=0)\
			\{\
				\cf3 if\cf0 (i<=total)\
				\{\
					total=total+arr[i];\
				\}\
				\cf3 else\cf0 \
				\{\
					answer=answer+i-total;\
					total=i+arr[i];\
				\}\
\
			\}\
			\}\
		\}\
\
\
\
\
		cout<<\cf4 "Case #"\cf0 <<counter<<\cf4 ": "\cf0 <<answer<<endl;\
\
\
\
	\}\
	\cf2 //\ul cout\ulnone  << "!!!Hello World!!!" << \ul endl\ulnone ; // prints !!!Hello World!!!\cf0 \
	\cf3 return\cf0  0;\
\}\
}