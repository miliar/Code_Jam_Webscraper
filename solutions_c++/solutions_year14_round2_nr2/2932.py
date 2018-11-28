#include<stdio.h>
#include<iostream>
#include<algorithm>

#define DEBUG 1



int main()
{
	int i,j,N, count, cas=0;
	int A,B,K;
	scanf("%d", &N);
	while(N--){
		cas++;
		scanf("%d %d %d", &A, &B, &K);
		count = 0;
		for(i=0;i<A;i++){
			for(j=0;j<B;j++){
				if( (i&j) < K) count++;
			}
		}
		printf("Case #%d: %d\n", cas, count);
	}
	
}
