#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (int)n; ++i)
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
class MillerRabin {
    vector<int> prime;
    // calculate (a * b) % c
    ll mulmod(ll a, ll b, ll c) {
        if (a < b) swap (a, b);
        ll res = 0, x = a;
        while (b > 0) {
            if (b & 1) {
                res = res + x;
                if (res >= c) res -= c;
            }
            x = x * 2;
            if (x >= c) x -= c;
            b >>= 1;
         }
         return res % c;
    }
    // calculate (a ^ p) % mod
    ll bigmod(ll a, ll p, ll mod) {
        ll x = a, res = 1;
        while (p) {
            if (p & 1) res = mulmod(res, x, mod);
            x = mulmod(x, x, mod);
            p >>= 1;
        }
        return res;
    }
    bool witness(ll a, ll d, ll s, ll n) {
        ll r = bigmod(a, d, n);
        if (r == 1 || r == n - 1) return false;
        for (int i = 0; i < s - 1; ++i) {
            r = mulmod(r, r, n);
            if (r == 1) return true;
            if (r == n - 1) return false;
        }
        return true;
    }
public:
    MillerRabin() {
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    }
    bool test(ll n) {
        if (n <= 1) return false;
        ll p = n - 1;
        ll s = 0;
        while (!(p & 1)) {
            p /= 2;
            s++;
        }
        ll d = p;
        p = n - 1;
        for (int i = 0; i < (int)prime.size() && prime[i] < n; ++i) {
            if (witness(prime[i], d, s, n)) return false;
        }
        return true;
    }
};
int n, tot;
MillerRabin mr;
vector<ll> res;
ll get(ll& cur, int base) {
    ll ret = 0;
    for (int i = n - 1; i >= 0; --i) {
        ret = ret * base + ((cur & (1ll << i)) != 0);
    }
    return ret;
}
string to_s(ll num) {
    string ret;
    for (int i = n - 1; i >= 0; --i) {
        if (num & (1ll << i)) {
            ret.push_back('1');
        }
        else {
            ret.push_back('0');
        }
    }
    return ret;
}
ll fac(ll& num) {
    for (ll i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return i;
        }
    }
    assert(false);
}
void solve() {
    cin >> n >> tot;
    for (ll i = 0; i < (1ll << (n - 2)); ++i) {
        bool ok = true;
        ll val = (1ll << (n - 1)) + (i << 1) + 1ll;
        for (int j = 2; j <= 10; ++j) {
            ll tmp = get(val, j);
            if (mr.test(tmp)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            res.push_back(val);
            if ((int)res.size() == tot) {
                break;
            }
        }
    }
    FOR(i, res.size()) {
        // cout << res[i] << " ";
        printf("%s", to_s(res[i]).c_str());
        for (int j = 2; j <= 10; ++j) {
            ll tmp = get(res[i], j);
            printf(" %lld", fac(tmp));
        }
        printf("\n");
    }
    return;
}
int main() {
    int TestCase;
    cin >> TestCase;
    FOR(caseID, TestCase) {
        cout << "Case #" << caseID + 1 << ":\n";
        solve();
    }
    return 0;
}
