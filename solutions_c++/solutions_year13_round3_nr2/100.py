#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

bool vis[10000];
bool vis1[10000];
int ansx[10000],ansy[10000];
int main()
{
	int T,cas=0;

  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);

	scanf("%d",&T);
	while(T--)
	{
		int x,y;
		scanf("%d %d",&x,&y);
		int X=abs(x);
		int Y=abs(y);
		int n=0;
		while(n*(n+1)/2<X+Y||(n*(n+1)/2-X-Y)%2!=0)n++;
		int s=n*(n+1)/2-X-Y;
		s/=2;
		memset(vis,0,sizeof(vis));
		for(int i=n;i>=1;i--)
		{
			if(s>=i)
				vis[i]=1,s-=i;
		}
		memset(vis1,0,sizeof(vis1));
		s=n*(n+1)/2-(X-Y);s/=2;
		for(int i=n;i>=1;i--)
		{
			if(s>=i)
				vis1[i]=1,s-=i;
		}
		memset(ansx,0,sizeof(ansx));
		memset(ansy,0,sizeof(ansy));
		for(int i=1;i<=n;i++)
			if(vis[i]&&vis1[i])
				ansx[i]=-1;
		for(int i=1;i<=n;i++)
			if(!vis[i]&&!vis1[i])
				ansx[i]=1;
		for(int i=1;i<=n;i++)
			if(vis[i]&&!vis1[i])
				ansy[i]=-1;
		for(int i=1;i<=n;i++)
			if(!vis[i]&&vis1[i])
				ansy[i]=1;
		if(x<0)
			for(int i=1;i<=n;i++)
				ansx[i]=-ansx[i];
		if(y<0)
			for(int i=1;i<=n;i++)
				ansy[i]=-ansy[i];
		printf("Case #%d: ",++cas);
		for(int i=1;i<=n;i++)
			if(ansx[i])
			{
				if(ansx[i]>0)
					printf("E");
				else
					printf("W");
			}
			else
			{
				if(ansy[i]>0)
					printf("N");
				else
					printf("S");
			}
		puts("");
	}
}
