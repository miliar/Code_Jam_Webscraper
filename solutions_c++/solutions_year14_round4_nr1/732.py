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

int a[10010];
int T,n,cap,cs=0;

int main()
{
	freopen("123.in","r",stdin);
	freopen("123.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&cap);
		for(int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		for(int i=1;i+i<=n;i++)swap(a[i],a[n+1-i]);
		int ans=0;
		for(int i=1,j=n;i<=j;i++)
		{
			ans++;
			if(i<j && a[i]+a[j]<=cap)j--;
		}
		printf("Case #%d: %d\n",++cs,ans);
	}
	return 0;
}
