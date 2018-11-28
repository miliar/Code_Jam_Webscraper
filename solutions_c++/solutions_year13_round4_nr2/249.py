// New Ryan
// Create @ 23:18 06-01 2013
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

int64 getW(int64 id, int n) {
    int64 bigger = id;
    int64 res = 0;
    rep (i, n) {
        if (bigger) {
            bigger = (bigger - 1) >> 1;
            res += (1LL << (n - i - 1));
        } else {
            break ;
        }
    }
    return res;
}

int64 getB(int64 id, int n) {
    int64 less = (1LL << n) - id - 1;
    int64 res = 0;
    rep (i, n) {
        if (less) {
            less = (less - 1) >> 1;
        } else {
            res += (1LL << (n - i - 1));
        }
    }
    return res;
}

int64 solveW(int n, int64 p) {
    int64 l = 0, r = (1LL << n) - 1;
    while (l <= r) {
        int64 mid = (l + r) >> 1;
        if (getW(mid, n) <= p) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return l - 1;
}

int64 solveB(int n, int64 p) {
    int64 l = 0, r = (1LL << n) - 1;
    while (l <= r) {
        int64 mid = (l + r) >> 1;
        if (getB(mid, n) <= p) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return l - 1;
}

int main() {
    wrte ("B.out");
    
    repcase {
        int n;
        int64 p;
        cin >> n >> p;
        --p;
        
        cout << "Case #" << Case++ << ": " <<
            solveW(n, p) << " " << solveB(n, p) << endl;
    }
    return 0;
}

