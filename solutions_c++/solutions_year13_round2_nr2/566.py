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
//#include <ctime>
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
typedef pair<int, int> PII;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "B"
#define RR 151
#define X first
#define Y second

int dx[] = {-1, 1};

const int INF = 1000*1000*1000;
const int SH = 40;
const int MAXX = 100;
const int MAXY = 41;

int n;
char used[MAXX][MAXY];
double ans[MAXX][MAXY];

void solve () {
	cin >> n;
	memset(ans, 0, sizeof ans);
	//int maxy = 2;
	for (int mask = 0; mask < (1 << (n - 1)); ++mask) {
		memset(used, 0, sizeof used);
		used[0 + SH][0] = true;
		ans[0 + SH][0] += 1.0;
		for (int i = 0; i < n - 1; ++i) {
			int bit = (mask >> i) & 1;
			int y = 40;
			for (; y >= 2 && !used[0 + SH][y]; y -= 2) ;
			y += 2;
			int x = 0;
			for (; y > 0; --y) {
				if (!used[x + SH + dx[bit]][y - 1])
					x += dx[bit];
				else if (!used[x + SH + dx[!bit]][y - 1])
					x += dx[!bit];
				else
					break;
			}
			used[x + SH][y] = true;
			ans[x + SH][y] += 1.0;
		}
	}
	int x, y;
	cin >> x >> y;
	if (0 <= x + SH && x + SH < MAXX && y < MAXY)
		printf("%.15lf\n", ans[x + SH][y] / (1 << (n - 1)));
	else
		puts("0");
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
