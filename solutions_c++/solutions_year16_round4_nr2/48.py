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

using R = double;

R calc(int K, vector<R> v) {
    assert(2*K == (int)v.size());
    R dp1[2*K+1];
    fill_n(dp1, 2*K+1, 0);
    dp1[0] = 1;
    R dp2[2*K+1];
    for (int i = 0; i < 2*K; i++) {
        R p = v[i];
        for (int j = 0; j <= 2*K; j++) {
            dp2[j] = dp1[j-1]*p+dp1[j]*(1-p);
        }
        copy_n(dp2, 2*K+1, dp1);
    }
    return dp1[K];
}
void solve() {
    int n, k;
    cin >> n >> k; k/=2;
    R p[n];
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    R ma = 0;
    sort(p, p+n);
    for (int i = 0; i <= 2*k; i++) {
        vector<R> v;
        for (int j = 0; j < i; j++) {
            v.push_back(p[j]);
        }
        for (int j = 0; j < 2*k-i; j++) {
            v.push_back(p[n-1-j]);
        }
        ma = max(ma, calc(k, v));
    }

    printf("%.20lf\n", ma);
}
int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}