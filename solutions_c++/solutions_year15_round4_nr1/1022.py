#include <bits/stdc++.h>
#define maxn 102
const int INF=1<<30;
using namespace std;
char mp[maxn][maxn];
int n,m;
int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};
void sol()
{
	char str[]="^v<>";
	//cout<<strchr(str,'v')-str<<endl;
	int ans=0;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		{
			if(mp[i][j]=='.')
				continue;
			int mov=1<<30;
			for(char c:"^v<>")
			{
				if(!c) break;
				int t=strchr(str,c)-str;
				int nx=i+dx[t],ny=j+dy[t];
				while(0<=nx&&nx<n && 0<=ny&&ny<m)
				{
					if(strchr(str,mp[nx][ny]))
					{
						if(mov>(mp[i][j]!=c?1:0))
							mov=(mp[i][j]!=c?1:0);
						break;
					}
					nx+=dx[t],ny+=dy[t];
				}
			}
			if(mov>1)
			{
				puts("IMPOSSIBLE");
				return;
			}
			ans+=mov;
		}
	printf("%d\n",ans);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%s",mp[i]);
		printf("Case #%d: ",cas);
		sol();
	}
	return 0;
}
