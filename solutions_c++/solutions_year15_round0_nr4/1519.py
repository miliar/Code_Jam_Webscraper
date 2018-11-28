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
const string name = "d";

int x, r, c;

string solve() {
	cin >> x >> r >> c;
	if (r * c % x != 0) return "RICHARD";
	if (x > max(r, c)) return "RICHARD";
	if (x >= min(r, c) * 2 + 1) return "RICHARD";
	if (x == r * c) return "GABRIEL";
	if (x >= 7) return "RICHARD";
	if (x <= min(r, c) + 1) return "GABRIEL";

	if (r > c) swap(r, c);

	if (x == 1 || x == 2 || x == 3) return "GABRIEL";
	if (r == 2) return "RICHARD";
	if (x == 4) return "GABRIEL";
	if (x == 6) return "RICHARD";
	return "GABRIEL";
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
		printf("Case #%d: %s\n", i + 1, solve().c_str());
	}

	return 0;
}