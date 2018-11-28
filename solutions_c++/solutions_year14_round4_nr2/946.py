#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

const int maxn = 1010;
const int inf = 9999999;

int n, dat[maxn];

int mincount()
{
	static pair<int, int> sorted[maxn];
	for (int i = 0; i < n; i++)
	{
		sorted[i].first = dat[i];
		sorted[i].second = 0;
		for (int j = 0; j < i; j++)
			if (dat[j] > dat[i]) sorted[i].second++;
	}
	
	sort(sorted, sorted + n);
	
	static int h[maxn][maxn];
	h[0][0] = 0;
	for (int i = 0; i <= n - 1; i++)
		for (int j = 0; j + i <= n - 1; j++)
		{
			int cur = i + j;
			if (cur == 0) continue;
			h[i][j] = inf;
			if (i) h[i][j] = min(h[i][j], h[i-1][j] + sorted[cur-1].second);
			if (j) h[i][j] = min(h[i][j], h[i][j-1] + n - cur - sorted[cur-1].second);
		}
		
	int ans = inf;
	for (int i = 0; i <= n - 1; i++)
	{
		ans = min(ans, h[i][n-i-1]);
	}
	
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; j++) scanf("%d", &dat[j]);
		printf("Case #%d: %d\n", i, mincount());
	}
	
	return 0;
}
