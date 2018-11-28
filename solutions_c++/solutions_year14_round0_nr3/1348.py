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

const int dx[8] = {1, 1, 1, 0, 0, -1, -1, -1};
const int dy[8] = {1, 0, -1, 1, -1, 1, 0, -1};

int n, m, x, cnt[210][210], used[210][210], ept;
char ans[210][210];

int dfs(int x, int y) {
	if (cnt[x][y] == -1)
		return 0;
	used[x][y] = 1;
	ept++;
	if (cnt[x][y] != 0) return 1;
	int i = x, j = y;
	forn(f, 8)
		if (i + dx[f] >= 0 && i + dx[f] < n && j + dy[f] >= 0 && j + dy[f] < m && !used[i + dx[f]][j + dy[f]])
			dfs(i + dx[f], j + dy[f]);
	return 1;
}

int check() {
	forn(i, n)
		forn(j, m)
		if (ans[i][j] != '*') {
			cnt[i][j] = 0;
			forn(f, 8)
				if (i + dx[f] >= 0 && i + dx[f] < n && j + dy[f] >= 0 && j + dy[f] < m && ans[i + dx[f]][j + dy[f]] == '*')
					cnt[i][j]++;
		}
		else cnt[i][j] = -1;
	seta(used, 0);
	ept = 0;
	int stx = -1, sty = -1;
	forn(i, n)
		forn(j, m)
			if (ans[i][j] == 'c') {
				if (stx >= 0)
					return 0;
				stx = i, sty = j;
			}
	if (!dfs(stx, sty)) return 0;
	if (x + ept != n * m)
		return 0;
	return 1;
}

void print() {
	forn(i, n)
		cout << ans[i] << endl;
	if (!check()) {
		cerr << "CHECK FAILED!" << endl;
		exit(0);
	}
}

int triv() {
	forn(msk, 1 << (n * m)) {
		int cnt = 0;
		forn(i, n)
			forn(j, m)
				if (msk & (1 << (i * m + j))) ans[i][j] = '*', cnt++;
				else ans[i][j] = '.';
		if (cnt != x) continue;
		forn(xx, n)
			forn(yy, m) {
				if (ans[xx][yy] == '*') continue;
				ans[xx][yy] = 'c';
				if (check())
					return 1;
			}
	}
	return 0;
}

void solve() {
	seta(ans, 0);
	cin >> n >> m >> x;
	/*if (triv()) {
		print();
	} else {
		cout << "Impossible" << endl;
	}
	return;*/

	if (x == n * m - 1) {
		forn(i, n)
			forn(j, m)
				if (i != n - 1 || j != m - 1) ans[i][j] = '*';
				else ans[i][j] = '.';
		ans[n - 1][m - 1] = 'c';
		print();
		return;
	}
	if (n == 1) {
		forn(i, m)
			if (i < x) ans[0][i] = '*';
			else ans[0][i] = '.';
		ans[n - 1][m - 1] = 'c';
		print();
		return;
	}
	if (m == 1) {
		forn(i, n)
			if (i < x) ans[i][0] = '*';
			else ans[i][0] = '.';
		ans[n - 1][m - 1] = 'c';
		print();
		return;
	}
	forn(i, n - 1)
		forn(j, m - 1) {
			int l = n * m - (n - i) * (m - j);
			int r = l + (n - i - 2) * (m - j - 2);
			if (l <= x && x <= r) {
				int now = x - l;
				forn(ii, n)
					forn(jj, m)
						if (ii < i || jj < j) ans[ii][jj] = '*';
						else ans[ii][jj] = '.';
				int mod = m - j - 2;
				forn(f, now)
					ans[i + f / mod][j + f % mod] = '*';
				ans[n - 1][m - 1] = 'c';
				print();
				return;
			}
		}

/*	if (triv()) {
		cout << endl << n << " " << m << " " << x << endl;
		print();
		exit(0);
	}*/

	cout << "Impossible" << endl;
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
		cout << "Case #" << i + 1 << ":" << endl;
		solve();
		cerr << i + 1 << " " << clock() << endl;
	}

	return 0;
}