#include<stdio.h>
int main(){
	int T,t,K,C,S,i,j;
	long long ans;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d%d",&K,&C,&S);
		if((K-1)/C+1>S)
			printf("Case #%d: IMPOSSIBLE\n",t);
		else{
			printf("Case #%d:",t);
			for(i=0;i<K;i+=C){
				ans = 0;
				for(j=i;j<i+C;j++){
					ans *= K;
					if(j<K) ans+=j;
				}
				printf(" %I64d",ans+1);
			}
			puts("");
		}
	}
}
