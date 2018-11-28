#include <bits/stdc++.h>

using namespace std;

int k,c,s;

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",t);
		for(int i = 1; i <= k; i++){
			printf(" %d",i);
		}
		printf("\n");
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