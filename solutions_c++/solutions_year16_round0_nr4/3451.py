#include "bits/stdc++.h"
using namespace std;

long long power(long long x, long long p){
	if(p == 0) return (long long)1;
	else if(p == 1) return x;
	long long y = power(x, p/2);
	if(p%2 == 0) return y*y;
	else return y*y*x;
}

int main(void){
	int i, t; cin>>t;
	for(i = 1; i <= t; i++){
		cout<<"Case #"<<i<<": ";
		int k, c, s; cin>>k>>c>>s;
		long long ans = power((long long)k, (long long)c-1);
		long long xyz = 1;
		while(k--){
			cout<<xyz<<" ";
			xyz += ans;
		}
		cout<<endl;
	}
}
