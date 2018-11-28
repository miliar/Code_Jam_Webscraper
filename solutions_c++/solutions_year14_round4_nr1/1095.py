#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int n,m;
int d[10010];

int solve()
{
	int ans=0;
	sort(d,d+n);
	int p=0;
	for(int i=n-1;i>=p;i--)
		{
			ans++;
			if (i==p)break;
			if (i!=p)
				if (d[i]+d[p]<=m)
					p++;
		}
	return ans;
}

int main()
{
	freopen("al.in","r",stdin);
	int tt;
	scanf("%d",&tt);
	for(int ii=1;ii<=tt;ii++)
		{
			scanf("%d%d",&n,&m);
			for(int i=0;i<n;i++)
				scanf("%d",d+i);
			int ans=solve();
			printf("Case #%d: %d\n",ii,ans);
		}
	return 0;
}


