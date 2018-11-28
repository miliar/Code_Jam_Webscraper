#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
long long pow(long long a,long long b){
	long long ret = 1;
	while(b--){
		ret *= a;
	}
	return ret;
}
int main(){
	int tcase;
	cin >> tcase;
	for(int casei=1;casei<=tcase;casei++){
		long long k,c,s;
		cin >> k >> c >> s;
		long long kc = pow(k,c-1);
		printf("Case #%d: ",casei);
		long long ans = 1;
		for(int i=1;i<=s;i++){
			printf("%lld%c",ans,(i==s?'\n':' '));
			ans += kc;
		}
	}
	return 0;
}
