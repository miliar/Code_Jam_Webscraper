#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;
char str[1005];
int main(){
	freopen("E:A-large.in","r",stdin);
	freopen("E:A-large.out","w",stdout);
	int i,j,n,m,T,smax,ans,vans,vcase=0;
	scanf("%d",&T);
	while(T--){
		ans=0;vans=0;
		scanf("%d",&smax);
		scanf("%s",str);
		for(i=0;i<=smax;i++){
			if(i>vans){
				ans+=i-vans;
				vans=i;
			}
			vans+=str[i]-'0';
		}
		printf("Case #%d: %d\n",++vcase,ans);
	}
	return 0;
}