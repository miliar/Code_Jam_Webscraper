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
typedef pair<int, int> PII;
typedef pair<lng, int> PLI;
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

#define TASK "A"

int a[2];
int b[2][4][4];

void solve() {
	for (int i = 0; i < 2; ++i) {
		cin >> a[i];
		--a[i];
		for (int x = 0; x < 4; ++x) {
			for (int y = 0; y < 4; ++y) {
				cin >> b[i][x][y];
				--b[i][x][y];
			}
		}
	}
	int ms[2] = {0};
	for (int i = 0; i < 2; ++i) {
		int x = a[i];
		for (int y = 0; y < 4; ++y)
			ms[i] |= 1 << b[i][x][y];
	}
	int mask = ms[0] & ms[1];
	if (mask == 0)
		puts("Volunteer cheated!");
	else if ((mask & (mask - 1)) == 0) {
		int res = 0;
		for (; mask; mask >>= 1)
			++res;
		printf("%d\n", res);
	} else {
		puts("Bad magician!");
	}
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
