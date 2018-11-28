#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>

using namespace std;

int C,K,S;


int check(){

	int i;
	long long pos =0;

	for(i = 0; i < K && i < C; ++i){
		pos*=K;
		pos += i;
	}

	if(K-i+1 > S) return 0;

	printf(" %lld",pos+1);
	for(; i < K; ++i){
		printf(" %d",i+1);
		assert(i != pos);
	}

	return 1;
}


int main(){

	int t,x;

	scanf("%d",&t);

	for(x = 1; x <= t; ++x){
		scanf("%d%d%d",&K,&C,&S);
		printf("Case #%d:",x);
		if(!check()){
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}

	return 0;
}
