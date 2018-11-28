#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second

typedef long long llint;

double a[210],f[210][410],g[210][410];
int n, K;

int main()
{
	freopen("B.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n,&K);
		for(int i=0;i<n;i++) scanf("%lf",&a[i]);
		sort(a,a+n);
		memset(f,0,sizeof f);
		f[0][K]=1;
		for(int i=0;i<K;i++)
			for(int j=0;j<=2*K;j++)
			{
				f[i+1][j+1]+=f[i][j]*a[i];
				f[i+1][j-1]+=f[i][j]*(1-a[i]);
			}
		reverse(a,a+n);
		memset(g,0,sizeof g);
		g[0][K]=1;
		for(int i=0;i<K;i++)
			for(int j=1;j<2*K;j++)
			{
				g[i+1][j+1]+=g[i][j]*a[i];
				g[i+1][j-1]+=g[i][j]*(1-a[i]);
			}
		double ans=0;
		for(int i=0;i<=K;i++)
		{
			double now=0;
			for(int j=0;j<=2*K;j++)
				now+=f[i][j]*g[K-i][2*K-j];
			//printf("%d %d %.10f\n",i, K-i, now);
			if (now>ans)
				ans=now;
		}
		printf("Case #%d: %.10f\n", tt, ans);
		
	}
	
	return 0;
}