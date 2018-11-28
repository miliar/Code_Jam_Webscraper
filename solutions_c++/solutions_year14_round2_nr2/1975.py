#include<stdio.h>      
#include<stdlib.h>      
#include<math.h>  
#include <iostream>
#include <string>
using namespace std;
	

int main() { 
	
	int T,i,j,k,A, B, K;
	scanf("%d",&T);
	
	for (i=1; i<=T; i++)
	{

		scanf("%d", &A);
		scanf("%d", &B);
		scanf("%d", &K);

		long result = 0;
		for (j=0;j<A;j++)
			for (k=0;k<B;k++)
				if ((j&k)<K) {
					result++;
				}
			
		printf("Case #%d: %ld\n",i,result);
		
	}
	
	return 0;
}

