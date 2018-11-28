#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
typedef long long LL;
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }

void init()
{

}


#define maxn 205

int n, k;
double dp[maxn][maxn];
double p[maxn], p_orig[maxn];

double get_tie_prob()
{
	CLR(dp, 0);
	dp[0][0] = 1.0;
	for (int i = 0; i < k; i++)
		for (int j = 0; j <= i; j++)
		{
			dp[i+1][j+1] += dp[i][j] * p[i];
			dp[i+1][j] += dp[i][j] * (1 - p[i]);
		}
	return dp[k][k/2];
}

void solvecase()
{
	scanf("%d%d", &n, &k);
	CLR(dp, 0);
	for (int i = 0; i < n; i++) scanf("%lf", &p_orig[i]);
	sort(p_orig, p_orig + n);
	double res = 0;
	for (int i = 0; i <= k; i++)
	{
		for (int j = 0; j < i; j++) p[j] = p_orig[j];
		int rgt = k - i;
		int q = i;
		for (int j = n-1; rgt > 0; j--, rgt--) p[q++] = p_orig[j];
		res = max(res, get_tie_prob());
	}
	printf("%.8lf", res);
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define problem_letter "B"
//#define fname "testcpp"
#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
//#define fname problem_letter "-large"
//#define fname problem_letter "-small-practice"
//#define fname problem_letter "-large-practice"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}
