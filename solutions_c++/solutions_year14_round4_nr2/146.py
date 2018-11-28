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

int n, a[1010], b[1010], ans;

int p[1010];

int triv() {
	int ok = 0;
	forn(i, n) {
		ok = 1;
		for (int j = 0; j < i; ++j)
			if (a[p[j]] > a[p[j + 1]]) { ok = 0; break; }
		for (int j = i; j < n - 1; ++j)
			if (a[p[j]] < a[p[j + 1]]) { ok = 0; break; }
		if (ok) break;
	}
	if (!ok) return n * n;

	int now = 0;
	forn(i, n)
		forn(j, i)
			if (p[j] > p[i]) now++;
	return now;
}

int l, r;

void make() {
	int idx = l;
	for (int i = l; i <= r; ++i)
		if (a[idx] > a[i]) idx = i;

	if (idx - l < r - idx) {
		while (idx > l) {
			ans++;
			swap(a[idx], a[idx - 1]);
			idx--;
		}
		l++;
	} else {
		while (idx < r) {
			ans++;
			swap(a[idx], a[idx + 1]);
			idx++;
		}
		r--;
	}
}

void solve() {
	cin >> n;
	forn(i, n) {
		cin >> a[i];
	}

/*	forn(i, n)
		p[i] = i;
	int trivans = n * n;
	do {
		trivans = min(trivans, triv());
	} while (next_permutation(p, p + n));*/

	ans = 0;
	l = 0, r = n - 1;
	forn(j, n)
		make();
	cout << ans << endl;

/*	cout << "triv = " << trivans << endl;
	if (trivans != ans) exit(0);*/
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
		cerr << i << endl;
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	cerr << clock() << endl;

	return 0;
}