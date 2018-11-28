#include<bits/stdc++.h>
using namespace std;

int main(){
	long long int t,k,c,s,cas,i,j,ans,iter;
	scanf("%lld",&t);

	for(cas=1;cas<=t;cas++){
		scanf("%lld%lld%lld",&k,&c,&s);
		if(ceil((double)k/c)>s){
			printf("Case #%lld: IMPOSSIBLE\n",cas);
			continue;
		}

		printf("Case #%lld: ",cas);
		iter=ceil((double)k/c);
		for(i=1;i<iter;i++){
			ans=(i-1)*c+1;
			for(j=2;j<=c;j++){
				ans=(ans-1)*k+(i-1)*c+j;
			}
			printf("%lld ",ans);
		}
		
		ans=k-c+1;
		if(ans>0){
			for(j=2;j<=c;j++){
				ans=(ans-1)*k+k-c+j;
			}
			printf("%lld ",ans);
		}
		else{
			ans=1;
			for(j=2;j<=k;j++){
				ans=(ans-1)*k+j;
			}
			printf("%lld ",ans);
		}
		printf("\n");
	}
	return 0;
}