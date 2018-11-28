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

int n, K;
vector<double> prob;
double dp[211][211][211];


double doit() {
    clr(dp, 0);
    dp[n][0][0] = 1.0;
    for (int k = 1; k <= K; ++k) {
        forn(yes, K + 1) {
            for (int i = n - 1; i >= 0; --i) {
                dp[i][k][yes] = max(
                    dp[i + 1][k][yes],
                    prob[i] * (yes ? dp[i + 1][k - 1][yes - 1] : 0.0) +
                        (1.0 - prob[i]) * dp[i + 1][k - 1][yes]
                );
            }
        }
    }
    return dp[0][K][K / 2];
}

double bf() {
    double p[211][211];
    double res = 0.0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (~mask & (1 << i)) continue;
            ++cnt;
        }
        if (cnt != K) continue;
        clr(p, 0);
        p[0][0] = 1.0;
        for (int i = 0, k = 1; i < n; ++i) {
            if (~mask & (1 << i)) continue;
            forn(j, K + 1)
                p[k][j] = prob[i] * (j ? p[k - 1][j - 1] : 0) + (1 - prob[i]) * p[k - 1][j];
            ++k;
        }
        res = max(res, p[K][K / 2]);
    }
    return res;
}

void solve() {
    cin >> n >> K;
    prob.resize(n);
    forn(i, n)
        cin >> prob[i];
    //printf("%.15lf\n", doit());
    printf("%.15lf\n", bf());
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
#define SMALL
//#define LARGE

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
