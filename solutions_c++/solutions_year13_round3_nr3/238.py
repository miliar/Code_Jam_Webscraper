#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <complex>
#include <deque>
#include <functional>
#include <list>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
using namespace std;
template<class T> inline T sqr(T x) { return x * x; }
template<class T> inline string tostr(const T & x) { stringstream ss; ss << x; return ss.str(); }
typedef long long lng;
typedef unsigned long long ulng;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef long double ld;
typedef pair<uchar, uchar> PII;
typedef pair<PII, uchar> PIII;
typedef pair<lng, lng> PLL;
typedef pair<lng, int> PLI;
typedef pair<ld, ld> PDD;
#define left asdleft
#define right asdright
#define link asdlink
#define unlink asdunlink
#define next asdnext
#define prev asdprev
#define y0 asdy0
#define y1 asdy1
#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define istr stringstream
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define X first
#define Y second
const double EPS = 1e-9;
const int INF = 1000*1000*1000;
const char CINF = 102;
const lng LINF = INF * 1ll * INF;
const ld PI = 3.1415926535897932384626433832795;
#define TASK "C"

struct wall {
	static const int MAX = 1000;
	//int h[MAX];
	vector<int> h;

	wall() {
		h.resize(MAX);
		//clr(h, 0);
	}

	bool hit(int i, int s) const {
		return h[i + MAX / 2] < s;
	}

	void build(int i, int s) {
		h[i + MAX / 2] = max(h[i + MAX / 2], s);
	}
};

struct tribe {
	int d, n, w, e, s, delta_d, delta_p, delta_s;

	void read() {
		cin >> d >> n >> w >> e >> s >> delta_d >> delta_p >> delta_s;
	}
};

struct attack {
	int d, w, e, s;

	attack() {}

	attack(const tribe & t, int day) {
		d = t.d + t.delta_d * day;
		w = t.w + t.delta_p * day;
		e = t.e + t.delta_p * day;
		s = t.s + t.delta_s * day;
	}

	bool operator < (const attack & o) const {
		return d < o.d;
	}

	bool success(const wall & wl) {
		for (int i = 2 * w; i <= 2 * e; ++i) {
			if (wl.hit(i, s))
				return true;
		}
		return false;
	}

	void build(wall & wl) {
		for (int i = 2 * w; i <= 2 * e; ++i) {
			wl.build(i, s);
		}
	}
};

int n;
tribe a[1 << 10];

void solve() {
	cin >> n;
	for (int i = 0; i < n; ++i)
		a[i].read();

	vector<attack> at;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < a[i].n; ++j) {
			//a[i].attack(j, w[a[i].d + i * a[i].delta_d]);
			at.pb(attack(a[i], j));
		}
	}
	sort(all(at));
	wall w, next_w;
	int res = 0;
	for (int i = 0; i < sz(at); ++i) {
		if (at[i].success(w))
			++res;
		at[i].build(next_w);
		if (i + 1 == sz(at) || at[i].d != at[i + 1].d) {
			w = next_w;
		}
	}
	cout << res << endl;
}

//#define DEBUG
#define SMALL
//#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int T;
	char buf[32];
	gets(buf);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
