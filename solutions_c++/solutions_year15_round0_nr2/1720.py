#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int a[1003];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int cas; scanf("%d",&cas);
	for(int t=1;t<=cas;t++)
	{
		int n; scanf("%d",&n);
		int mx=0,ans=999999999;
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			mx=max(mx,a[i]);
		}
		for(int now=1;now<=mx;now++)
		{
			int res=now;
			for(int i=1;i<=n;i++)
				if(a[i]>now)
				{
					int x=a[i]-now;
					res+=x/now;
					if(x%now) res++;
				}
			ans=min(ans,res);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}