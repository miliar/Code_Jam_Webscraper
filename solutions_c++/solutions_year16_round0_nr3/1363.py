#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>

using namespace std;

#ifndef LOCAL
#define cerr if(0)cerr
#endif
#define pb push_back
#define mp make_pair

#define F first
#define S second
#define RT fprintf(stderr, "\nTIME = %lf\n", 1.0 * clock()/CLOCKS_PER_SEC);

typedef long long ll;
typedef long double ld;

const int INFint = 2147483547;
const ll INF = 9223372036854775807ll;
const ll MOD = 1000000007ll;

const ld EPS = 1e-9;

#define FILE "vacation"


ll f(ll x) {
    for (ll d = 2; d * d <= x; d++) {
        if (x % d == 0) return d;
    }
    return -1;
}

ll to_dec(vector<int> v, int base) {
    ll res = 0;
    for (int i = 0; i < v.size(); i++) {
        res *= base;
        res += v[i];
    }
    return res;
}


int main() {
    ios_base::sync_with_stdio(0);
#ifdef LOCAL
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
    //    freopen(FILE".in", "r", stdin); freopen(FILE".out", "w", stdout);
    //    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;
    for (int TT = 1; TT <= T; TT++) {
        int n, m;
        cin >> n >> m;
        n -= 2;
        printf("Case #%d:\n", TT);
        int all = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> cur;
            cur.pb(1);
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) cur.pb(1);
                else cur.pb(0);
            }
            cur.pb(1);
            reverse(cur.begin(), cur.end());
//            for (int i = 0; i < cur.size(); i++) cerr << cur[i];
//            cerr << endl;

            bool good = 1;
            vector<ll> ans;
            for (int base = 2; base < 11; base++) {
                ll a = to_dec(cur, base);
                ll dv = f(a);
//                cerr << base << ' ' << a << ' ' << dv << endl;
                if (dv == -1) {
                    good = 0;
                    break;
                }
                ans.pb(dv);
            }
            if (!good) continue;
            for (int i = 0; i < cur.size(); i++) {
                printf("%d", cur[i]);
            }
            printf(" ");
            for (int i = 0; i < ans.size(); i++) printf("%lld ", ans[i]);
            printf("\n");
            all++;
            if (all == m) break;
        }
    }
    
    
    RT;
    return 0;
}