#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <string>

#include <valarray>
#include <complex>
#include <functional>

using namespace std;

typedef long double ld;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

const int N = 210;
const int SHIFT = 105;
ld p[N];

ld dp[N][N];
int n, k;

void read()
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%Lf", &p[i]);
}

ld solve(vector <ld> fp)
{
	for (int i = 0; i <= (int)fp.size(); i++)
	{
		fill(dp[i], dp[i] + N, 0);
	}
	dp[0][SHIFT] = 1;
	for (int i = 0; i < (int)fp.size(); i++)
	{
		for (int shift = 0; shift < N; shift++)
		{
			if (dp[i][shift] == 0)
				continue;
			dp[i + 1][shift + 1] += dp[i][shift] * fp[i];
			dp[i + 1][shift - 1] += dp[i][shift] * (1 - fp[i]);
		}
	}
	return dp[(int)fp.size()][SHIFT];
}

void solve()
{
	sort(p, p + n);
	vector <ld> fp = {};
	ld greedy = 0;
	for (int i = 0; i <= k; i++)
	{
		fp.clear();
		for (int s = 0; s < i; s++)
			fp.push_back(p[s]);
		for (int s = 0; s < k - i; s++)
			fp.push_back(p[n - s - 1]);
		greedy = max(greedy, solve(fp));
	}
	/*
	for (int i = 0; i < (1 << n); i++)
	{
		if (__builtin_popcount(i) != k)
			continue;
		fp.clear();
		for (int s = 0; s < n; s++)
		{
			if (i & (1 << s))
				fp.push_back(p[s]);
		}
		ld cur = solve(fp);
		if (cur > greedy && fabsl(cur - greedy) > 1e-8)
		{
			eprintf("Alarm!");
			printf("Can better: %Lf > %Lf\n", cur, greedy);
			for (int s = 0; s < n; s++)
				if (i & (1 << s))
					printf("%Lf ", p[s]);
			puts("");
			greedy = cur;
		}
	}
	*/
	printf("%.10Lf\n", greedy);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
