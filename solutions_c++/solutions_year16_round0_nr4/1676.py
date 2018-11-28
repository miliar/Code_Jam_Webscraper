#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
int k,c,s;

int main(){
	int T,ca=1;
	scanf("%d",&T);
	while(T--){
		printf("Case #%d: ",ca++);
		scanf("%d%d%d",&k,&c,&s);
		if(k==1){
			printf("1\n");
			continue;
		}
		if(c==1){
			if(s<k) printf("IMPOSSIBLE\n");
			else {
				for (int i=1;i<=k;i++){
					printf("%d ",i);
				}
				printf("\n");
			}
			continue;
		}
		long long kc=1;
		for (int i=0;i<c-1;i++) kc*=k;
		for (int i=0;i<k;i=i+2){
			long long qian=kc*i;
			qian+=i;
			if(i+1<k) qian++;
			printf("%lld ",qian+1);
		}
		printf("\n");
	}
	return 0;
}
