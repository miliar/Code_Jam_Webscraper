#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = 3.14159265359;

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}



int main() {
    srand(time(NULL));
    //gen();
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        int n, k;
        cin >> n >> k;
        vector<int> a;
        for (int i = 0; i < n - k + 1; i++) {
            int x;
            cin >> x;
            a.pb(x);
        }

        vector<vector<pair<int,ll>>> g(n);

        for (int i = 1; i < n - k + 1; i++) {
            g[i - 1].pb(mp(i + k - 1, a[i] - a[i - 1]));
        }

        vector<pair<ll,ll>> rng;

        for (int i = 0; i < k; i++) {
            ll l = 0, r = 0;
            ll c = 0;
            int v = i;
            while (!g[v].empty()) {
                c += g[v][0].snd;
                l = min(l, c);
                r = max(r, c);
                v = g[v][0].fst;
            }
            rng.pb(mp(l, r));
        }

        ll need = a[0];

        auto check = [&](ll x) {
            for (auto p : rng) {
                if (p.snd - p.fst > x) {
                    return false;
                }
            }

            ll l = 0, r = 0;

            for (auto p : rng) {
                l += -p.fst;
                r += x - p.snd;
            }

            ll d = (need - l) / k;
            l += d * k;
            r += d * k;

            while (l + k <= need) {
                l += k;
                r += k;
            }

            while (r - k >= need && l > need) {
                l -= k;
                r -= k;
            }

            return l <= need && need <= r;
        };

        ll lo = -1, hi = 1e16;
        while (hi - lo > 1) {
            ll mid = (lo + hi) >> 1;

            if (check(mid)) {
                hi = mid;
            } else {
                lo = mid;
            }

        }


        printf("Case #%d: %lld\n", tt, hi);
    }

    return 0;
}