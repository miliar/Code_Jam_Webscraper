#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker,"/STACK:256000000")
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<cassert>
#include<string>
using namespace std;

#define INF 1000000000
#define lint long long
#define pb push_back
#define mp make_pair
#define MOD 1000000007

int a[1005];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc, T = 0;
	scanf("%d", &tc);
	while(tc--)
	{
		int n, i, j;
		scanf("%d", &n);
		int mx = 0;
		for (i = 1; i <= n; ++i)
		{
			scanf("%d", &a[i]);
			mx = max(mx, a[i]);
		}

		int ans = mx;

		for (i = 1; i <= mx; ++i)
		{
			int cur = i;
			for (j = 1; j <= n; ++j)
			{
				if (a[j] <= i) continue;
				cur += (a[j] - 1) / i;
			}
			ans = min(ans, cur);
		}


		printf("Case #%d: %d\n", ++T, ans);
	}
	return 0;
}
