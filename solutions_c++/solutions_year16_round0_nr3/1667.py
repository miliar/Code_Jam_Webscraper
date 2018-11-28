#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int T, J;
int n;
set <string> ans;

ll get() {
    return ((rand() * 1ll) << 16)|rand();
}

int get_mod(ll mask, int base, int p) {
    int P = 1;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (mask&(1ll << i)) {
            ans = (ans + P % p) % p;
        }
        P = P * 1ll * base % p;
    }
    return ans;
}

ll get_val(ll mask, int base) {
    ll ans = 0, P = 1;
    for (int i = 0; i < n; i++) {
        if (mask&(1ll << i)) {
            ans += P;
        }
        P *= base;
    }
    return ans;
}

bool is_ok(ll mask) {
    for (int base = 2; base <= 10; base++) {
        bool ok = 0;
        for (int i = 2; i <= 1000; i++) {
            if (get_mod(mask, base, i) == 0) {
                ok = 1;
                continue;
            }
        }
        if (!ok) return false;
    }
    return true;
}

bool is_prime(ll val) {
    for (int i = 2; i < val && i * 1ll * i <= val; i++) {
        if (val % i == 0) return false;
    }
    return true;
}

bool is_ok1(ll mask) {
    for (int base = 2; base <= 10; base++) {
        ll val = get_val(mask, base);
        if (is_prime(val)) return false;
    }
    return true;
}

string to_str(ll mask) {
    string ans = "";
    for (int i = 0; i < n; i++) {
        ans += (char)(mask % 2 + '0');
        mask /= 2;
    }
    reverse(all(ans));
    return ans;
}

ll get_val(string s) {
    ll ans = 0;
    for (int i = sz(s) - 1; i >= 0; i--) {
        if (s[i] == '1') ans |= (1ll << (sz(s) - 1 - i));
    }
    return ans;
}

ll get_div(ll mask, int base) {
    for (int i = 2; i <= 1000; i++) {
        int mod = 0;
        int P = 1;
        for (int j = 0; j < n; j++) {
            if (mask&(1ll << j)) {
                mod = (mod + P) % i;
            }
            P = 1ll * P * base % i;
        }
        if (mod == 0) return i;
    }
    return -1;
}

int main(){

    cin >> T;
    cin >> n >> J;

    srand(time(NULL));

    for (ll x = 0; x < (1ll << (n - 2)) && sz(ans) < J; x++) {
        ll mask = x;
        mask &= (1ll << (n - 2)) - 1;
        mask = 2ll * mask + 1;
        mask |= (1ll << (n - 1));
        if (is_ok(mask)) ans.insert(to_str(mask));
    }

    printf("Case #%d:\n", 1);
    forit (it, ans) {
        cout << *it;
        ll val = get_val(*it);
        for (int i = 2; i <= 10; i++) {
            cout << " " << get_div(val, i);
        }
        cout << endl;
    }
    
    return 0;
}
