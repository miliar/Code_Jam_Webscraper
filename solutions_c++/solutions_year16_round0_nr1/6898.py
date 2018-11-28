#include <bits/stdc++.h>
using namespace std;

bool vis[10];

inline void solve()
{
	int x;
	scanf("%d",&x);
	if (x==0)
	{
		puts("INSOMNIA");
		return;
	}
	int cnt=0,now=x;
	memset(vis,0,sizeof(vis));
	while (cnt<10)
	{
		int t=now;
		while (t)
		{
			if (!vis[t%10])
			{
				vis[t%10]=true;
				cnt++;
			}
			t/=10;
		}
		now+=x;
	}
	printf("%d\n",now-x);
}

int main()
{
//	freopen("read.txt","r",stdin);
//	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
