// Rain Dreamer MODEL
// Create @ 22:10 05-31 2014
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

const int maxn = 1010;

int n, a[maxn], b[maxn], c[maxn], d[maxn];
map<int, int> mp;

struct BIT {
    
#define lowbit(x) ((x) & (-(x)))
    
    int a[maxn];
    
    void clear() {
        clz (a);
    }
    void update (int x) {
        for (; x < maxn; x += lowbit(x)) {
            a[x] ++;
        }
    }
    int getsum (int x) {
        int res = 0;
        for (; x; x -= lowbit(x)) {
            res += a[x];
        }
        return res;
    }
};

BIT bit;

int solve() {
    mp.clear();
    
    rep (i, n) b[i] = a[i];
    sort (b, b + n);
    rep (i, n) mp[b[i]] = i + 1;
    rep (i, n) a[i] = mp[a[i]];
    
    bit.clear();
    rep (i, n) {
        c[i] = i - bit.getsum(a[i] - 1);
        bit.update (a[i]);
    }
    bit.clear();
    repd (i, n - 1, 0) {
        d[i] = n - 1 - i - bit.getsum(a[i] - 1);
        bit.update (a[i]);
    }
    int ans = 0;
    rep (i, n) {
        ans += min(c[i], d[i]);
        //printf ("%d %d\n", c[i], d[i]);
    }
    //int res = ans;
    //repd (i, n - 1, 0) {
        //ans += d[i] - c[i];
        //ckmin (res, ans);
    //}
    return ans;
}

int main() {
    WT ("B3.out");
    
    repcase {
        scanf ("%d", &n);
        rep (i, n) scanf ("%d", a + i);
        printf ("Case #%d: %d\n", Case++, solve());
    }
    return 0;
}

