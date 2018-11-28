#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<vector>
#include<queue>
#include<string>
#include<sstream>
#define eps 1e-9
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define MAXN 1005
#define MAXM 40005
#define INF 0x3fffffff
using namespace std;
typedef long long LL;
int i,j,k,n,m,x,y,T,ans,big,cas,num,len;
bool flag;
int a[1005],s;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d",&n);
		for (i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			big=max(big,a[i]);
		}
		ans=INF;
		
		for (i=1;i<=big;i++)
		{
			int now=i,tm=0;
			for (j=1;j<=n;j++)
			{
				s=(a[j]+i-1)/i;
				now+=s-1;
			}
			//printf("%d %d\n",i,now);
			ans=min(ans,now);
		}
		printf("Case #%d: %d\n",++cas,ans);
	}
	return 0;
}
