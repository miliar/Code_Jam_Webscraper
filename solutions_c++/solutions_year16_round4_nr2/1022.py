#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <utility>
#include <stack>
#include <set>
#include <algorithm>
#include <bitset>
#include <functional>
#include <ctime>
#include <cassert>
#include <valarray>
#include <unordered_map>
#include <unordered_set>
#pragma comment(linker, "/STACK:167772160")

using namespace std;
#pragma region TypeDefs

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef vector< vector<int> > vvint;

#pragma endregion

const int INF = 1e9 + 10;
const ll LINF = ll(2e18) + 10;
const ld PI = acosl(-1);
const double eps = 1e-8;
const ld EPS = 1e-12;

int popcount(int t)
{
	int res = 0;
	for (; t; res += (t & 1), t >>= 1);
	return res;
}

const int N = 17;
int n, k;
double p[N];
double dp[N], ndp[N];

double solve(int mask)
{
	fill(dp, dp + N, 0);
	dp[0] = 1;
	for (int i = 0; i < n; ++i)
		if (mask & (1 << i))
		{
			fill(ndp, ndp + N, 0);
			for (int j = 0; j <= k / 2; ++j)
			{
				ndp[j] += dp[j] * (1 - p[i]);
				ndp[j + 1] += dp[j] * p[i];
			}
			copy(ndp, ndp + N, dp);
		}
	return dp[k / 2];
}

void solve()
{
	double ans = 0;
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; ++i)
		scanf("%lf", &p[i]);
	for (int mask = 0; mask < (1 << n); ++mask)
		if (popcount(mask) == k)
			ans = max(ans, solve(mask));
	printf("%.10lf\n", ans);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen("chocolate.in", "r", stdin);
	//freopen("chocolate.out", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}

#ifdef LOCAL
	fprintf(stderr, "\n\nTime: %.3f", double(clock()) / CLOCKS_PER_SEC);
#endif
	return 0;
}