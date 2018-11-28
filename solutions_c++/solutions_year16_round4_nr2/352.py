#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

double P[300],f[300][600],ans;
int n,K;
bool use[300];

void check()
{
	memset(f,0,sizeof(f));
	int w=0;
	f[0][300]=1;
	for (int i=1;i<=n;i++)
	{
		if (!use[i]) continue;
		w++;
		for (int j=-w;j<=w;j++)
			f[w][300+j]=f[w-1][300+j-1]*P[i]+f[w-1][300+j+1]*(1.-P[i]);
	}
	ans=max(ans,f[w][300]);
}
/*
void dfs(int w,int _s)
{
	if (w>n)
	{
		if (_s==K) check();
		return;
	}
	if (_s>K) return;
	use[w]=1;
	dfs(w+1,_s+1);
	use[w]=0;
	dfs(w+1,_s);
}
*/

int main()
{
	freopen("B1.in","r",stdin);
	freopen("B1.out","w",stdout);
	int T,Tt=0;
	scanf("%d",&T);
	for (;T--;)
	{
		scanf("%d%d",&n,&K);
		for (int i=1;i<=n;i++) scanf("%lf",&P[i]);
		sort(P+1,P+n+1);
		ans=0;
		for (int i=0;i<=K;i++)
		{
			memset(use,0,sizeof(use));
			for (int j=1;j<=i;j++) use[j]=1;
			for (int j=1;j<=K-i;j++) use[n-j+1]=1;
			check();
			if (ans>0.8)
			{
				int xx=1;xx--;
			}
		}
		printf("Case #%d: %lf\n",++Tt,ans);
	}
}