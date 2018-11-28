#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;
int a[10010];
bool vis[10010];
void solve()
{
	int X,n;
	scanf("%d %d",&n,&X);
	for(int i=1;i<=n;i++)scanf("%d",&a[i]);
	sort(a+1,a+1+n);
	int ans=0;
	memset(vis,0,sizeof(vis));
	int p=n;
	for(int i=1;i<=n;i++)if(!vis[i])
	{
		ans++;
		while(p>i&&a[p]+a[i]>X)p--;
		if(p>i)
		{
			vis[p]=1;
			p--;
		}
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		solve();
	}
}
