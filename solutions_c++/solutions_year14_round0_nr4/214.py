#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;
double a[1005],b[1005];
int main(){
	//freopen("D-large.in","r",stdin);
	//freopen("D-large.out","w",stdout);
	int i,j,m,n,T,na,nb,ans1,ans2,vcase=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=1;i<=n;i++) scanf("%lf",&a[i]);
		for(i=1;i<=n;i++) scanf("%lf",&b[i]);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		na=n;nb=n;ans1=0;ans2=0;
		while(nb){
			if(a[na]>b[nb]){
				na--;
				nb--;
				ans1++;
			}
			else nb--;
		}
		na=n;nb=n;
		while(na){
			if(b[nb]>a[na]){
				na--;
				nb--;
				ans2++;
			}
			else na--;
		}
		printf("Case #%d: %d %d\n",++vcase,ans1,n-ans2);
	}
	return 0;
}