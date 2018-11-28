#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
const int mod = 1e9+7;
#ifndef M_PI
#define M_PI acos(-1.0)
#endif

int main(){
	ll t, k, c, s;
	cin>>t;
	for(int ct=0; ct<t; ++ct){
		cin>>k>>c>>s;
		cout<<"Case #"<<ct+1<<": ";
		if(s*c<k){
			cout<<"IMPOSSIBLE";
		}
		else{
			for(int i=0; i<s;){
				ll cpos=0;
				for(int j=0; j<c; ++j){
					cpos*=k;
					if(i<k){
						cpos+=i;
						++i;
					}
				}
				cout<<cpos+1<<' ';
			}
		}
		cout<<"\n";
	}
	return 0;
}
