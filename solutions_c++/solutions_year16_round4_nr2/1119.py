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
#define LL long long
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
#define fo(i, n) for (int i = 0; i < (n); i++)
#define foz(i, a) for (int i = 0; i < (a).size(); i++)

void init()
{

}

typedef unsigned int uint;
//typedef long long numt;
//typedef __int128 numt;


double dp[300][300][300];

void solvecase()
{
	memset(dp, 0, sizeof(dp));
	dp[0][0][0] = 1;
	int n, k;
	cin >> n >> k;
	//double p;
	//for (int i = 1; i <= n; ++i) {
	//	cin >> p;
	//	for (int j = 0; j <= i; ++j)
	//		for (int y = 0; y <= j; ++y) {
	//			dp[i][j][y] = dp[i - 1][j][y];
	//			double r2 = 0;
	//			if (y && j)
	//				r2 += p * dp[i - 1][j - 1][y - 1];
	//			if (j)
	//				r2 += (1 - p) * dp[i - 1][j - 1][y];
	//			dp[i][j][y] = max(r2, dp[i][j][y]);
	//		}
	//}
	double p[200];
	for (int i = 1; i <= n; ++i) 
		cin >> p[i-1];
	int t[200];
	for (int i = 0; i < n; ++i)
		t[i] = i >= n-k;
	double best = 0;
	do {
		double loc[200];
		for (int i = 0, j = 0; i < n; ++i) if (t[i]) loc[j++] = p[i];
		double prob = 0;
		for (int i = 0; i < (1 << k); ++i) {
			double r = 1;
			int m = 0;
			for (int j = 0; j < k; ++j) {
				if ((1<<j) & i) {
					++m;
					r *= loc[j];
				}
				else
					r *= 1 - loc[j];
			}
			if (m == k / 2)
				prob += r;
		}
		best = max(best, prob);
	} while (next_permutation(t, t + n));
	printf("%.9lf", best);
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

#define dir "C:/Users/dmarin3/Downloads/"
#define problem_letter "B"
//#define fname "test"
#define fname dir problem_letter "-small-attempt0"
//#define fname dir problem_letter "-small-attempt1"
//#define fname dir problem_letter "-small-attempt2"
//#define fname dir problem_letter "-large"

int main()
{
	cout << fname ".in";
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}
