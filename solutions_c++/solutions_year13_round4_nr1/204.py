#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#define int64 long long
using namespace std;
const int mo=1000002013;
struct ppp{
	int x,sta;
}b[120000],a[120000];
int i,j,k,l,n,m,T,tim,tot,num,x,y,p;
long long ans;
bool cmp(const ppp&a,const ppp &b){
	return a.x<b.x || a.x==b.x && a.sta>b.sta;
}
long long calc(long long p){
	return (p*n-p*(p-1)/2)%mo;
}
int main(){
	freopen("2A.in","r",stdin);
	freopen("2A.out","w",stdout);
	for(scanf("%d",&T);T--;){
		tim++;
		scanf("%d%d",&n,&m);
		tot=0;
		ans=0;
		for(i=1;i<=m;++i){
			scanf("%d%d%d",&x,&y,&p);
			a[++tot].x=x; a[tot].sta=p;
			a[++tot].x=y; a[tot].sta=-p;
			ans=(ans+(long long)p*calc(y-x))%mo;
		}
		sort(a+1,a+tot+1,cmp);
		num=0;
		for(i=1;i<=tot;++i){
			if(a[i].sta>0){
				b[++num]=a[i];
			}else{
				int x=-a[i].sta;
				for(;;num--){
					if(x<=b[num].sta){
						ans=(ans-(int64)x*calc(a[i].x-b[num].x))%mo;
						b[num].sta-=x;
						break;
					}
					ans=(ans-(int64)b[num].sta*calc(a[i].x-b[num].x))%mo;
					x-=b[num].sta;
				}
			}
		}
		printf("Case #%d: %I64d\n",tim,(ans+mo)%mo);
	}
//	system("pause");
}
			
			
