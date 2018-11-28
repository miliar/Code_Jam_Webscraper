#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;i++)
#define ll long long
const int N=3105,oo=1000002013;
int T,n,m,Case,s,w[N],z[N],x[N],y[N],p[N],v[N]; ll c[N],ans;
bool cmp(const int i,const int j){return w[i]<w[j];}
ll cal(ll d){return !d?0:(n+n-d+1)*d/2%oo;}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		scanf("%d%d",&n,&m),ans=s=0;
		rep(i,m) scanf("%d%d%d",w+i,w+m+i,z+i),ans=(ans+cal(w[m+i]-w[i])*z[i])%oo,
			w[i]*=2,w[m+i]*=2,w[i+m+m]=w[i+m]+1;
//		printf("%d\n",ans);
		rep(i,m*3) p[i]=i; sort(p,p+m*3,cmp);
		rep(i,m*3){
			if (!i || w[p[i]]!=w[p[i-1]]) v[++s]=w[p[i]];
			if (p[i]<m) x[p[i]]=s; else y[p[i]-m]=s;
			}
//		rep(i,m) printf("%d %d\n",x[i],y[i]);
		s+=2;
		rep(i,m) c[x[i]]+=z[i],c[y[i]+1]-=z[i]; rep(i,s) c[i+1]+=c[i];
		rep(i,s) while (c[i]){
			int j=i; ll d=c[i];
			while (c[j]) d=min(d,c[j++]);
//			printf("%d %d %lld %d\n",i,j,d,v[j-1]/2-v[i]/2);
//			rep(k,j+1) printf("%d ",c[k]); puts("");
			for (int k=i;k<j;k++) c[k]-=d;
			ans=(ans-d%oo*cal(v[j-1]/2-v[i]/2))%oo;
			}
		printf("Case #%d: %d\n",++Case,(ans+oo)%oo);
		}
	return 0;
}
