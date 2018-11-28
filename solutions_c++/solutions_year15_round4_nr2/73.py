#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#define eps 0.0000000000001
using namespace std;

int T,Case,n,i,j,k;
long double V,X,l,r,mid;

struct node
{
	long double x,y;
}t[105];
long double p[105];
inline bool cmp(const node &a,const node &b){return a.y<b.y;}

long double Abs(long double x){if(x<0)return -x;return x;}

bool check(long double T)
{
	int i,j;
	long double w,o,res=V,sum=0,aim=V*X;
	for(i=1;i<=n;++i)p[i]=0;
	for(i=1;i<=n;++i)
	{
		
		w=t[i].x*T;
		if(res>0)
		{
			if(w<res)
			{
				p[i]=w;
				sum+=w*t[i].y;
				res-=w;
				continue;
			}
			p[i]=res;
			w-=res;
			res=0;
			sum+=p[i]*t[i].y;
		}
		if(sum/V>X+eps)return false;
		if(Abs(sum/V-X)<eps)return true;
		for(j=1;j<i;++j)
		{
			o=min(p[j],w);
			if((sum+o*(t[i].y-t[j].y))/V>=X-eps)return true;
			sum+=o*(t[i].y-t[j].y);
			p[j]-=o;p[i]+=o;w-=o;
		}
	}
	return false;
}

void read(long double &x)
{
	double y;
	scanf("%lf",&y);
	x=y;
}

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for(;T;--T)
	{
		scanf("%d",&n);read(V);read(X);
		for(i=1;i<=n;++i)read(t[i].x),read(t[i].y);
		if(n==1)
		{
			++Case;
			printf("Case #%d: ",Case);
			if(X!=t[1].y)printf("IMPOSSIBLE\n");
			else printf("%.10lf\n",(double)(V/t[1].x));
			continue;
		}
		sort(t+1,t+n+1,cmp);
		l=0;r=1000000000;
		for(i=1;i<=300;++i)
		{
			mid=(l+r)/2;
			if(check(mid))r=mid;
			else l=mid;
		}
		++Case;
		printf("Case #%d: ",Case);
		if(mid>200000000)printf("IMPOSSIBLE\n");
		else printf("%.10lf\n",(double)mid);
	}
}
