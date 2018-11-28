/*
 * C.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: yassery
 */


#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

set<long long> s,sss;
long long MX = 1000LL;

long long toNum(string s){
	long long x=0;
	for(int i=0;i<s.size();i++){
		x*=10;
		x+= (s[i]-'0');
	}
	return x;
}

void gen(string st){
	long long x = toNum(st);
	if(x <= MX){
		if(x%10){
			if(!s.insert(x).second)
				return;
		}
		
		for(char i=(x==0?'1':'0');i<='9';i++){
			string ss = "";
			ss+= i;
			gen(ss + st + ss);
		}
	}
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("test.in","rt",stdin);
	freopen("test.txt","wt",stdout);
#endif

	string s="";
	for(char i='0';i<='9';i++){
		string ss = s+i;
		gen(ss);
		gen(ss+ss);
	}

	int T;
	cin>>T;
	long long a, b;
	for(int tt=0;tt<T;tt++){
		cin>>a>>b;
		cout<<"Case #"<<tt+1<<": ";
		int c =0;
		set<long long>::iterator it ;
		for(it = ::s.begin();it!= ::s.end();it++){
			long long x = *it;
			x *= x;
			if(::s.find(x)!= ::s.end() && x>=a && x<= b)
				c++;
		}
		cout<<c<<endl;
	}
	return 0;
}
