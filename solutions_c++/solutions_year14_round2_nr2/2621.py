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

int main(){
	int test = 0, N = 0;
	LL i = 0, j = 0, count = 0;
	LL A = 0, B = 0, K = 0;
	scanf("%d",&test);
	for(int x_test = 1;x_test<=test; x_test++){
		scanf("%lld %lld %lld\n",&A,&B,&K);
		count = 0;
		for(i = 0; i<A; i++){
			for(j = 0; j<B; j++){
//				cout<<i<<" "<<j<<" "<<endl<<flush;
//				printf("%lld\n",i&j);
				LL temp = i&j;
//				cout<<temp<<endl<<flush;
				if(temp<K && temp>=0){
					count++;
				}
			}
		}
		printf("Case #%d: %lld\n",x_test,count);
	}
	return(0);
}
