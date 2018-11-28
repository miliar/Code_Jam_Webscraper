#include<cstdio>
#include<vector>
using namespace std;

vector<int> g[2010];
int t[2010];
int size[2010];
int w[2010];
bool vis[2010];

int main()
{
int T;
scanf("%d", &T);
for (int tt=1; tt<=T; tt++)
{
	printf("Case #%d: ", tt);
	int n, i, j, k;
	scanf("%d", &n);
	for (i=0; i<=n; i++)
	{
		size[i] = 0;
		vis[i] = 0;
	}	
	for (i=0; i<n; i++)
	{
		scanf("%d", &t[i]);
		for (j=i-1; j>=0; j--)
		{
			if(t[j] == t[i]-1)
			{
				g[j].push_back(i);
				size[i]++;
				break;
			}
		}	
		for (j=i-1; j>=0; j--)
		{
			if(t[j] == t[i])
			{
				g[i].push_back(j);
				size[j]++;
				break;
			}
		}
	}	
	for (i=0; i<n; i++)
	{
		scanf("%d", &t[i]);
	}
	for (i=n-1; i>=0; i--)
	{
		for (j=i+1; j<n; j++)
		{
			if(t[j] == t[i]-1)
			{
				g[j].push_back(i);
				size[i]++;
				break;
			}
		}	
		for (j=i+1; j<n; j++)
		{
			if(t[j] == t[i])
			{
				g[i].push_back(j);
				size[j]++;
				break;
			}
		}
	}	
	
	for (i=1; i<=n; i++)
	{
		for (j=0; j<n; j++)
		{
			if(vis[j]) continue;
			if(size[j]==0)
			{
				w[j] = i;
				vis[j] = 1;
				for (k=0; k<g[j].size(); k++)
					size[ g[j][k] ]--;
				break;
			}
		}
	}
	
	for (i=0; i<n; i++)
		printf("%d ", w[i]);
	printf("\n");	
	
	for (i=0; i<=n; i++)
		g[i].clear();
	
}
return 0;
}

