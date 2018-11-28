#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define sqr(x) ((x) * (x))
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()

typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef pair <int, int> pii;

int n, m;

vi get2(int val) {
    vi d(n);
    for (int i = 0; i < n; i++) {
        d[i] = (val & (1 << i)) ? 1 : 0;
    }
    return d;
}

ll getDiv(ll n) {
    for (int i = 2; i * 1ll * i <= n; i++) {
        if (n % i == 0) {
            return i;
        }
    }
    assert(false);
}

ll getVal(const vi &d, int b) {
    ll res = 0;
    ll pw = 1;
    for (int x : d) {
        res += pw * x;
        pw *= b;
    }
    return res;
}

bool isPrime(ll n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i * 1ll * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

bool isGood(int mask) {
    vi d = get2(mask);
    if (n < 2 || d[0] == 0 || d[n - 1] == 0) {
        return false;
    }
    for (int b = 2; b <= 10; b++) {
        ll val = getVal(d, b);
        if (isPrime(val)) {
            return false;
        }
    }
    return true;
}

void solve(int test) {
    vi res;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (isGood(mask)) {
            res.pb(mask);
            if (sz(res) == m) {
                break;
            }
        }
    }
    vi d;
    cout << "Case #" << test << ":\n";
    for (int x : res) {
        d = get2(x);
        reverse(all(d));
        for (int y : d) {
            cout << y;
        }
        reverse(all(d));
        for (int b = 2; b <= 10; b++) {
            ll val = getVal(d, b);
            cout << " " << getDiv(val);
        }
        cout << "\n";
    }
}

int main() {
    freopen("/Users/nurlan/Dropbox/Programming/contest/contest/input", "r", stdin);
    freopen("/Users/nurlan/Dropbox/Programming/contest/contest/output", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cin >> n >> m;
        solve(test);
    }
    return 0;
}