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
const string name = "b";

int n, a[10010];
multiset <int> S;

int may(int t) {
	forn(s, t) {
		int now = 0;
		forn(j, n)
			now += (a[j] - 1) / (t - s);
		if (now <= s) return true;
	}
	return false;
}

int solve() {
	cin >> n;
	int _max = 0;
	forn(i, n) {
		cin >> a[i];
		_max = max(_max, a[i]);
	}
	int l = 0, r = _max;
	while (l < r) {
		int m = (l + r) / 2;
		if (may(m))
			r = m;
		else
			l = m + 1;
	}
	return l;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);
#endif

	int tests;
	cin >> tests;
	forn(i, tests) {
		printf("Case #%d: %d\n", i + 1, solve());
	}

	return 0;
}