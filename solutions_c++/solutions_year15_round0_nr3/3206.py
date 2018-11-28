#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;
// #define i 2
// #define j 3
// #define k 4
const int i = 2;
const int j = 3;
const int k = 4;
int quad(int a, int b);
bool findi(const char* str);

int main() {
	int T;
	cin>>T;
	for(int t_i=0; t_i<T; ++t_i) {
		int L,X;
		cin>>L;
		cin>>X;
		string str_temp,str;
		cin>>str_temp;
		for(int str_i=0; str_i<X; ++str_i) {
			str.append(str_temp);
		}
		const char* str_c = str.c_str();
		bool res = findi(str_c);
		if(res)
			printf("Case #%d: YES\n",t_i+1);
		else
			printf("Case #%d: NO\n",t_i+1);
	}
	return 0;
}

int getval(char a) {
	switch(a) {
		case 'i':
			return i;
		case 'j':
			return j;
		case 'k':
			return k;
	}
	return 1;
}

bool findk(const char* str) {
//	printf("strk[%s]\n",str);
	if(*str=='\0')
		return false;
	int output = 1;
	while(*str!='\0') {
		bool minus = false;
		if(output<0) {
			minus = true;
			output *=-1;
		}
		// printf("output[%d]\n",output);
		output = quad(output,getval(*str));
		if(minus)
			output *=-1;
		str++;	
	}
	if(output == k && *str=='\0') {
		return true;
	}
	return false;
}

bool findj(const char* str) {
//	printf("strj[%s]\n",str);
	if(*str=='\0')
		return false;
	int output = 1;
	while(*str!='\0') {
		bool minus = false;
		if(output<0) {
			minus = true;
			output *=-1;
		}
		// printf("output[%d]\n",output);
		output = quad(output,getval(*str));
		if(minus)
			output *=-1;
		str++;
		if(output == j) {
			if(findk(str))
				return true;
			else
				return false;
		}
	}
		return false;
}


bool findi(const char* str) {
//	printf("stri[%s]\n",str);
	if(*str=='\0')
		return false;
	int output = 1;
	// printf("output[%d]\n",output);
	while(*str!='\0') {
		bool minus = false;
		if(output<0) {
			minus = true;
			output *=-1;
		}
		// printf("output[%d]\n",output);
		output = quad(output,getval(*str));
		if(minus)
			output *=-1;
		str++;
		if(output == i) {
			if(findj(str))
				return true;
			else
				return false;
		}
	}
	return false;
}

int quad(int a, int b) {
	switch(a) {
		case 1:
		switch(b) {
			case 1:
				return 1;
			case i:
				return i;
			case j:
				return j;
			case k:
				return k;
		}
		case i:
		switch(b) {
			case 1:
				return i;
			case i:
				return -1;
			case j:
				return k;
			case k:
				return -j;
		}
		case j:
		switch(b) {
			case 1:
				return j;
			case i:
				return -k;
			case j:
				return -1;
			case k:
				return i;
		}
		case k:
		switch(b) {
			case 1:
				return k;
			case i:
				return j;
			case j:
				return -i;
			case k:
				return -1;
		}
	}
	return 1;
}
