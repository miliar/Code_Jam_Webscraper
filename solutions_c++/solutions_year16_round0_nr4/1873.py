#include <cstdio>
#include <cmath>
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int k,c,s;
		scanf("%d %d %d",&k,&c,&s);
		long long at=pow(k,c-1);
		printf("Case #%d:",i+1);
		for(int j=0;j<k;j++){
			printf(" %lld",at*j+1);
		}
		printf("\n");
	}

}