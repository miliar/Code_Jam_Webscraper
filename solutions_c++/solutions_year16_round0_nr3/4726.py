#include <bits/stdc++.h>

using namespace std;
#define ll long long
/*
 * calculates (a * b) % c taking into account that a * b might overflow
 */
ll mulmod(ll a, ll b, ll mod) {
    ll x = 0, y = a % mod;
    while (b > 0) {
        if (b % 2 == 1) {
            x = (x + y) % mod;
        }
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}
/*
 * modular exponentiation
 */
ll modulo(ll base, ll exponent, ll mod) {
    ll x = 1;
    ll y = base;
    while (exponent > 0) {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}

/*
 * Miller-Rabin primality test, iteration signifies the accuracy
 */
bool Miller(ll p, int iteration) {
    if (p < 2) {
        return false;
    }
    if (p != 2 && p % 2 == 0) {
        return false;
    }
    ll s = p - 1;
    while (s % 2 == 0) {
        s /= 2;
    }
    for (int i = 0; i < iteration; i++) {
        ll a = rand() % (p - 1) + 1, temp = s;
        ll mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1) {
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }
        if (mod != p - 1 && temp % 2 == 0) {
            return false;
        }
    }
    return true;
}

int cases = 1, cnt = 0;

ll cnv(string ex, ll base) {
    ll sum = 0, weight = 1;
    for (int i = ex.size() - 1; i > -1; --i) {
        if (ex[i] == '1')sum += weight;
        weight *= base;
    }
    return sum;
}

set<string> out;

pair<bool, ll> geet(ll num) {
    for (ll i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return make_pair(true, i);
        }
    }
    return make_pair(false, 0LL);
}

int main(void) {
    freopen("/home/vanessi/ClionProjects/CodeJamQC/Coin Jam.in", "r", stdin);
    freopen("/home/vanessi/ClionProjects/CodeJamQC/Coin Jam.out", "w", stdout);
    int t, n, len;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &len, &n);
        printf("Case #%d:\n", cases++);
        for (int i = 1; cnt < n && i < 65536; ++i) {
            string ex = bitset<16>(i).to_string(); // direct output
            ex[0] = ex[ex.size() - 1] = '1';
            if (out.count(ex))
                continue;
            vector<ll> arkam;
            for (int j = 2; j <= 10; ++j) {
                arkam.push_back(cnv(ex, j));
            }
            vector<ll> factors;
            for (ll num : arkam) {
                pair<bool, ll> re = geet(num);
                if (re.first)factors.push_back(re.second);
                else break;
            }
            if (factors.size() == 9 && out.count(ex) == 0) {
                out.insert(ex);
                cnt++;
                printf("%s ", ex.c_str());
                for (ll num : factors) {
                    printf("%lld ", num);
                }
                puts("");
            }
        }
    }
}