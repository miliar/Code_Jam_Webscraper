#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#include <set>
#include <functional>
#include <cmath>
#include <string>
#define SIZE 105

using namespace std;
typedef long long int ll;
typedef pair <int,int> P;

char mp[SIZE][SIZE];
int cx[SIZE],cy[SIZE];

int solve()
{
	int n,m;
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++) scanf("%s",&mp[i]);
	memset(cx,0,sizeof(cx));
	memset(cy,0,sizeof(cy));
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(mp[i][j]!='.')
			{
				cx[i]++;
				cy[j]++;
			}
		}
	}
	int cnt=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(mp[i][j]!='.')
			{
				if(mp[i][j]=='<')
				{
					if(cx[i]==1&&cy[j]==1)
					{
						return -1;
					}
					cnt++;
				}
				break;
			}
		}
		for(int j=m-1;j>=0;j--)
		{
			if(mp[i][j]!='.')
			{
				if(mp[i][j]=='>')
				{
					if(cx[i]==1&&cy[j]==1)
					{
						return -1;
					}
					cnt++;
				}
				break;
			}
		}
	}
	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(mp[j][i]!='.')
			{
				if(mp[j][i]=='^')
				{
					if(cx[j]==1&&cy[i]==1)
					{
						return -1;
					}
					cnt++;
				}
				break;
			}
		}
		for(int j=n-1;j>=0;j--)
		{
			if(mp[j][i]!='.')
			{
				if(mp[j][i]=='v')
				{
					if(cx[j]==1&&cy[i]==1)
					{
						return -1;
					}
					cnt++;
				}
				break;
			}
		}
	}
	return cnt;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int ans=solve();
		if(ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
