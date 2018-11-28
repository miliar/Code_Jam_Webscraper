#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main(){

	int t,caseno,i,j,n,count,A,B,K;
	scanf("%d",&t);
	caseno=0;

	while(caseno++ < t){
		int count=0;
		scanf("%d %d %d",&A,&B,&K);
		count=A+B-1;
		for(i=1;i<A;i++){
			for(j=1;j<B;j++){
				if((i & j) < K)
					count++;
			}
		}

		printf("Case #%d: %d\n",caseno,count);
	}



	}