#pragma comment(linker, "/STACK:600000000")
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <list>

#include <ctime>
#include <cassert>

using namespace std;

typedef long double ldb;
typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

#define y0 wwwwwww
#define y1 qqqqqqq
#define next NEXT
#define prev PREV
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define ford(i, n) for (int i = (int) n - 1; i >= 0; i--)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define last(a) a[a.size() - 1]
#define mp make_pair
#define fs first
#define sc second

template <class T> T sqr(T x) { return x * x; }

double const pi = 3.1415926535897932384626433832795;
int const inf = (int) 1e9;
int64 const inf64 = (int64) 4e18;
const string name = "a";

const int NMAX = 21;

int n, m, k, ans[NMAX];

void solve(int t) {
	cin >> n >> m >> k;
	forn(i, k)
		ans[i] = 0;
	ans[k] = k;
	for (int i = k + 1; i <= m; ++i) {
		ans[i] = m;
		for (int j = 0; j < i; ++j) {
			int wrong = ans[j] + ans[i - j - 1];
			int right = min(i, ans[min(j, k - 1) + min(i - j - 1, k - 1) + 1]);
			ans[i] = min(ans[i], max(right, wrong + 1));
		}
	}
	printf("Case #%d: %d\n", t, ans[m] * n);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);
#endif

	int tests;
	cin >> tests;
	forn(i, tests)
		solve(i + 1);

	return 0;
}