#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

#define LL long long 
using namespace std;
const int maxn = 1e6+5;

LL gao(int x){
	static bool f[10];
	static int cnt;
	memset(f,false,sizeof(f));
	cnt = 0;

	LL y = x;
	for(int i=1;i<=maxn;i++){
		LL tmp = y;
		while ( tmp>0 ){
			int d = tmp % 10; 
			tmp /= 10;
			if ( !f[d] ) {
				cnt++; f[d] = true;
			}
		}

		if ( cnt==10 ) return y;
		y += x;
	}
	return maxn;
}

int main(){

	int t; scanf("%d", &t);
	for(int it=1;it<=t;it++){
		int n; scanf("%d", &n);
		if ( n==0 ) {
			printf("Case #%d: INSOMNIA\n", it);
			continue;
		}

		printf("Case #%d: %lld\n", it, gao(n) );
	}

	return 0;
}