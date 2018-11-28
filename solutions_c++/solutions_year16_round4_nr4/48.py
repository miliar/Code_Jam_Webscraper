#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>

using namespace std;
using ll = long long;
using ull = unsigned long long;
constexpr int TEN(int n) {return (n==0)?1:10*TEN(n-1);}

const int MN = 25;
using P = array<int, 2>;
struct Solve {
    int coun[2];
    bool used[2][MN] = {};
    vector<int> g[2][MN];
    void dfs(int side, int p) {
        if (used[side][p]) return;
        used[side][p] = true;
        coun[side]++;
        for (int d: g[side][p]) {
            dfs(1-side, d);
        }
    }
    vector<P> v;
    int vc;
    using Q = tuple<int, int, int>;
    map<Q, int> dp;
    int calc(int mp, int lc, int rc) {
        if (lc < 0 or rc < 0) return 10000;
        if (!mp) {
            assert(lc == rc);
            return lc;
        }
        if (dp.count(Q(mp, lc, rc))) return dp[Q(mp, lc, rc)];
        int ans = 10000;
        if (lc and rc) ans = min(ans, 1+calc(mp, lc-1, rc-1));
        for (int f = 1; f < (1<<vc); f++) {
            if (~mp & f) continue;
            int a = 0, b = 0;
            for (int i = 0; i < vc; i++) {
                if (!(f & (1<<i))) continue;
                a += v[i][0]; b += v[i][1];
            }
            int co = max(a,b)*max(a,b);
            if (a < b) {
                ans = min(ans, co+calc(mp ^ f, lc-(b-a), rc));
            } else {
                ans = min(ans, co+calc(mp ^ f, lc, rc-(a-b)));
            }
        }
        return dp[Q(mp, lc, rc)] = ans;
    }
    void solve() {
        int n;
        cin >> n;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            string s; cin >> s;
            for (int j = 0; j < n; j++) {
                if (s[j] == '1') {
                    g[0][i].push_back(j);
                    g[1][j].push_back(i);
                    ans--;
                }
            }
        }
        int lc = 0, rc = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                if (used[i][j]) continue;
                coun[0] = coun[1] = 0;
                dfs(i, j);
                if (coun[0] == 1 and coun[1] == 0) lc++;
                if (coun[0] == 0 and coun[1] == 1) rc++;
                if (coun[0] == coun[1]) {
                    ans += coun[0]*coun[1];
                    continue;
                }
                if (coun[0] and coun[1]) v.push_back(P{coun[0], coun[1]});
            }
        }
        vc = (int)v.size();
        printf("%d\n", ans + calc((1<<vc)-1, lc, rc));
    }
};

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        Solve s;
        s.solve();
    }
    return 0;
}