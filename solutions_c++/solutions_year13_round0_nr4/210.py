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
#define TASK "D"
#define RR 151

int n;
char d[1 << 20];
char p[1 << 20];
int keys[256];
int opens_with[20];
vector< vector<int> > in;

char rec(int mask) {
    if (mask == (1 << n) - 1)
        return true;
    char & res = d[mask];
    if (res != -1)
        return res;
    res = 0;
    for (int i = 0; i < n; ++i) {
        if (mask & (1 << i))
            continue;
        int key = opens_with[i];
        if (keys[key] == 0)
            continue;
        --keys[key];
        for (int j = 0; j < sz(in[i]); ++j) {
            ++keys[in[i][j]];
        }
        if (rec(mask | (1 << i))) {
            p[mask] = i;
            return res = true;
        }
        for (int j = 0; j < sz(in[i]); ++j) {
            --keys[in[i][j]];
        }
        ++keys[key];
    }
    return res;
}

void solve () {
    memset(keys, 0, sizeof keys);
    int k;
    cin >> k >> n;
    for (int x; k--; ) {
        cin >> x;
        --x;
        ++keys[x];
    }
    in.clear();
    in.resize(n);
    for (int i = 0; i < n; ++i) {
        int t;
        cin >> opens_with[i] >> t;
        --opens_with[i];
        in[i].resize(t);
        for (int j = 0; j < t; ++j) {
            cin >> in[i][j];
            --in[i][j];
        }
    }
    memset(d, -1, sizeof d);
    if (!rec(0)) {
        puts("IMPOSSIBLE");
    } else {
        for (int i = 0, mask = 0; i < n; ++i) {
            printf("%d ", p[mask] + 1);
            mask |= 1 << p[mask];
        }
        puts("");
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
