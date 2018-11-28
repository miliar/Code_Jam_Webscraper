#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        ll n, p;
        cin >> n >> p;
        if (p == (1LL << n)) {
            printf("Case #%d: %lld %lld\n", test, (1LL << n) - 1, (1LL << n) - 1);
            continue;
        }
        ll p1 = (1LL<<n) - p - 1;
        --p;
        vi v(n);
        for (int i = 0; i < n; ++i) if (p & (1LL << i)) {
            v[i] = 1;
        }
        int cnt1 = 0;
        for (int i = n-1; i >= 0; --i) {
            if (v[i] == 0)
                break;
            cnt1++;
        }
        int cnt0 = 0;
        v.assign(n, 0);
        for (int i = 0; i < n; ++i) if (p1 & (1LL << i)) {
            v[i] = 1;
        }
        for (int i = n-1; i >= 0; --i) {
            if (v[i] == 0)
                break;
            cnt0++;
        }
        printf("Case #%d: %lld %lld\n", test, (1LL << (cnt1+1)) - 2, (1LL << n) - (1LL << (1+cnt0)));
    }
    return 0;
}
