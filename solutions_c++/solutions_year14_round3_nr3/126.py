#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long lng;
typedef unsigned long long ulng;
typedef long double ld;
typedef pair<int, int> PII;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, PII> PIII;
typedef pair<lng, PII> PLII;
#define FAIL ++*(int*)0
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define RR 151
#define X first
#define Y second
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "C"

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int n, m, k;
int ans;

char a[20][20];
char used[20][20];
PII q[20*20];

inline bool ok(int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < m;
}

int get_enclosed() {
	int res = n * m;
	clr(used, 0);
	int l = 0, r = 0;
	for (int x = 0; x < n; ++x) {
		for (int y = 0; y < m; ++y) {
			if (a[x][y])
				continue;
			if (x == 0 || x == n - 1 || y == 0 || y == m - 1) {				
				used[x][y] = true;
				q[r++] = mp(x, y);
				--res;
			}
		}
	}
	while (l < r) {
		int x = q[l].X;
		int y = q[l].Y;
		++l;
		for (int i = 0; i < 4; ++i) {
			int tx = x + dx[i];
			int ty = y + dy[i];
			if (ok(tx, ty) && !used[tx][ty] && !a[tx][ty]) {
				used[tx][ty] = true;
				q[r++] = mp(tx, ty);
				--res;
			}
		}
	}
	return res;
}

void solve() {
	cin >> n >> m >> k;
	ans = INF;
	for (int mask = 0; mask < (1 << (n * m)); ++mask) {
		int put = 0;
		for (int i = 0; i < n * m; ++i) {
			int x = i / m;
			int y = i % m;
			a[x][y] = !!(mask & (1 << i));
			put += a[x][y];
		}		
		if (get_enclosed() >= k)
			ans = min(ans, put);
	}
	printf("%d\n", ans);
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
