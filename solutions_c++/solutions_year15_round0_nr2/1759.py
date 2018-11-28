#include<bits/stdc++.h>
using namespace std;
#define maxn 10000+10
int p[maxn];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=0,n;
	scanf("%d",&t);
	while(t--)
	{
		int N=-1;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&p[i]);
			N=max(N,p[i]);
		}
		int ans=N;
		for (int i=1;i<=N;i++)
		{
			int tp=i;
			for (int j=1;j<=n;j++)
			{
				if (p[j]>i)
				{
					if (p[j]%i) tp=tp+p[j]/i;
					else tp=tp+p[j]/i-1;
				}
			}
			ans=min(ans,tp);
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
