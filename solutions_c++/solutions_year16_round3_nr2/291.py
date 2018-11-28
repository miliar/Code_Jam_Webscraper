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
typedef pair<int, int> pii;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, pii> PIII;
typedef pair<lng, pii> PLII;
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
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "B"

vector<string> doit(int n, lng m) {
    vector<string> res(n, string(n, '0'));
    forn(i, n - 1) {
        forn(j, i)
            res[j][i] = '1';
    }
    if (m == 1LL << (n - 2)) {
        forn(j, n-1)
            res[j][n-1] = '1';
    } else {
        forn(i, n-2) {
            if (m & (1LL << i)) {
                res[i + 1][n - 1] = '1';
                m -= 1LL << i;
            }
        }
        if (m) res.clear();
    }
    return res;
}

void solve() {
    int n;
    lng m;
    cin >> n >> m;
    auto res = doit(n, m);
    if (res.empty())
        puts("IMPOSSIBLE");
    else {
        puts("POSSIBLE");
        for (auto x : res) puts(x.c_str());
    }
}


//void stress() {
//    for (int n = 3; n <= 10; ++n) {
//        for (int t = 0; t < 1000; ++t) {
//            if (ans != res) {
//                cerr << "FAIL" << endl;
//                cerr << "NEED: " << ans << endl;
//                cerr << "HAVE: " << res << endl;
//                exit(66);
//            }
//        }
//    }
//    cerr << "PASSED" << endl;
//}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
#ifdef SMALL                                   
    freopen(TASK "-small-attempt1.in", "r", stdin);
    freopen(TASK "-small-attempt1.out", "w", stdout);
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
