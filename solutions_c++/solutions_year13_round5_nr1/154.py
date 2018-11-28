// New Ryan
// Create @ 21:59 06-15 2013
// Comment - 

#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <map>
#include <set>
#include <cassert>

using namespace std;

// Self Template Code BGEIN

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define all(x) (x).begin(), (x).end()
#define clz(x) memset (x, 0, sizeof(x))
#define read(x) freopen (x, "r", stdin)
#define wrte(x) freopen (x, "w", stdout)
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<double, double> pdd;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

int n;
int64 B, p[38];

bool check(int64 need, int X, bool debug = false) {
    int64 res = 0;
    rep (i, X) {
        if (p[i] > need) {
            return false;
        }
        res += need - p[i];
    }
    repf (i, X, 36) {
        res += max(0LL, need + 1 - p[i]);
    }
    //if (debug) printf ("res %I64d\n", res);
    return res <= B;
}

int64 cal(int64 need, int X) {
    int64 canB = 0;
    rep (i, X) {
        if (p[i] > need) {
            return 0;
        }
        canB += need - p[i];
    }
    int64 put = 0;
    repf (i, X, 36) {
        put += max(0LL, need + 1 - p[i]);
    }
    return canB * 36 - (canB + put) * X;
}

double solve(int X) {
    int64 l = p[X - 1] - 1, r = (1LL << 58);
    while (l <= r) {
        int64 mid = (l + r) >> 1;
        //printf ("mid %I64d\n", mid);
        if (check(mid, X)) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    if (l == p[X - 1] - 1) {
        return 0;
    }
    //printf ("try %d with %I64d\n", X, l - 1);
    int64 max_goal = l - 1;
    //check(goal, X, true);
    //int64 canB = 0;
    //int64 put = 0;
    //rep (i, X) {
        //canB += goal - p[i];
    //}
    //repf (i, X, 34) {
        //put += max(0LL, goal + 1 - p[i]);
    //}
    l = p[X - 1] - 1; r = max_goal + 1;
    int64 ans = 0;
    while (l <= r) {
        int64 mid1 = (l * 2 + r) / 3;
        int64 mid2 = (l + r * 2) / 3;
        int64 p1 = cal(mid1, X);
        int64 p2 = cal(mid2, X);
        ckmax(ans, p1); ckmax(ans, p2);
        if (p1 >= p2) {
            r = mid2 - 1;
        } else {
            l = mid1 + 1;
        }
    }
    //printf ("here %lf\n", (double)ans / X);
    return (double)ans / X;
}

int main() {
    wrte ("A.out");
    
    repcase {
        fprintf (stderr, "Solve Case %d ...\n", Case);
        
        scanf ("%I64d%d", &B, &n);
        rep (i, n) {
            scanf ("%I64d", &p[i]);
        }
        
        repf (i, n, 36) {
            p[i] = 0;
        }
        sort (p, p + 37);
        
        double ans = 0.0;
        repf (i, 1, 36) {
            ckmax(ans, solve(i));
        }
        //solve(35);
        
        printf ("Case #%d: %.9lf\n", Case++, ans);
    }
    return 0;
}

