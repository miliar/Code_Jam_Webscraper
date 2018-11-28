#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000ll;
const double eps = 1e-8;

int n, k;
double p[205];

bool mask[205];

double dp[2][205];
double prob()
{
	memset(dp, 0, sizeof(dp));

	int cur = 0, next = 1;
	dp[cur][0] = 1.0;
	for (int j = 0; j < n; j++)
	{
		if (!mask[j])
			continue;

		for (int i = 0; i < 205; i++)
			dp[next][i] = 0.0;

		for (int i = 0; i < k; i++)
		{
			dp[next][i + 1] += dp[cur][i] * p[j];
			dp[next][i] += dp[cur][i] * (1.0 - p[j]);
		}

		swap(cur, next);
	}

	return dp[cur][k / 2];
}

double stupid()
{
	double ans = 0.0;

	int mm = 1 << n;
	for (int i = 0; i < mm; i++)
	{
		memset(mask, 0, sizeof(mask));

		int cnt = 0;
		int x = i;
		int j = 0;
		while (x)
		{
			mask[j++] = (x & 1);
			cnt += (x & 1);
			x >>= 1;
		}

		if (cnt != k)
			continue;

		ans = max(ans, prob());
	}

	return ans;
}

double smart()
{
	double ans = 0.0;

	for (int i = 0; i <= k; i++)
	{
		memset(mask, 0, sizeof(mask));
		for (int j = 0; j < i; j++)
			mask[j] = true;

		for (int j = 0; j < k - i; j++)
			mask[n - 1 - j] = true;

		ans = max(ans, prob());
	}

	return ans;
}

void solve()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%lf", &p[i]);

	sort(p, p + n);

	double b = smart();

	printf("%.8lf", b);

	printf("\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
