#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
const int mod = 1e9+7;
#ifndef M_PI
#define M_PI acos(-1.0)
#endif

bool used[10];

int main(){
	int t, n;
	cin>>t;
	for(int ct=0; ct<t; ++ct){
		cin>>n;
		cout<<"Case #"<<ct+1<<": ";
		if(n==0){
			cout<<"INSOMNIA";
		}
		else{
			for(int i=0; i<10; ++i){
				used[i]=false;
			}
			int cur=0;
			while(true){
				cur+=n;
				string sp=to_string(cur);
				for(auto c : sp){
					used[c-'0']=true;
				}
				bool sl_time=true;
				for(int i=0; i<10; ++i){
					sl_time=sl_time && used[i];
				}
				if(sl_time){
					break;
				}
			}
			cout<<cur;
		}
		cout<<"\n";
	}
	return 0;
}
