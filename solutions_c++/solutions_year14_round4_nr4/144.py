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

const int NMAX = 12;

int n, s, ans1, ans2, cur[NMAX];
char buf[NMAX];
string str[NMAX];
int edge[4][128][128], num[4];

void add(int server, int vertex, int yl, const string& str) {
	if (yl == str.length()) return;
	if (edge[server][vertex][str[yl]] == -1)
		edge[server][vertex][str[yl]] = num[server]++;
	add(server, edge[server][vertex][str[yl]], yl + 1, str);
}

int calc() {
	forn(i, s) {
		forn(f, num[i])
			for (char c = 'A'; c <= 'z'; ++c)
				edge[i][f][c] = -1;
		num[i] = 1;
	}
	forn(i, n) {
		add(cur[i], 0, 0, str[i]);
	}
	int sum = 0;
	forn(i, s) {
		sum += num[i];
		if (num[i] == 1) sum--;
	}
	return sum;
}

void update(int ept) {
	if (ept > ans1) ans1 = ept, ans2 = 0;
	if (ept == ans1) ans2++;
}

void rec(int idx) {
	if (idx == n) {
		update(calc());
		return;
	}

	forn(i, s) {
		cur[idx] = i;
		rec(idx + 1);
	}
}

void solve() {
	seta(edge, 255);
	cin >> n >> s;
	forn(i, n) {
		scanf("%s", buf);
		str[i] = buf;
	}

	ans1 = 0, ans2 = 0;
	rec(0);
	cout << ans1 << " " << ans2 << endl;
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