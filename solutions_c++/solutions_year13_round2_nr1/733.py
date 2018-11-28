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
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<lng, lng> pii64;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
//typedef complex<double> point;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "A"
#define RR 151

const int INF = 1000*1000*1000;

const int MAX = 1000;

int A;
int n;
int a[100];
int d[100][MAX + 1];

int rec(int x, int w) {
	if (x == n) return 0;
	int & res = d[x][w];
	if (res != -1)
		return res;
	res = INF;
	if (a[x] < w)
		res = rec(x + 1, min(MAX, w + a[x]));
	else {
		res = min(rec(x + 1, w), rec(x, min(MAX, 2 * w - 1))) + 1;
	}
	return res;
}

void solve () {
	cin >> A >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	sort(a, a + n);
	memset(d, -1, sizeof d);
	printf("%d\n", rec(0, A));
}

//#define DEBUG
#define SMALL
//#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt2.in", "r", stdin);
    freopen(TASK "-small-attempt2.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large-1.in", "r", stdin);
    freopen(TASK "-large-1.out", "w", stdout);
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
