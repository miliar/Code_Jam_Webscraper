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

int n, m;
vector<string> s, q;
int sum[1<<8];
int t[5][1<<8];
int w[5][1<<8];

int lcp(string a, string b) {
	int res = 0;
	forn(i, min(a.length(), b.length())) {
		if (a[i] != b[i])
			return i;
		else res++;
	}
	return res;
}

int calcs(int mask) {
	int v = 1;
	q.clear();
	forn(i, n)
		if (mask & (1 << i)) {
			int x = 0;
			forn(j, q.size())
				x = max(x, lcp(s[i], q[j]));
			v += s[i].length() - x;
			q.pb(s[i]);
		}	
	return v;
}

void solve() {
	cin >> n >> m;
	s.resize(n);
	forn(i, n)
		cin >> s[i];
	forn(i, 1 << n)
		sum[i] = calcs(i);
	seta(t, 0);
	for(int i = 1; i <= m; i++)
		forn (j, 1 << n) {
			t[i][j] = 0;
			forn(k, 1 << n)
				if ((j & k) == k && k)
					t[i][j] = max(t[i][j], t[i-1][j^k] + sum[k]);
		}
	seta(w, 0);
	w[0][0] = 1;
	for(int i = 1; i <= m; i++)
		forn (j, 1 << n) {
			forn(k, 1 << n)
				if ((j & k) == k && t[i][j] == (t[i-1][j^k] + sum[k]) && k)
					w[i][j] += w[i-1][j^k];
		}
	cout << t[m][(1<<n)-1] << " " << w[m][(1<<n)-1] << endl;
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn(ii, tt) {
		printf("Case #%d: ", ii + 1);
		solve();
	}	
	return 0;
}
