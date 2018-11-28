#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <queue>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long big;

const int N=10020;
int n,X,a[N];
bool vis[N];
priority_queue<int>heap;
map<int,int>f;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int i,cas,cass,j;
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%d%d",&n,&X);
		memset(vis,false,sizeof(vis));
		for(i=1;i<=n;i++)
			scanf("%d",&a[i]);
		sort(a+1,a+1+n);
		reverse(a+1,a+1+n);
		int ans=0;
		for(i=1;i<=n;i++)
		if(!vis[i])
		{
			for(j=i+1;j<=n;j++)
				if(a[i]+a[j]<=X&&!vis[j])
					break;
			if(j<=n)
				vis[i]=true,vis[j]=true;
			else vis[i]=true;
			ans++;
		}
		printf("Case #%d: ",cass);
		printf("%d\n",ans);
	}
}
