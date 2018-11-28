#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

const int N = (int)1e4 + 10;
const int INF = (int)1e9 + 10;
const int C = (int)1e5 + 10;

int x[N];
int sum[N];
int nextEq[N];
int minValue[N], maxValue[N];

void solve()
{
	int n, k;
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n - k + 1; i++)
	{
		scanf("%d", &sum[i]);
	}
	for (int i = 1; i < n - k + 1; i++)
		nextEq[i - 1] = sum[i] - sum[i - 1];
	for (int i = 0; i < k; i++)
	{
		int value = 0;
		minValue[i] = 0;
		maxValue[i] = 0;
		for (int s = i; s < n; s += k)
		{
			minValue[i] = min(minValue[i], value);
			maxValue[i] = max(maxValue[i], value);
			value += nextEq[s];
		}
	}
	int ans = INF;
	for (int i = 0; i < k; i++)
	{
		int S = 0;
		x[i] = S - minValue[i];
		int curSum = 0;
		int curAns = 0;
		int delta = 0;
		int maxX = -INF;
		for (int q = 0; q < k; q++)
		{
			x[q] = S - minValue[q];
			curSum += x[q];
			x[q] += maxValue[q];
			curAns = max(curAns, x[q] - S);
			maxX = max(maxX, x[q]);
		}
		for (int q = 0; q < k; q++)
		{
			if (q == i) continue;
			delta += maxX - x[q];
		}
		int rSK = sum[0] - curSum;
		int lSK = sum[0] - curSum - delta;
		bool ok = false;
		for (int s = lSK; s <= min(rSK, lSK + 2 * k); s++)
		{
			if (s % k == 0)
				ok = true;
		}
		if (ok)
			ans = min(ans, maxX - S);
		else
		{
			int l = 0, r = INF;
			while (r - l > 1)
			{
				int mid = (l + r) / 2;
				lSK = sum[0] - curSum - delta - mid;
				ok = false;
				for (int s = lSK; s <= min(rSK, lSK + 2 * k); s++)
				{
					if (s % k == 0)
						ok = true;
				}
				if (ok)
					r = mid;
				else
					l = mid;
			}
			ans = min(ans, (maxX + (r + k - 2) / (k - 1)) - S);
		}
	}
	printf("%d\n", ans);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		eprintf("%d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
