#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

const int MOD = 1000002013;


int Cost(int n, int diff, LL cnt) {
    LL ans = ((LL)(n - diff + 1 + n) * diff / 2) % MOD;
    return ans * (cnt % MOD) % MOD;
}

int Solve() {
    int n, m;
    cin >> n >> m;
    

    set<int> bounds;
    bounds.insert(1);
    bounds.insert(n + 1);

    LL defCost = 0;

    vector< vector<int> > v;
    for (int i = 0; i < m; ++i) {
        vector<int> w;
        int a, b, cnt;
        cin >> a >> b >> cnt;
        
        defCost += Cost(n, b - a, cnt);
        defCost %= MOD;

        w.push_back(a);
        w.push_back(b);
        w.push_back(cnt);
        v.push_back(w);

        bounds.insert(a);
        bounds.insert(b);
    }

    vector<int> vb(bounds.begin(), bounds.end());
    vector<LL> pc(vb.size());

    for (int i = 0; i < m; ++i) {
        int a = v[i][0], b = v[i][1], cnt = v[i][2];
        for (size_t j = 0; j < vb.size(); ++j) {
            if (a <= vb[j] && vb[j] < b) {
                pc[j] += cnt;
            }
        }
    }


    LL newCost = 0;

    for (;;) {
        LL mx = *max_element(pc.begin(), pc.end());
        if (mx == 0) {
            break;
        }
        size_t p1 = 0, p2 = 0;

        while (p1 < pc.size()) {
            p2 = p1 + 1;
            while (p2 < pc.size() && pc[p1] == pc[p2]) {
                ++p2;
            }
            if (pc[p1] == mx) {
                LL leave = 0;
                if (p1 > 0) {
                    leave = max(leave, pc[p1 - 1]);
                }
                if (p2 < pc.size()) {
                    leave = max(leave, pc[p2]);
                }
                assert(mx > leave);
                LL delta = mx - leave;

                newCost += Cost(n, vb[p2] - vb[p1], delta);
                newCost %= MOD;

                for (int k = p1; k < p2; ++k) {
                    pc[k] = leave;
                }
            }
            p1 = p2;
        }
    }
    return (defCost - newCost + MOD) % MOD;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int nTests;
    cin >> nTests;

    for (int test = 0; test < nTests; ++test) {
        int ans = Solve();
        cout << "Case #" << test + 1 << ": " << ans << '\n';
    }

    return 0;
}
