#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int p,q,n;
        cin >> p >> q >> n;
        vi h(n), g(n);
        for (int i = 0; i < n; ++i) cin >> h[i] >> g[i];
/*        if (test == 48) {
            cerr << p << ' ' << q << ' ' << n << endl;
            out(h); out(g);
        }*/
        vi d(20*n + 100000, -1);
        int zero = d.size()/2;
        d[zero] = 0;
        for (int i = 0; i < n; ++i) {
            vi nd(d.size(), -1);
            for (int k = 0; k < d.size(); ++k) if (d[k] >= 0) {
                int cnt_wait = (h[i]+q-1)/q;
                int t = k - zero;
//                cerr << i << ' ' << t << ' ' << d[k] << ' ' << cnt_wait << endl;
                nd[cnt_wait+k] = max(nd[cnt_wait+k], d[k]);
                if (-t*q >= h[i]) continue;
                t += cnt_wait-1;
                int rem = h[i] - q*(cnt_wait-1);
                if (rem <= (t + 1)*p) {
                    int cnt = (rem + p-1) / p;
                    int ind = zero + t - cnt;
                    nd[ind] = max(nd[ind], d[k] + g[i]);
                }
            }
            d.swap(nd);
        }
        int ma = 0;
        for (int i = zero-1; i < d.size(); ++i) {
            ma = max(ma, d[i]);
        }
        cout << ma << endl;
    }
    return 0;
}
