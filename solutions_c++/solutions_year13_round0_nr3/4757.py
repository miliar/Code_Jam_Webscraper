//============================================================================
// Name        : FairSquare.cpp
// Author      : Loc Ngo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <sstream>
using namespace std;
ifstream fin("C-small-attempt0.in");
ofstream fout("out.txt");
int T;
int A,B;
int F[1000];
int nF = 0;
long int form_even_p(int v) {
	stringstream ss;
	ss << v;
	string s;
	ss>>s;
	string reverse_s = s;
	int len = reverse_s.length();
	for(int i=0;i<len/2;i++)
		swap(reverse_s[i], reverse_s[len-i-1]);
	string ret_s = s + reverse_s;
	ss.clear();
	ss<<ret_s;
	long int ret;
	ss >> ret;
	return ret;
}

long int form_odd_p(int v,int c) {
	stringstream ss;
	ss << v;
	string s;
	ss>>s;
	string reverse_s = s;
	int len = reverse_s.length();
	for(int i=0;i<len/2;i++)
		swap(reverse_s[i], reverse_s[len-i-1]);
	ss.clear();
	ss<<c;
	string s_c;
	ss>>s_c;
	string ret_s = s + s_c + reverse_s;
	ss.clear();
	ss<<ret_s;
	long int ret;
	ss >> ret;
	return ret;
}

bool is_palind(long int v){
	stringstream ss;
	ss << v;
	string s;
	ss>>s;
	int len = s.length();
	for(int i=0;i<len/2;i++)
		if(s[i]!=s[len-i-1])
			return false;
	return true;
}

void generate(int n, bool even){
	if(even){
		for(int i=(int)pow(10,n-1);i<(int)pow(10,n);i++)
		{
			long int d = form_even_p(i);
			long int d_root = sqrt(d);
			if(d_root*d_root == d && is_palind(d_root)) {
				F[nF++] = d;
			}
		}
	}
	else
	{
		for(int i=(int)pow(10,n-1);i<(int)pow(10,n);i++)
		{
			for(int j=0;j<10;j++) {
				long int d = form_odd_p(i,j);
				long int d_root = sqrt(d);
				if(d_root*d_root == d && is_palind(d_root)) {
					F[nF++] = d;
				}
			}
		}
	}
}

void process(int t) {
	fin>>A>>B;
	int n = 0;
	for(int i=0;i<nF;i++){
		if(F[i]>=A && F[i]<=B)
			n++;
	}
	fout<<"Case #"<<t<<": "<<n<<endl;
}

int main() {
	F[nF++] = 1;
	F[nF++] = 4;
	F[nF++] = 9;
	for(int n=1;n<=6;n++)
	{
		generate(n,true);
		generate(n,false);
	}

	fin>>T;
	for(int t=1;t<=T;t++)
		process(t);

	return 0;
}
