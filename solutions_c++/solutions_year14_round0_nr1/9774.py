{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf190
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 //\
#include <iostream>\
#include <vector>\
#include <stdio.h>\
#include <algorithm>\
using namespace std;\
\
int main()\
\{\
	\
	int t;\
	scanf("%d\\n",&t);\
	vector<int> frec;\
	frec.resize(16);\
	\
	for(int k=0;k<t;k++)\
	\{\
		fill(frec.begin(),frec.end(),0);\
		int col1,col2;\
		scanf("%d\\n",&col1);\
		char aux[100];\
		for(int i=0;i<4;i++)\
		\{\
			if(i!=col1-1)\
                gets(aux);\
			else\
			\{\
				for(int j=0;j<4;j++)\
				\{\
					int num;\
					scanf("%d ",&num);\
					frec[num-1]++;\
				\}\
				scanf("\\n");\
			\}\
            \
            \
		\}\
        scanf("%d\\n",&col2);\
		int cont=0;\
		int res=-1;\
		for(int i=0;i<4;i++)\
		\{\
			if(i!=col2-1)\
                gets(aux);\
			else\
			\{\
				for(int j=0;j<4;j++)\
				\{\
					int num;\
					scanf("%d ",&num);\
					frec[num-1]++;\
					if(frec[num-1]>1)\
					\{\
						cont++;\
						res=num;\
					\}\
				\}\
			\}\
		\}\
	\
	if(cont==0)\
	 printf("Case #%d: Volunteer cheated!\\n",k+1);\
	 else if (cont==1)\
	 printf("Case #%d: %d\\n",k+1,res);\
	 else \
      printf("Case #%d: Bad magician!\\n",k+1);\
		\
	\
		\
		\
	\}\
    \
	return 0;\
\}}