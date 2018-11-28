#include <bits/stdc++.h>

using namespace std;

#define sz(a) int(a.size())
#define pb push_back

typedef long long ll;

ll ok(ll x) {
    ll sqrtx = sqrt(x);
    for (ll i = 2; i <= sqrtx; i++)
        if (x % i == 0) return i;
    return 0;
}

ll gen(int x, ll base) {
    ll res = 0, p = 1;
    while (x) {
        res += p * (x & 1);
        x >>= 1;
        p *= base;
    }
    return res;
}

string toBinary(ll x) {
    string res = "";
    while (x) {
        res = char((x & 1) + '0') + res;
        x >>= 1;
    }
    return res;
}

void solve(int N, int J) {
    vector <vector<ll> > res;
    for (ll i = (1 << (N-1)) + 1; i < (1 << N) && sz(res) < J; i += 2) {
        vector <ll> cur;
        for (int b = 2; b <= 10; b++) {
            ll x = gen(i, b);
            ll y = ok(x);
            if (y) {
                cur.pb(y);
            }
            else break;
        }
        if (sz(cur) == 9) {
            cur.pb(i); 
            res.pb(cur);
        }
    }
    for (int i = 0; i < sz(res); i++) {
        cout << toBinary(res[i][9]);
        for (int j = 0; j < 9; j++) cout << " " << res[i][j];
        cout << '\n';
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    ios::sync_with_stdio(0);
    int T; cin >> T;
    for (int te = 1; te <= T; te++) {
        int N, J; cin >> N >> J;
        cout << "Case #" << te << ":\n";
        solve(N, J);
    }
    
    return 0;
}
