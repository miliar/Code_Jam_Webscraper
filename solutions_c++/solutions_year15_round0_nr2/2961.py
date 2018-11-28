#include <iostream>
#include<time.h>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<string.h>
#include<assert.h>
using namespace std;
#define LL(x) ((x)<<1)
#define RR(x) ((x)<<1|1)
typedef __int64 lld;
const int BIT = 100;
const int INF = 1000000000;
const int MAX = 2004800;
const int MOD = 1000000007;
int a[MAX];
int calc(int a[],int n,int lim)
{
	int i,ret=0;
	for (i=0;i<n;i++)
	{
		if(a[i]>lim)
		{
			if (a[i] % lim == 0)
				ret += a[i] / lim - 1;
			else ret += a[i] / lim;
		}
	}
	return ret;
}
int main()
{
	int i, j, k, n;
	int ioflag, Q;
	
	int CS = 1;
	freopen("E:/B-small-attempt1.in", "r", stdin);
	freopen("E:/ans.out", "w", stdout);
	int T;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		int ans = 0;
		for (i=0;i<n;i++)
		{
			scanf("%d", &a[i]);
			ans = max(ans, a[i]);
		}
		int lim = ans;
		for (i=1;i<=lim;i++)
		{
			int tmp = calc(a, n, i);
			ans = min(ans, i + tmp);
		}
		printf("Case #%d: %d\n",CS++, ans);
	}
	return 0;
}
/*

5 4
1 2 3 4 1
1 3 1 4

5 5
1 2 3 4 1
1 3 1 4 2

10 28
1 2256 998 11266 1000000000 12266981 7777777 12345 110 3214
2 1 2257 2256 997 998 11264 11266 11267 999999999 1000000000 12266991 12266981 7777777 12345 110 3214 112 1 2256 998 11266 1000000000 12266981 7777777 12345 110 3214

*/
