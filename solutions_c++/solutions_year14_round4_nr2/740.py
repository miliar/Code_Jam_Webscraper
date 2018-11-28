#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>

#define maxlongint 2147483647
#define LL long long
#define pb push_back
#define mp make_pair

using namespace std;

struct dwell
{
	int x,y;
}a[1010];

int b[1010],l[1010],r[1010],dp[1010][1010];
int T,n,cs=0;

inline bool cmp(const dwell &a,const dwell &b)
{
	return a.x<b.x;
}

inline int Checkl(int x,int y)
{
	if(x<=y)return 0;
	return x-y;
}

inline int Checkr(int x,int y)
{
	if(x>=y)return 0;
	return y-x;
}

int main()
{
	freopen("123.in","r",stdin);
	freopen("123.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&a[i].x);
			a[i].y=i;
		}
		sort(a+1,a+n+1,cmp);
		for(int i=1;i<=n;i++)
			b[a[i].y]=i;
		memset(dp,0,sizeof(dp));
		memset(l,0,sizeof(l));
		memset(r,0,sizeof(r));
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				if(j<i && b[j]>b[i])
					l[i]++;
				else if(j>i && b[j]>b[i])
					r[i]++;
		for(int i=1;i<=n;i++)//一共移动了i个
			for(int x=0;x<=i;x++)//在左边放x个
			{
				int y=i-x;//在右边放y个
				dp[x][y]=maxlongint;
				if(x)dp[x][y]=min(dp[x][y],dp[x-1][y]+l[a[i].y]);
				if(y)dp[x][y]=min(dp[x][y],dp[x][y-1]+r[a[i].y]);
			}
		int ans=maxlongint;
		for(int i=0;i<=n;i++)ans=min(ans,dp[i][n-i]);
		printf("Case #%d: %d\n",++cs,ans);
	}
	return 0;
}
