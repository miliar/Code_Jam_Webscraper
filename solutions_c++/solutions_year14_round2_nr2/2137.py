#include<string.h>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
int main(){
	freopen("D:\\Users\\Song\\Downloads\\Code\\input.txt","r",stdin);
	freopen("D:\\Users\\Song\\Downloads\\Code\\output.txt","w",stdout);
	int T,count=0;
	long A,B,K;
	long i,j,k;
	long pairs;

	scanf("%d",&T);
	for(count=1;count<=T;count++){
		pairs=0;
		scanf("%ld",&A);
		scanf("%ld",&B);
		scanf("%ld",&K);
		for(i=0;i<A;i++)
			for(j=0;j<B;j++){
				if((i&j)<K)
					pairs++;
			}
		printf("Case #%d: %d\n",count,pairs);
	}
	return 0;
}

