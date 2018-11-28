#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long       li;
typedef vector<li>      vi;
typedef complex<double> pt;
typedef pair<pt, pt>    line;
typedef pair<li, li>    pi;
typedef vector<string>  vs;

#define rep(i,to)       for(li i=0;i<((li)to);++i)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

template <class T> inline void minu(T& x, T y) { x = min(x, y); }
template <class T> inline void maxu(T& x, T y) { x = max(x, y); }
inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
    foreach(it, x) os << *it << ' ';
    return os;
}

li dx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li dy[8] = {0,  0, 1, -1, -1, 1, -1,  1};
const li maxn = 37;

double calc (li use, li m, const vector<li>& x, li b) {
    li tbets = 0, tcosts = 0;
    rep(i, use) {
        tbets += max(m - x[i], 0LL);
    }
    for (li i = use; i < maxn; ++i) {
        tcosts += max(m + 1 - x[i], 0LL);
    }
    tcosts += tbets;
    double ret = (tcosts <= b) ? double(tbets) / use * 36 - tcosts : -bit(60);
    // cerr << use << ' ' << m << ' ' << tbets << ' ' << tcosts << ' ' << ret << endl;
    return ret;
}

double findr(li use, const vector<li>& x, li b) {
    li l = 0, r = x[maxn-1] + b + 1;
    while (r - l > 1) {
        li m = (l + r) / 2;
        if (calc(use, m, x, b) < -bit(59)) {
            r = m;
        } else {
            l = m;
        }
    }
    return l;
} 

void solve() {

    li b, n;
    cin >> b >> n;
    vector<li> x(maxn, 0);
    rep (i, n) cin >> x[i];
    sort(all(x));

    double ans = 0;
    for (li use = 1; use < maxn; ++use) {
        double tans = 0;
        li l = 0, r = findr(use, x, b) + 1;
        // cerr << use << ' ' << l << ' ' << r << endl;
        while (r - l > 10) {
            li p = (l * 2 + r) / 3;
            li q = (l + r * 2) / 3;
            if (calc(use, p, x, b) <= calc(use, q, x, b)) {
                l = p;
            } else {
                r = q;
            }
        }
        // cerr << use << ' ' << l << ' ' << r << endl;
        for (li m = l; m < r; ++m) tans = max(tans, calc(use, m, x, b));

        ans = max(ans, tans);
    }

    static int casenum = 1;
    printf("Case #%d: %.9f\n", casenum++, ans);
    // cout << "Case #" << casenum++ << ": " << ans << endl;
    return;
}

int main() {
    int n;
    cin >> n;
    cout.precision(15);
    while (n--) solve();

    return 0;
}
