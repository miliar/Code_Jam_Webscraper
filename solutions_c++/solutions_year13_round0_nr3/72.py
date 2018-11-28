#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define next NEXTHUI
#define prev PREVHUI
#define y1 Y1HUI

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

vector<string> ans;

void solve() {
	string l, r;
	cin >> l >> r;
	while (l.size() < 110)
		l = '0' + l;
	while (r.size() < 110)
		r = '0' + r;
	int res = 0;
	forn(i, ans.size())
		if (l <= ans[i] && ans[i] <= r)
			res++;
	cout << res << endl;
}

void add(string s) {
	vector<int> a;
	int n = s.length();
	a.resize(n * 2 - 1);
	forn(i, n)
		forn(j, n)
			a[i+j] += (s[i] - '0') * (s[j] - '0');
	forn(i, n * 2 - 2) {
		a[i+1] += a[i] / 10;
		a[i] %= 10;
	}
	s = "";
	forn(i, n * 2 - 1)
		s = s + (char)(a[i] + '0');
	while (s.length() < 110)
		s = '0' + s;
	ans.pb(s);
}

void gen(string s, int cur) {
	if (s.length() > 0 && s[0] != '0')
		add(s);
	if (cur + 2 > 9) return;
	if (s.length() > 55) return;
	for (int i = 0; cur + i * i * 2 <= 9; i++) {
		string t = (char)('0' + i) + s + (char)('0' + i);
		gen(t, cur + i * i * 2);
	}
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	gen("", 0);
	gen("0", 0);
	gen("1", 1);
	gen("2", 4);
	gen("3", 9);
	cerr << ans.size() << " " << clock() << endl;
	int tt;
	cin >> tt;
	forn(ii, tt) {
		printf("Case #%d: ", ii + 1);
		solve();
	}
	return 0;
}
