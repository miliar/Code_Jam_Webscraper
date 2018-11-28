#include <bits/stdc++.h>

using namespace std;

long long N, D;
int n, L = (1 << 10) - 1;

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d",&n);
		N = 0;
		if(n){
			int mask = 0;
			while(mask != L){
				N += n;
				D = N;
				while(D){
					mask |= (1 << (D % 10));
					D /= 10;
				}
			}
			printf("Case #%d: %lld\n",t,N);
		}
		else printf("Case #%d: INSOMNIA\n",t);
	}
}

void fread(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int main(){
	fread();
	init();
	return 0;
}