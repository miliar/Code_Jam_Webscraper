#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;

pii p[1<<20];
int n;
int a[1<<20];

int dp[1024][1024];

int getDP(int c, int l)
{
	if (c == n - 1)
		return 0;
	int r = (n - 1 - c) + l;
	int cp = p[c].second;
	//~ printf("DD %d %d %d %d %d\n", n, c, l, r, cp);
	if (cp - l < r - cp)
	{
		for (int i = c + 1; i < n; ++i)
		{
			if (p[i].second < cp)
				++p[i].second;
		}
		return cp - l + getDP(c + 1, l + 1);
	}
	else
	{
		for (int i = c + 1; i < n; ++i)
		{
			if (p[i].second > cp)
			{
				--p[i].second;
			}
		}
		return r - cp + getDP(c + 1, l);
	}
}

int main()
{
	int t, T;
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
			p[i] = make_pair(a[i], i);
		}
		sort(p, p + n);

		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", t, getDP(0, 0));
	}
	return 0;
}
