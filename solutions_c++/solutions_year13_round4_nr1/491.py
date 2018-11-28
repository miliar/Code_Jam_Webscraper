#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

int64 mod = 1000002013;

void solve() {
    int64 n, m;
    cin >> n >> m;
    map<int64, int64> a_in;
    map<int64, int64> a_out;
    int64 ans = 0;
    for (int64 i = 0; i < m; ++i) {
        int64 x, y, z;
        cin >> x >> y >> z;
        a_in[x] += z;
        a_in[y] += 0;
        a_out[x] += 0;
        a_out[y] += z;
        int64 l = y - x;
        int64 mul = l * (l - 1) / 2;
        mul %= mod;
        mul *= z;
        mul %= mod;
        ans -= mul;
        ans %= mod;
        ans += mod;
        ans %= mod;
    }
    map<int64, int64> a;
    int64 prev = 0;
    bool ok = false;
    for (map<int64, int64>::iterator it = a_in.begin(); it != a_in.end(); ++it) {
        int64 add = 0;
        if (ok)
            add = it->first - prev;
        ok = true;
        prev = it->first;
        map<int64, int64> b;
        for (map<int64, int64>::iterator it1 = a.begin(); it1 != a.end(); ++it1)
            b[it1->first + add] = it1->second;
        a = b;
        a[0] += it->second;
        a[0] %= mod;
        int64 x = a_out[it->first];
        while (x > 0) {
           map<int64, int64>::iterator it1 = a.begin();
           if (x >= it1->second) {
               x -= it1->second;
               int64 mul = it1->first * (it1->first - 1) / 2;
               mul %= mod;
               mul *= it1->second;
               mul %= mod;
               ans +=  mul;
               ans %= mod;
               ans += mod;
               ans %= mod;
               a.erase(it1->first);
           } else {
               a[it1->first] -= x;
               int64 mul = it1->first * (it1->first - 1) / 2;
               mul %= mod;
               mul *= x;
               mul %= mod;
               ans += mul;
               ans %= mod;
               ans += mod;
               ans %= mod;
               x = 0;
           }
        }
    }
    ans %= mod;
    ans += mod;
    ans %= mod;           
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
