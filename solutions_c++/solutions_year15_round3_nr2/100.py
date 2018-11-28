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

const int NMAX = 10100;

string s, t;
int ss, tt, n;
double d[NMAX], dd[NMAX];
int prefix2[NMAX][NMAX];

void move(int p, double v) {
	forn(f, s.length()) {
		int target = prefix2[p][f];
		dd[target] += v / s.length();
	}
}

void solve(int num) {
	cin >> ss >> tt >> n;
	cin >> s;
	cin >> t;

	if (n < t.length()) {
		printf("Case #%d: 0\n", num);
		return;
	}
	forn(i, t.length())
		if (s.find(t[i]) == string::npos) {
			printf("Case #%d: 0\n", num);
			return;
		}

	int prefix = 0;
	forn(i, t.length()) {
		if (i > 0 && t.substr(0, i) == t.substr(t.length() - i, i))
			prefix = i;
	}

	forn(i, t.length()) {
		forn(j, s.length()) {
			string x = t.substr(0, i);
			x += s[j];
			while (x.length() > 0 && t.substr(0, x.length()) != x) {
				x = x.substr(1, x.length() - 1);
			}
			prefix2[i][j] = x.length();
		}
	}
	
	int need = 1 + (n - t.length()) / (t.length() - prefix);

	double ans = 0;
	seta(d, 0);
	d[0] = 1.0;
	forn(i, n) {
		seta(dd, 0);
		forn(j, t.length() + 1)
			move(j, d[j]);
		forn(j, t.length() + 1)
			d[j] = dd[j];
		ans += d[t.length()];
		d[prefix] += d[t.length()];
		d[t.length()] = 0;
	}

	printf("Case #%d: %.10lf\n", num, need - ans);
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
		solve(i + 1);
		cerr << clock() << endl;
	}

	return 0;
}