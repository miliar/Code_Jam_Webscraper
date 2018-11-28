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

struct rect {
	int x1, x2, y1, y2;
	rect() {}
	rect(int X1, int Y1, int X2, int Y2) {
		x1 = X1;
		y1 = Y1;
		x2 = X2;
		y2 = Y2;
	}
};

int w, h;
int n;
vector<rect> a;
int d[1050];
bool u[1050];

int dist(pii a, pii b) {
	return max(abs(a.fs - b.fs), abs(a.sc - b.sc)) - 1;
}

int dist(rect a, pii p) {
	int res = inf;
	res = min(res, dist(p, mp(a.x1, a.y1)));
	res = min(res, dist(p, mp(a.x1, a.y2)));
	res = min(res, dist(p, mp(a.x2, a.y1)));
	res = min(res, dist(p, mp(a.x2, a.y2)));
	if (a.x1 <= p.fs && p.fs <= a.x2) {
		res = min(res, abs(p.sc - a.y1) - 1);
		res = min(res, abs(p.sc - a.y2) - 1);
	}
	if (a.y1 <= p.sc && p.sc <= a.y2) {
		res = min(res, abs(p.fs - a.x1) - 1);
		res = min(res, abs(p.fs - a.x2) - 1);
	}
	res = max(res, 0);
	return res;
}

int dist(rect a, rect b) {
	int res = inf;
	res = min(res, dist(a, mp(b.x1, b.y1)));
	res = min(res, dist(a, mp(b.x1, b.y2)));
	res = min(res, dist(a, mp(b.x2, b.y1)));
	res = min(res, dist(a, mp(b.x2, b.y2)));
	swap(a, b);
	res = min(res, dist(a, mp(b.x1, b.y1)));
	res = min(res, dist(a, mp(b.x1, b.y2)));
	res = min(res, dist(a, mp(b.x2, b.y1)));
	res = min(res, dist(a, mp(b.x2, b.y2)));
	
//	cerr << a.x1 << " " << a.y1 << " " << a.x2 << " " << a.y2 << endl;
//	cerr << b.x1 << " " << b.y1 << " " << b.x2 << " " << b.y2 << endl;
//	cerr << res << endl;
//	cerr << endl;
	return res;
}

void solve() {
	cin >> w >> h >> n;
	a.clear();
	forn(i, n) {
		int x1, y1, x2, y2;
		cin >> x1  >> y1 >> x2 >> y2;
		a.pb(rect(x1, y1, x2, y2));
	}
	a.pb(rect(-1, 0, -1, h-1));
	a.pb(rect(w, 0, w, h-1));
        
        seta(u, 0);
        forn(i, n+2)
        	d[i] = inf;
	d[n] = 0;
	while (1) {
		int v = -1;
		forn(i, n+2)
			if (!u[i] && (v == -1 || d[v] > d[i]))
				v = i;
		if (v == -1) break;
		u[v] = 1;
		forn(i, n+2) {
			int ds = dist(a[v], a[i]);
			d[i] = min(d[i], ds + d[v]);
		}
	}
	cout << d[n+1] << endl;
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
