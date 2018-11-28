{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 #include <iostream>\
using namespace std;\
\
int main() \{\
	int n;\
	cin >> n;\
\
	for (int i = 0; i < n; i++)\{\
		int N;\
		cin >> N;\
		//cout << "haha"<<N << endl;\
		if (N==0)\{ cout << "Case #" << i+1 <<": INSOMNIA"<<endl;continue;\}\
		\
		bool cache[10] = \{false\};\
		int count = 0;\
		int ii = 2;\
		int nn = N;\
		while (1)\{\
			while (nn)\{\
				if (cache[nn%10]==false) \{cache[nn%10] = true;count++;\}\
				nn = nn/10;\
			\}\
			if (count == 10) break;\
			nn = N * ii;\
			ii++;\
		\}\
		\
		cout << "Case #" << i+1 <<": "<<N*(ii-1) << endl;\
	\}\
	return 0;\
\}}