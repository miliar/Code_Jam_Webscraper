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
const string name = "c";

const int NMAX = 1010;

int n, w, h, used[NMAX], d[NMAX], g[NMAX][NMAX];
int x1[NMAX], y1[NMAX], x2[NMAX], y2[NMAX];

int calc(int a, int b) {
	int res = 0;
	if (x1[b] > x2[a] && y1[b] > y2[a]) res = max(x1[b] - x2[a], y1[b] - y2[a]);
	else if (x1[b] > x2[a] && y2[b] < y1[a]) res = max(x1[b] - x2[a], y1[a] - y2[b]);
	else if (x1[b] > x2[a]) res = x1[b] - x2[a];
	else if (x2[b] < x1[a] && y2[b] < y1[a]) res = max(x1[a] - x2[b], y1[a] - y2[b]);
	else if (x2[b] < x1[a] && y1[b] > y2[a]) res = max(x1[a] - x2[b], y1[b] - y2[a]);
	else if (x2[b] < x1[a]) res = x1[a] - x2[b];
	else if (y1[b] > y2[a]) res = y1[b]- y2[a];
	else if (y2[b] < y1[a]) res = y1[a]- y2[b];

	//cerr << a << " " << b <<  " " << res << endl;
	return max(res - 1, 0);
}

void solve() {
	cin >> w >> h >> n;
	x1[0] = -1, x2[0] = -1;
	y1[0] = 0, y2[0] = h;
	for (int i = 1; i <= n; ++i)
		cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
	x1[n + 1] = w, x2[n + 1] = w;
	y1[n + 1] = 0, y2[n + 1] = h;
	n += 2;

	forn(i, n)
		forn(j, n)
			g[i][j] = calc(i, j);

	seta(used, 0);
	forn(i, n)
		d[i] = w + 1;
	d[0] = 0;
	forn(i, n) {
		int v = -1;
		forn(j, n)
			if (!used[j] && (v == -1 || d[v] > d[j])) v = j;
		used[v] = 1;
		forn(j, n)
			d[j] = min(d[j], d[v] + g[v][j]);
	}
	cout << d[n - 1] << endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);
#endif

	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}