#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;
int vf[12];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,n,m,T,ans,vcase=0,k,cnt;
	scanf("%d",&T);
	while(T--){
		memset(vf,0,sizeof(vf));
		scanf("%d",&n);
		if(n==0) printf("Case #%d: INSOMNIA\n",++vcase);
		else{
			m=n;
			cnt=0;
			while(1){
				k=m;
				while(k){
					if(vf[k%10]==0){
						vf[k%10]++;
						cnt++;
					}
					k/=10;
				}
				if(cnt==10) break;
				m+=n;
			}
			printf("Case #%d: %d\n",++vcase,m);
		}
	}
	return 0;
}