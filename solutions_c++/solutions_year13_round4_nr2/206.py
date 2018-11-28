#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;
		long long b;
		scanf("%d%lld",&a,&b);b--;
		long long left=0;
		long long right=(1LL<<a);
		while(left+1<right){
			long long M=(left+right)/2;
			long long ue=M;
			long long shita=(1LL<<a)-1-M;
			bool ok=true;
			for(int i=a-1;i>=0;i--){
				if(!(b&(1LL<<i))){
					if(ue){
						ok=false;
						break;
					}
					long long gen=(ue)/2;
					ue-=gen;
					shita-=(1LL<<i)-gen;
				}else{
					if(!ue){
						ok=true;
						break;
					}
					ue--;
					long long gen=1;
					gen+=(ue+1)/2;
					ue-=(ue+1)/2;
					shita-=(1LL<<i)-gen;
				}
			}
			if(ok)left=M;
			else right=M;
		}
		printf("Case #%d: %lld ",t,left);
		left=0;
		right=(1LL<<a);
		while(left+1<right){
			long long M=(left+right)/2;
			long long ue=M;
			long long shita=(1LL<<a)-1-M;
			bool ok=true;
			for(int i=a-1;i>=0;i--){
				if(!(b&(1LL<<i))){
					if(!shita){
						ok=false;
						break;
					}
					long long gen=1;
					shita--;
					gen+=(shita+1)/2;
					shita-=(shita+1)/2;
					ue-=(1LL<<i)-gen;
				}else{
					if(shita){
						ok=true;
						break;
					}
					long long gen=0;
					gen+=(shita)/2;
					shita-=(shita)/2;
					ue-=(1LL<<i)-gen;
				}
			}
			if(ok)left=M;
			else right=M;
		}
		printf("%lld\n",left);
	}
}