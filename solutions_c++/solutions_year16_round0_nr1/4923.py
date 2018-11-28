#include <bits/stdc++.h>

using namespace std;

long long Capita, D;
int n, L = (1 << 10) - 1;

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d",&n);
		Capita = 0;
		if(n){
			int mask = 0;
			while(mask != L){
				Capita += n;
				D = Capita;
				while(D){
					mask |= (1 << (D % 10));
					D /= 10;
				}
			}
			printf("Case #%d: %lld\n",t,Capita);
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