#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<time.h>



float compare (const void * a, const void * b)
{
  return ( *(float*)a - *(float*)b );
}

int main(){
	int n=1, input, num, i, j;
	float temp;
	scanf("%d", &input);
	while(n<=input){
		int pts_d=0;
		scanf("%d", &num);
		float N[num], K[num];
		for(i=0; i<num; i++)
			scanf("%f", &N[i]);
		for(i=0; i<num; i++)
			scanf("%f", &K[i]);

		std::sort(N, N+num);
		std::reverse(N, N+num);
		std::sort(K, K+num);

		i=num-1;
		while(N[i]<K[0]){
			i--;
		}
		std::reverse(K, K+i+1);
		j=i;
		while(N[i]>K[j] && i>-1){
			pts_d++;
			i--;j--;
			while(N[i]<K[j] && i)
				i--;
		}

		int pts_o=0;
		std::sort(N, N+num);
		std::sort(K, K+num);
		for(i=num-1, j=0; i>=0; i--){
			if(N[i]>K[num-1-j]){
				pts_o++;
			}
			else
				j++;
		}
		printf("Case #%d%s%d%c%d", n, ": ", pts_d, ' ', pts_o);

		n++;
		printf("\n"); 
	}
	return 0;
}