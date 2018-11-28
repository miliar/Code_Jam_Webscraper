#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int N=105;
int adj[N][N];
int row[N],col[N],n,m;
bool vis[N][N];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t_cnt=0;
	scanf("%d",&t);
	while(t--)
	{
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		memset(vis,0,sizeof(vis));

		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) 
		{
			scanf("%d",&adj[i][j]);
			row[i]=max(row[i],adj[i][j]);
		}
		for(int i=0;i<m;i++) for(int j=0;j<n;j++)
		{
			col[i]=max(col[i],adj[j][i]);
		}
		for(int i=0;i<n;i++) for(int j=0;j<m;j++)
		{
			if(adj[i][j]==row[i]) vis[i][j]=1;
		}
		for(int i=0;i<m;i++) for(int j=0;j<n;j++)
		{
			if(adj[j][i]==col[i]) vis[j][i]=1;
		}

		bool flag=1;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) 
		{
			if(vis[i][j]==0) flag=0;
		}

		printf("Case #%d: ",++t_cnt);
		if(flag) puts("YES");
		else puts("NO");
	}
	return 0;
}
