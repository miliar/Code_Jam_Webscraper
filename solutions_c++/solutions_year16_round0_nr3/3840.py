/*
 * Author:Õı”Ì«Ô(jywyq) 
 * Date:20160409
 */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#define LL long long
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("dataout.txt","w",stdout);
	int t,cas=0;
	LL n,m;
	cin>>t;
	while(t--){
		printf("Case #%d: \n",++cas);
		cin>>n>>m;
		LL M=1LL<<(n-2);
		int cnt=0;
		for(LL s=0;s<M;s++){
			LL ans[11];
			LL S=(s<<1)+1+(1LL<<(n-1));
			bool bk=0;
			for(LL bas=2;bas<=10;bas++){
				LL res=0;
				for(LL j=0;j<n;j++){
					res*=bas;
					if(S&(1LL<<j)){
						res++;
					}
				}
				bool ok=0;
				for(LL i=2;i*i<=res;i++){
					if(res%i==0){
						ok=1;
						ans[bas]=i;
						break;
					}
				}
				if(!ok)break;
				if(bas==10){
					printf("%lld ",res);
					for(LL bas=2;bas<=10;bas++)printf("%lld ",ans[bas]);
					puts("");
					cnt++;
					if(cnt==m){
						bk=1;
						break;
					}
				}
				
				//printf("%lld ",res);
			}//puts("");
			if(bk)break;
			
			
			
		}
		
		
		
	}
	
	
	
}
