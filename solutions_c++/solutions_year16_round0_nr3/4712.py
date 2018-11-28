#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
using ll = long long;

#define all(c) (c).begin(), (c).end()
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const ll INF = 1e9;
const ll MOD = 1e9 + 7;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int N, J;

bool isPrime(ll n) {
    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

ll cnv(const string &s, int base) {
    ll num = 0;
    rep(i, s.size()) num = num * base + s[i] - '0';
    return num;
}

bool isPrime(const string &s, int base) { return isPrime(cnv(s, base)); }
bool ok(const string &s) {
    bool res = true;
    rep(i, 11) if (i > 1) res &= !isPrime(s, i);
    return res;
}
uint32_t xor128(void) {
    static uint32_t x = 123456789;
    static uint32_t y = 362436069;
    static uint32_t z = 521288629;
    static uint32_t w = 88675123;
    uint32_t t;

    t = x ^ (x << 11);
    x = y;
    y = z;
    z = w;
    return w = (w ^ (w >> 19)) ^ (t ^ (t >> 8));
}

string make(int n) {
    string res;
    rep(i, n - 2) {
        if(xor128() % 2) res += "1";
        else res += "0";
    }
    res = "1" + res + "1";
    return res;
}

void solve() {
    set<string> ans;
    while (ans.size() != J) {
        auto s = make(N);
        if (ok(s)) ans.insert(s);
    }
    for (auto e : ans) {
        cout<<e<<" ";
        rep(i,11) if(i>1) {
            auto num = cnv(e, i);
            // cerr << num << endl;
            for(ll i=2;i*i<=num;i++) {
                if(num%i==0) {
                    cout<<i<<" ";
                    break;
                }
            }
        }
        cout<<endl;
    }
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cin >> N >> J;
        printf("Case #%d:\n", i + 1);
        solve();
    }
    return 0;
}
