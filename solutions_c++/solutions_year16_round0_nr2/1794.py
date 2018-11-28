#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
const int mod = 1e9+7;
#ifndef M_PI
#define M_PI acos(-1.0)
#endif

int main(){
	int t;
	string s;
	cin>>t;
	for(int ct=0; ct<t; ++ct){
		cin>>s;
		s=s+"+";
		int res=0;
		for(int i=0; i<s.size()-1; ++i){
			if(s[i]!=s[i+1]){
				++res;
			}
		}
		cout<<"Case #"<<ct+1<<": "<<res<<"\n";
	}
	return 0;
}
