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

const int NMAX = 205;
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};
const char dd[4] = {'^', '>', 'v', '<'};

int n, m;
char s[NMAX][NMAX];

int check(int xx, int yy) {
	int may = 0;
	forn(j, 4) {
		int ok = 0, x = xx, y = yy;

		while (x + dx[j] >= 0 && x + dx[j] < n && y + dy[j] >= 0 && y + dy[j] < m) {
			if (s[x + dx[j]][y + dy[j]] != '.') {
				ok = 1;
				break;
			}
			x += dx[j];
			y += dy[j];
		}

		if (ok) may = 1;
		if (ok && s[xx][yy] == dd[j]) {
			return 0;
		}
	}
	if (may) return 1;
	else return -1;
}

void solve(int tnum) {
	cin >> n >> m;
	forn(i, n) {
		scanf("%s", s[i]);
	}
	int ans = 0;
	forn(i, n)
		forn(j, m)
		if (s[i][j] !='.') {
			if (check(i, j) == -1) {
				printf("Case #%d: IMPOSSIBLE\n", tnum);
				return;
			}
			ans += check(i, j);
		}
	printf("Case #%d: %d\n", tnum, ans);
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