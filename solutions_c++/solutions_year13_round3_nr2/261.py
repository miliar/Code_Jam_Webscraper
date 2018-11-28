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
#define TASK "B"

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
const string dir = "WNES";

const int MAX = 250;
uchar dist[MAX][MAX][MAX];
uchar p[MAX][MAX][MAX];
const int SH = MAX / 2;

inline bool ok(int x, int y) {
	return x >= 0 && y >= 0 && x < MAX && y < MAX;
}

void bfs(int x, int y) {
	clr(dist, -1);
	dist[x][y][0] = 0;
	static PIII q[MAX * MAX * MAX];
	int l = 0, r = 0;
	q[r++] = mp(mp(x, y), 0);
	while (l < r) {
		int x = q[l].X.X;
		int y = q[l].X.Y;
		int d = q[l].Y;
		++l;
		for (int i = 0; i < 4; ++i) {
			int tx = x + dx[i] * (d + 1);
			int ty = y + dy[i] * (d + 1);
			if (ok(tx, ty) && d + 1 < MAX && dist[tx][ty][d + 1] == 255) {
				dist[tx][ty][d + 1] = dist[x][y][d] + 1;
				p[tx][ty][d + 1] = i;
				q[r++] = mp(mp(tx, ty), d + 1);
			}
		}
	}
}

inline bool pred(uchar x) {
	return x == 255;
}

void solve () {
	int x, y;
	cin >> x >> y;
	x += SH, y += SH;
	int d = *find_if_not(dist[x][y], dist[x][y] + MAX, pred);
	string path = "";
	for (int i = x, j = y; d > 0; --d) {
		int k = p[i][j][d];
		path += dir[k];
		i -= dx[k] * d;
		j -= dy[k] * d;
	}
	reverse(all(path));
	cout << path << endl;
}

void precalc() {
	bfs(SH, SH);
	return;
	for (int i = 0; i < MAX; ++i)
		for (int j = 0; j < MAX; ++j)
			printf("%d%c", *find_if_not(dist[i][j], dist[i][j] + MAX, pred), " \n"[j == MAX - 1]);
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

	precalc();

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
