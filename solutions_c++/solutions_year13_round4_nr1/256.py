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

#define rep(i,to)       for(li i=0;i<((li)to);i++)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
    foreach(it, x) os << *it << ' ';
    return os;
}
template <class T> inline void dbg(T x){
    // return;
    cerr << x << endl; 
}

li dx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li dy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

const li mod = 1000002013;

struct passenger {
    li o, e, p;
    li d() { return e - o; }
};

li fee(li d, li n) {
    return (n * d - d * (d - 1) / 2) % mod;
}

void solve() {

    li n, m;
    cin >> n >> m;
    vector<passenger> ps(m);
    rep (i, m) cin >> ps[i].o >> ps[i].e >> ps[i].p;

    li orig = 0;
    map<li, li> event;
    rep (i, m) {
        orig = (orig + fee(ps[i].d(), n) * ps[i].p) % mod;
        event[ps[i].o] += ps[i].p;
        event[ps[i].e] -= ps[i].p;
    }

    stack<pair<li, li> > s;
    li opt = 0;
    foreach(it, event) {
        li pos = it->first;
        li cnt = it->second;
        // cerr << pos << " " << cnt << endl;
        if (cnt == 0) continue;
        if (cnt > 0) {
            s.push(make_pair(pos, cnt));
        } else {
            cnt *= -1;
            while (cnt > 0) {
                if (s.empty()) {
                    cerr << "something wrong!" << endl;
                    return;
                }
                li use = min(cnt, s.top().second);
                s.top().second -= use;
                cnt -= use;
                opt = (opt + fee(pos - s.top().first, n) * use) % mod;
                if (s.top().second == 0) s.pop();
            }
        }
    }
    // cerr << orig << " " << opt << endl;
    li ans = (orig - opt + mod) % mod;
    static int casenum = 1;
    cerr << casenum << " " << ans << endl;
    cout << "Case #" << casenum++ << ": " << ans << endl;

    return;
}

int main() {
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
