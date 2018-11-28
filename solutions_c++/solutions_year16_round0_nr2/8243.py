{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 #include <iostream>\
using namespace std;\
\
int main() \{\
	string str;\
	getline (cin, str);\
\
	int n = atol(str.c_str());\
	for (int i = 0; i < n; i++)\{\
		string str;\
  		getline (cin, str);\
  		int changes = 1;\
  		\
  		char prev = str.at(0);\
  		for (int i = 1; i < str.length(); i++)\{\
  			if (str.at(i) != prev) \{changes++; prev = str.at(i);\}\
  		\}\
  		//cout << str << ": "<< changes << endl;\
  		cout << "Case #"<<i+1<<": "<< changes -1 + (str.at(str.length()-1)=='-'?1:0) << endl;\
	\}\
	return 0;\
\}}