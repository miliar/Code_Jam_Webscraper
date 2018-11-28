#include<stdio.h>
#include <string.h>
#include <math.h>

int K,C,S;
int array[10000000];

int main()
{
	freopen("D-small-attempt3.in","r",stdin);
	freopen("fractiles.out","w",stdout);

	int T,K,C,S;
	scanf("%d",&T);
	for (int i=1; i<=T;i++) {
		scanf("%d",&K);
		scanf("%d",&C);
		scanf("%d",&S);

		memset(array,0,sizeof(array));

		long int length = pow((double)K,(double)C);
		long long int originalSequences =1000;
		int ii;
		long int pos = 0;
		//for (ii=1;ii<length;ii++) {
		//	pos = (ii-1) * C + ii;
		//	array[pos] = (int)originalSequences/2; 
		//}
		printf("Case #%d:",i);
		if ((C == 1 && S < K) || (C > 1 && S < K-C+1)) {
			printf(" IMPOSSIBLE");
		}else if(K==1){
			printf(" 1");
		}else {
			for (int kk = 1;kk<=K;kk++){
				printf(" %d",kk);
			}
		}
		printf("\n");
	}
}