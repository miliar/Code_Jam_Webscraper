#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
struct snode
{
	int fr,to;
	int w;
	bool operator <(snode ano)const
	{
		return w<ano.w;
	}
}mys[1000001];int pmys;
int leader[1001];
int nx[1001],ny[1001],nz[1001];
int find(int iv)
{
	return leader[iv]?leader[iv]=find(leader[iv]):iv;
}
#define union union__
bool union(int ia,int ib)
{
	int ta=find(ia),tb=find(ib);
	if(ta==tb)return false;
	leader[ta]=tb;
	return true;
}
int n,nlim;
void task()
{
	scanf("%d%d",&n,&nlim);
	rep(i,n)
	{
		scanf("%d%d%d%*d%*d%*d",&nx[i],&ny[i],&nz[i]);
		leader[i]=0;
	}
	pmys=0;
	rep(i,n)
	{
		rep(j,n)
		{
			#define sqr(x) ((x)*(x))
			mys[++pmys]=(snode){i,j,sqr(nx[i]-nx[j])+sqr(ny[i]-ny[j])+sqr(nz[i]-nz[j])};
		}
	}
	sort(mys+1,mys+pmys+1);
	int tot=0;
	rep(p,pmys)
	{
		union(mys[p].fr,mys[p].to);
		if(find(1)==find(2))
		{
			tot=mys[p].w;
			break;
		}
	}
	printf("%.10f\n",sqrt(tot+0.0));
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
