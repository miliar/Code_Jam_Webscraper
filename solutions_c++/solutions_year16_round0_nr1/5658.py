#include<bits/stdc++.h>
using namespace std;
#define Int long long
int main(){
	Int t,n,ans,i,j,k,hash[10],sum,x;
	scanf("%lld",&t);
	for(x=1;x<=t;x++){
		scanf("%lld",&n);
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",x);
		}else{
			memset(hash,0,sizeof(hash));sum=0;
			for(i=1;;i++){
				j = i*n;
				while(j){
					k = j%10;
					if(hash[k]==0){
						hash[k]++;
						sum+=k;
					}
					j/=10;
				}
				if(sum==45 && hash[0]){
					ans = i*n;
					break;
				}
			}
			printf("Case #%lld: %lld\n",x,ans);
		}
	}
	return 0;
}