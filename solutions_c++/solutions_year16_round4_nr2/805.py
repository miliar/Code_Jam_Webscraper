//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#define TASK "B-small-attempt0"
//#define TASK "B-large"
#pragma comment(linker, "/STACK:536870912")
#include <cstdio>
#include <iostream>
#include <iomanip> 
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
#include <cassert>
#include <bitset>
#include <unordered_set>
#include <unordered_map>
#include <random>

const int MOD = 1000000003;
const int INF = 1000000001;
const int MAXN = 100000;
const long double EPS = 1e-8;
const int HASH_POW = 29;
const long double PI = acos(-1.0);

using namespace std;

void my_return(int code)
{
#ifdef MYDEBUG
	cout << "\nTime = " << fixed << setprecision(3) << double(clock()) / CLOCKS_PER_SEC << endl;
#endif
	exit(code);
}

long double dp[210][210][210];

long double check(int i, int j, int k)
{
	if (i < 0 || j < 0 || k < 0)
		return 0.0;
	return dp[i][j][k];
}

int main()
{
	cin.sync_with_stdio(0);
	cin.tie(0);
	mt19937 mt_rand(time(0));
#ifdef MYDEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen(TASK".in", "rt", stdin);
	freopen(TASK".out", "wt", stdout);
	/*freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);*/
#endif

	int CASE;
	scanf("%d", &CASE);
	for (int it = 1; it <= CASE; ++it)
	{
		int n, sz;
		long double p[210];

		scanf("%d %d", &n, &sz);
		for (int i = 1; i <= n; ++i)
		{
			double foo;
			scanf("%lf", &foo);
			p[i] = foo;
		}

		long double ans = 0.0;
		for (int msk = 1; msk < (1 << n); ++msk)
		{
			int cnt = 0;
			for (int i = 0; i < n; ++i)
				if (msk & (1 << i))
					++cnt;
			if (cnt != sz)
				continue;

			long double sum = 0.0;
			for (int s = msk; s; s = (s - 1) & msk)
			{
				cnt = 0;
				for (int i = 0; i < n; ++i)
					if (s & (1 << i))
						++cnt;
				if (cnt != sz / 2)
					continue;
				long double tmp = 1.0;
				for (int i = 0; i < n; ++i)
				{
					if (s & (1 << i))
						tmp *= p[i + 1];
					else if (msk & (1 << i))
						tmp *= (1.0 - p[i + 1]);
				}
				sum += tmp;
			}

			if (sum > ans)
				ans = sum;
		}

		printf("Case #%d: %.7lf\n", it, (double)ans);
	}

	my_return(0);
}
