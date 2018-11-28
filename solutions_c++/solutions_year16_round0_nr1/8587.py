#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#define INF (1<<30)
using namespace std;

bool sleep(bool digit[]){
	for(int i=0; i<10; i++)
		if(!digit[i])return false;
	return true;
}

int main(){
	int t=0, C=0;
	scanf("%d", &t);
	while(t--){
		C++;
		long long N=0, k=0, ans=0;
		scanf("%lld", &N);
		if(N<=0){
			printf("Case #%d: INSOMNIA\n", C);
			continue;
		}
		bool digit[10];
		memset(digit, false, sizeof(digit));
		while(!sleep(digit)){
			long long G=ans=(++k)*N;
			while(G>0){
				digit[G%10]=true;
				G/=10;
			}
		}
		printf("Case #%d: %lld\n", C, ans);
	}
	return 0;
}
