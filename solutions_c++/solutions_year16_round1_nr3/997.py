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

typedef unsigned uint;
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


bool check(const vector<int> &f, vector<int> a) {
    if (sz(a) == 1) {
        return true;
    }
    sort(all(a));
    do {
        bool ok = true;
        for (int i = 0; i < sz(a); ++i) {
            bool any = false;
            any |= f[a[i]] == a[(i + 1) % sz(a)];
            any |= f[a[i]] == a[(i - 1 + sz(a)) % sz(a)];
            ok &= any;
        }
        if (ok) return true;
    } while (next_permutation(all(a)));
    return false;
}

void solve() {
    int n;
    cin >> n;
    vector<int> f(n);
    for (int i = 0; i < n; ++i) {
        cin >> f[i];
        --f[i];
    }
    int res = 0;
    for (int mask = 1; mask < (1 << n); ++mask) {
        vector<int> a;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                a.push_back(i);
            }
        }
        if (check(f, a)) {
            res = max(res, sz(a));
        }
    }
    cout << res << endl;
}

void stress() {
    for (int n = 2; n <= 50; ++n) {
        cerr << n << endl;
    }
    cerr << "PASSED" << endl;
}

//#define DEBUG
#define SMALL
//#define LARGE

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif

	//stress();

	int T;
	char buf[32];
    fgets(buf, sizeof buf, stdin);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
