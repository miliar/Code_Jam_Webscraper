#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<stdlib.h>

using namespace std;

#define MEM(v,i) memset(v,i,sizeof(v))

typedef long long int LL;
typedef unsigned long long int LLU;
int main(){
	int test = 0;
	LLU K = 0, C = 0, S = 0;
	scanf("%d",&test);
	for(int x_test = 1;x_test<=test; x_test++){
		scanf("%llu %llu %llu\n",&K,&C,&S);
		if(C==1){
			if(K<=S){
				printf("Case #%d:",x_test);
				for(LLU i = 1; i<=K;i++){
					printf(" %llu",i);
				}
				printf("\n");
				continue;
			}
			else{
				printf("Case #%d: IMPOSSIBLE\n",x_test);
				continue;
			}
		}
		else if(K==1 && S<1){
			printf("Case #%d: IMPOSSIBLE\n",x_test);
			continue;
		}
		else if(K==1){
			printf("Case #%d: 1\n",x_test);
			continue;
		}
		else if(S<K-1){
			printf("Case #%d: IMPOSSIBLE\n",x_test);
			continue;
		}
		else{
			printf("Case #%d:",x_test);
			for(LLU i = 2, t = 0; i<= K; i++, t += K){
				printf(" %llu",t+i);
			}
			printf("\n");
		}
	}
	return(0);
}
