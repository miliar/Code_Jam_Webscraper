// Rain Dreamer MODEL
// Create @ 20:38 04-12 2014
// Comment - 

#include <cmath>
#include <ctime>
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
#define RD(x) freopen (x, "r", stdin)
#define WT(x) freopen (x, "w", stdout)
#define clz(x) memset (x, 0, sizeof(x))
#define cln(x) memset (x, -1, sizeof(x))
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

const int MAXN = 1000 + 10;

double a[MAXN], b[MAXN];
bool used[MAXN];
int n;

int solve_fair() {
    clz (used);
    int ans = 0;
    rep (i, n) {
        int ch = -1;
        rep (j, n) if (!used[j]) {
            ch = (ch == -1? j : ch);
            if (sgn(b[j] - a[i]) > 0) {
                ch = j;
                break ;
            }
        }
        used[ch] = true;
        if (sgn(b[ch] - a[i]) < 0) {
            ans += 1;
        }
    }
    return ans;
}

int solve_opt() {
    repf (off, 0, n - 1) {
        bool over_all = true;
        rep (i, n - off) if (sgn(a[i + off] - b[i]) < 0) {
            over_all = false;
            break ;
        }
        if (over_all) {
            return n - off;
        }
    }
    
    return 0;
}

int main() {
    WT ("D.ans");
    
    repcase {
        scanf ("%d", &n);
        rep (i, n) scanf ("%lf", &a[i]);
        rep (i, n) scanf ("%lf", &b[i]);
        
        sort (a, a + n);
        sort (b, b + n);
        
        printf ("Case #%d: %d %d\n", Case++, solve_opt(), solve_fair());
    }
    return 0;
}

