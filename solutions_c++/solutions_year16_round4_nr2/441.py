#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>

using namespace std;

#define in_str(b) scanf("%s",(b))
#define in_int1(a) scanf("%d",&(a))
#define in_int2(a,b) scanf("%d%d",&(a),&(b))
#define in_int3(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
#define in_int4(a,b,c,d) scanf("%d%d%d%d",&(a),&(b),&(c),&(d))
#define so(a) sort((a).begin(), (a).end())
#define rso(a) sort((a).rbegin(), (a).rend())
#define mp(a,b) make_pair(a,b)
#define mset(a,n) memset(a,n,sizeof(a))
#define readints(mas,n) for (int _i=0;_i<(n);_i++) in_int1((mas)[_i])
#define readdoubles(mas,n) for (int _i=0;_i<(n);_i++) scanf("%lf", &(mas)[_i])
#define unq(src) src.erase(unique((src).begin(), (src).end()), (src).end())
#define MOD 1000000007
typedef pair<int, int> pii;
typedef long long ll;
typedef pair<ll, ll> pll;

double mas[210];
double dp[210][210];
int k;

double go(int n, int yes)
{
	if (n == 0) return (yes + yes == k) ? 1.0 : 0.0;
	double& ans = dp[n][yes];
	if (ans < -0.5)
	{
		ans = 0.0;
		if (yes + yes < k)ans += mas[n - 1] * go(n - 1, yes + 1);
		int no = k - n - yes;
		if (no + no < k)ans += (1.0 - mas[n - 1]) * go(n - 1, yes);
	}
	return ans;
}

void Solve()
{
	int i, j, m, n;

	int tests;
	in_int1(tests);
	for (int test = 1; test <= tests; test++)
	{
		in_int2(n, k);
		double ma[210];
		for (i = 0; i < n; i++)
		{
			scanf("%lf", &ma[i]);
		}
		double best = 0.0;
		fprintf(stderr, "%d\n", test);
		sort(ma, ma + n);
		for (i = 0; i <= k; i++)
		{
			int l = 0;
			for (j = 0; j < i; j++) mas[l++] = ma[j];
			for (j=n-(k-i);j<n;j++) mas[l++] = ma[j];
			for (int ii = 0; ii <= k; ii++) for (int jj = 0; jj <= k; jj++) dp[ii][jj] = -1.0;
			double ret = go(k, 0);
			best = max(best, ret);
		}
		/*
		int besti = 0;
		for (i = 0; i < 1 << n; i++)
		{
			int cnt = 0;
			int l = 0;
			for (j = 0; j < n; j++)
			{
				if (i&(1 << j))
				{
					mas[l++] = ma[j];
					cnt++;
				}
			}
			if (cnt != k) continue;
			for (int ii = 0; ii <= k; ii++) for (int jj = 0; jj <= k; jj++) dp[ii][jj] = -1.0;
			double ret = go(k, 0);
			if (ret > best)
			{
				besti = i;
			}
			best = max(best, ret);
		}
		*/
		/*
		for (int ii = 0; ii <= k; ii++) for (int jj = 0; jj <= k; jj++) dp[ii][jj] = -1.0;
		sort(ma, ma + n);
		for (i = j = 0; i < k / 2; i++)
		{
			mas[j++] = ma[i];
			mas[j++] = ma[n - i - 1];
		}

		double ans = go(k, 0);
		*/

		printf("Case #%d: %.10lf", test, best);
		/*
		for (i = 0; i < n; i++) if (besti&(1 << i)) printf(" %.2lf", ma[i]);
		printf("\n");
		sort(ma, ma + n);
		for (i = 0; i < n; i++) printf(" %.2lf", ma[i]);
		*/
		printf("\n");
	}
}

int main()
{
#ifdef __LOCAL_RUN__
	FILE *res_output = freopen("output.txt", "wt", stdout);
	FILE *res_input = freopen("input.txt", "rt", stdin);
	Solve();
#else
	Solve();
#endif
	return 0;
}