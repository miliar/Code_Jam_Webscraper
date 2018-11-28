#ifdef NALP_PROJECT
#pragma hdrstop
#else
#define _SECURE_SCL 0
#endif

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <memory.h>

#include <iostream>
#include <fstream>
#include <sstream>

#ifdef _WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define y1 YYY1
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> inline T Abs(T x) { return (x >= 0) ? x : -x; }
template<typename T> inline T sqr(T x) { return x * x; }
template<typename T> inline string toStr(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int bit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline int64 nextInt64() { int64 x; if (scanf(LLD, &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;

const int MAXN = 1100;

int n, W, H, x1[MAXN], y1[MAXN], x2[MAXN], y2[MAXN];
int g[MAXN][MAXN], d[MAXN];
bool used[MAXN];
queue<int> q;

bool intersect(int a1, int b1, int a2, int b2) {
	return max(a1, a2) <= min(b1, b2);
}

void update(int v, int value) {
	if (d[v] > value) {
		if (!used[v]) q.push(v);
		used[v] = true;
		d[v] = value;
	}
}

int dijkstra2(int start, int finish) {
	memset(d, 60, sizeof d);
	memset(used, 0, sizeof used);
	update(start, 0);
	while (!q.empty()) {
		int v = q.front(); q.pop();
		used[v] = false;
		forn(u, n) {
			update(u, d[v] + g[v][u]);
		}
	}

	return d[finish];
}

int dijkstra(int start, int finish) {
	memset(d, 60, sizeof d);
	memset(used, 0, sizeof used);
	d[start] = 0;
	forn(step, n) {
		int v = -1, dist = INF;
		forn(i, n) {
			if (!used[i] && dist > d[i]) {
				dist = d[i];
				v = i;
			}
		}

		used[v] = true;
		forn(u, n) {
			d[u] = min(d[u], d[v] + g[v][u]);
		}
	}

	return d[finish];
}

int stupid() {
	forn(k, n) {
		forn(i, n) {
			forn(j, n) {
				g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
			}
		}
	}

	return g[n - 1][n - 2];
}

void solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
		W = nextInt();
		H = nextInt();
		n = nextInt();
		forn(i, n) {
			x1[i] = nextInt();
			y1[i] = nextInt();
			x2[i] = nextInt() + 1;
			y2[i] = nextInt() + 1;
		}
        // read test.
        if (skipThisTest) return;
    } else {
        cerr << "\tinput mode: generated test." << endl;
        // generate test.
    }

    x1[n] = 0; x2[n] = 0; y1[n] = 0; y2[n] = INF; n++;
    x1[n] = W; x2[n] = W; y1[n] = 0; y2[n] = INF; n++;
	forn(i, n) {
		g[i][i] = 0;
		forn(j, i) {
			int cx = max(x1[i] - x2[j], x1[j] - x2[i]);
			int cy = max(y1[i] - y2[j], y1[j] - y2[i]);
			if (intersect(y1[i], y2[i], y1[j], y2[j])) {
				cy = -INF;
			}
			if (intersect(x1[i], x2[i], x1[j], x2[j])) {
				cx = -INF;
			}

			if (cx < 0 && cy < 0) cx = cy = 0;
			g[i][j] = g[j][i] = max(cx, cy);
		}
	}

	int ans = dijkstra(n - 1, n - 2);
	cout << ans << endl;
    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (n <= 100) {
        int stupidAnswer = stupid();
        cerr << "\tstupid answer is '" << stupidAnswer << "'." << endl;
        assert(ans == stupidAnswer);
    }
}

int main(int argc, char * argv[]) {
#ifdef NALP_PROJECT
    freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#else
#endif

    int minTest = 1, maxTest = INF;
    if (argc == 3) {
        minTest = atoi(argv[1]);
        maxTest = atoi(argv[2]);
    }

    cout.precision(10);
    cout.setf(ios::fixed);

    cerr.precision(10);
    cerr.setf(ios::fixed);

    srand((unsigned int)time(0));
    int tests = nextInt();
    clock_t totalStartTime = clock();
    for(int test = 1; test <= tests; test++) {
        clock_t startTime = clock();
        cerr << "Case #" << test << endl;
        bool skipThisTest = (test < minTest || test > maxTest);
        if (!skipThisTest) cout << "Case #" << test << ": ";
        solve(skipThisTest);

        char formattedTime[100];
        clock_t time = clock() - startTime;
        sprintf(formattedTime, "%d.%03d", int(time / CLOCKS_PER_SEC), int(time % CLOCKS_PER_SEC));
        cerr << "time for test is " << formattedTime << " s." << endl << endl;
    }

    char formattedTime[100];
    clock_t totalTime = clock() - totalStartTime;
    sprintf(formattedTime, "%d.%03d", int(totalTime / CLOCKS_PER_SEC), int(totalTime % CLOCKS_PER_SEC));
    cerr << string(20, '=') << endl;
    cerr << "TOTAL TIME IS " << formattedTime << " s." << endl;

    return 0;
}
