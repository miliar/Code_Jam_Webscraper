#include <cstdio>
#include <algorithm>
#include <cstring>
#define Sort sort
#define int64 long long

using namespace std;

const int Maxn=1100;
const int64 mo=1000002013;

int64 x[Maxn],y[Maxn],pp[Maxn];
int64 p[Maxn*2],in[Maxn*2],out[Maxn*2];
int64 num[Maxn*2];
int64 n,m;

int Calc(int64 x)
{
	return x * (n + n - x + 1) / 2 % mo;
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	for (int ii=0;ii<Test;++ii)
	{
		printf("Case #%d: ",ii+1);
		scanf("%d%d",&n,&m);
		int tot=0;
		int64 old=0;
		for (int i=0;i<m;++i)
		{
			scanf("%d%d",&x[i],&y[i]);
			scanf("%d",&pp[i]);
			p[tot++]=x[i];p[tot++]=y[i];
			old=(old+(int64)pp[i]*Calc(y[i]-x[i]) % mo) % mo;
		}
		
		Sort(p,p+tot);
		
		int tmp=tot;
		tot=1;
		for (int i=1;i<tmp;++i)
			if (p[i]!=p[tot-1]) p[tot++]=p[i];
		
		memset(in,0,sizeof(in));
		memset(out,0,sizeof(out));
		for (int i=0;i<m;++i)
		{
			for (int j=0;j<tot;++j)
				if (p[j]==x[i]) 
				{
					x[i]=j;
					in[j]+=pp[i];
					break;
				}
			for (int j=0;j<tot;++j)
				if (p[j]==y[i])
				{
					y[i]=j;
					out[j]+=pp[i];
					break;
				}
		}
		
		int64 cost=0;
		for (int i=0;i<tot;++i)
		{
			num[i]+=in[i];
			int64 rest=out[i];
			for (int j=i;rest>0 && j>=0;--j)
			{
				int64 use;
				if (num[j]<rest) use=num[j];
				else use=rest;
				rest-=use;num[j]-=use;
				cost=(cost+use*Calc(p[i]-p[j]) % mo) % mo;
			}
		}
		
		int64 ans=(old-cost) % mo;
		ans=(ans+mo) % mo;
		printf("%d\n",((old-cost) % mo+mo) % mo);
	}
	
	return 0;
}
		
		
		
		
		