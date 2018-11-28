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
        ll n,p,q,r,s;
        cin >> n >> p >> q >> r >> s;
        vl v(n), sum(n+1);
        for (int i = 0; i < n; ++i) {
            v[i] = s + (i*p+q)%r;
            sum[i+1] = sum[i] + v[i];
        }
        ll best = sum.back();
        for (int r = 0; r < n; ++r) {
            ll cur = sum[r+1];
            int it = lower_bound(sum.begin(), sum.end(), sum[r+1] / 2) - sum.begin();
            for (int l = max(0, it - 4); l <= r && l <= it + 4; ++l) {
                cur = min(cur, max(sum[l], sum[r+1] - sum[l]));
            }
            best = min(best, max(cur, sum.back() - sum[r+1]));
        }
        printf("%.10lf\n", (sum.back() - best) / (double)sum.back());
    }
    return 0;
}
