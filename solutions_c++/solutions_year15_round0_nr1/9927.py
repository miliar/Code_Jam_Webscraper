{\rtf1\ansi\ansicpg1252\cocoartf1345\cocoasubrtf380
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 #include <iostream>\
#include <stdio.h>\
\
using namespace std;\
\
int check(char *a, int s)\
\{\
	int count =a[0]-48;\
	int ans = 0;\
	int temp;\
\
	for (int i=1;i<=s;i++)\
	\{\
		temp = a[i]-48;\
		if (i>count+ans)\
			ans++;\
\
		count+=temp;\
	\}\
	\
	return ans;\
\}\
\
int main() \{\
	// your code goes here\
	int t, s;\
	char a[1001];\
	scanf("%d", &t);\
	int c =1;\
	while(t--)\
	\{\
	scanf("%d %s", &s, &a);\
	getchar();\
	int ans = check(a,s);\
	printf("Case #%d: %d\\n", c, ans);\
	c++;\
	\}\
	\
	\
	\
\
	return 0;\
\}}