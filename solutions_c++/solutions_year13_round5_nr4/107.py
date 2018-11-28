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

int n;
char a[100];
double dp[1<<20];
bool vis[1<<20];
double dfs(int x)
{
	if(vis[x])return dp[x];
	vis[x]=1;
	double ans=0;
	for(int i=0;i<n;i++)
		if(!(x&(1<<i)))
		{
			ans+=1.0/n*(dfs(x|(1<<i))+n);
			int pre=(i-1+n)%n;
			int cnt=0;
			while(x&(1<<pre))
			{
				cnt++;
				ans+=1.0/n*(dfs(x|(1<<i))+n-cnt);
				pre=(pre-1+n)%n;
			}
		}
	dp[x]=ans;
	return ans;
}
void solve()
{
	scanf("%s",a);
	n=strlen(a);
	memset(vis,0,sizeof(vis));
	int now=0;
	for(int i=0;i<n;i++)
		if(a[i]=='X')now|=1<<i;
	printf("%.12f\n",dfs(now));
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++cas);
		solve();
	}
}
