#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;++i)


int main(int argc, char** argv) {
	int t;
	scanf("%d\n",&t);
	for(int tt=1;tt<=t;++tt) {
		printf("Case #%d:\n",tt);
		int n,j;
		scanf("%d%d",&n,&j);
		int x = (n-2)/2;
		
		FOR(i,j) {
			long long ans = (1<<(n-1))|1;
			for(int k=0;k<x;++k) {
				if((1<<k)&i) {
					ans|=3<<(2*k+1);
				}
			}
			for(int k=n-1;k>=0;--k) {
				printf("%d",((1<<k)&ans)?1:0);
			}
			for(int k=3;k<12;++k) printf(" %d",k);
			printf("\n");
		}
	}
		
	
	
}