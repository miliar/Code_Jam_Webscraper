#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
long long t,p,n,m,x[1100],y[1100],z[1100],a[2100];
long long g=1000002013;
struct node{
	long long a,b;
}w[2100],nw[2100],hei[2100];
int cmp(node a,node b){
	return a.a<b.a;
}
long long suan(long long x){
	return ((n+n-x+1)*x/2)%g;
}
long long doit(int r,int l){
	if(r>l)return 0;
	long long m=100000000000000ll,k;
	for(int i=r;i<=l;i++)
	if(hei[i].b<m){
		m=hei[i].b;
		k=i;
	}
	long long ans=((m%g)*suan(hei[l].a-hei[r-1].a))%g;
	for(int i=r;i<=l;i++)
		hei[i].b-=m;
	ans=(ans+doit(r,k-1)+doit(k+1,l))%g;
	return ans;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for(int q=1;q<=t;q++){
		scanf("%lld%lld",&n,&m);
		p=0;
		long long ans=0;
		for(int i=1;i<=m;i++){
			scanf("%lld%lld%lld",&x[i],&y[i],&z[i]);
			ans=(ans+suan(y[i]-x[i])*z[i])%g;
			p++;
			w[p].a=x[i];
			w[p].b=z[i];
			p++;
			w[p].a=y[i];
			w[p].b=-z[i];
			}
		sort(w+1,w+p+1,cmp);
		int np=0;
		w[0].a=-1;
		for(int i=1;i<=p;i++){
			if(w[i].a!=w[i-1].a){
				np++;
				nw[np]=w[i];
				continue;
			}
			nw[np].b+=w[i].b;
		}
		p=np;
		for(int i=1;i<=p;i++)
			w[i]=nw[i];
		hei[0].a=0;
		hei[0].b=0;
		for(int i=1;i<p;i++){
			hei[i].a=hei[i-1].a+w[i+1].a-w[i].a;
			hei[i].b=hei[i-1].b+w[i].b;
		}
		ans=((ans+g-doit(1,p-1))%g+g)%g;
		printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}
