#include<bits/stdc++.h>
#define eps 1e-9
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define MAXN 1005
#define MAXM 40005
#define INF 0x3fffffff
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)1)
using namespace std;
typedef long long LL;
int i,j,k,n,m,x,y,T,ans,big,cas,num,len;
bool flag;
int vis[4][105][105],cov[4][105][105];
char s[105][105];

int main()
{	freopen("a.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
		{
			scanf("%s",s[i]);
		}
		memset(vis,0,sizeof(vis));
		memset(cov,0,sizeof(cov));
		ans=0;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (s[i][j]!='.')
				{
					if (s[i][j]=='<')
					{
						vis[0][i][j]=1;
					}
					cov[0][i][j]=1;
					break;
				} 
			}
		}
		
		for (i=0;i<n;i++)
		{
			for (j=m-1;j>=0;j--)
			{
				if (s[i][j]!='.')
				{
					if (s[i][j]=='>')
					{
						vis[1][i][j]=1;
					}
					cov[1][i][j]=1;
					break;
				} 
			}
		}
		
		for (j=0;j<m;j++)
		{
			for (i=0;i<n;i++)
			{
				if (s[i][j]!='.')
				{
					if (s[i][j]=='^')
					{
						vis[2][i][j]=1;
					}
					cov[2][i][j]=1;
					break;
				} 
			}
		}
		
		for (j=0;j<m;j++)
		{
			for (i=n-1;i>=0;i--)
			{
				if (s[i][j]!='.')
				{
					if (s[i][j]=='v')
					{
						vis[3][i][j]=1;
					}
					cov[3][i][j]=1;
					break;
				} 
			}
		}


		printf("Case #%d: ",++cas);
		//===================================
		flag=false;
		ans=0;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (s[i][j]!='.')
				{
					int sum1=0;
					int sum2=0;
					for (k=0;k<4;k++)
					{
						sum1+=cov[k][i][j];
						sum2+=vis[k][i][j];
					}
					//printf("%d %d %d\n",i,j,sum);
					if (sum1==4) 
					{
						flag=true;
						printf("IMPOSSIBLE\n");
						break;
					}
					if (sum2>0) ans++;
				} 
			}
			if (flag) break;
		}
		
		if (flag) continue;
		printf("%d\n",ans);
		
		
	} 
	return 0;
}
