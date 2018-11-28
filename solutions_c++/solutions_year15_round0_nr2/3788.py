#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int pan[1010];
int dp[1010][1010];
int n;
int mmax;

int calc2(int mmax, int k)
{
	if(mmax <= k)
		return 0;
	else if(dp[mmax][k] != -1)
		return dp[mmax][k];
	int mmin = mmax;
	for (int i = 1; i < mmax; ++i)
	{
		mmin = min(1 + calc2(i, k) + calc2(mmax - i, k), mmin);
	}
	return dp[mmax][k] = mmin;
}

int main()
{
	int T;
	int ca = 0;
	freopen("B-large.in", "r", stdin);
	//freopen("out3.txt", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		memset(dp, -1, sizeof(dp));
		mmax = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &pan[i]);
			mmax = max(mmax, pan[i]);
		}

		int res = mmax;
		for (int k = 1; k <= mmax; ++k)
		{
			int tmp = 0;
			for (int i = 0; i < n; ++i)
			{
				tmp += calc2(pan[i], k);
			}
			res = min(res, tmp + k);
		}

		printf("Case #%d: ", ++ca);

		printf("%d\n", res);
	}
	return 0;
}