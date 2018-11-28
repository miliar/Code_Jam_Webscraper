#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

bool can(const vector<ll>& a, ll up) {
    int ptr = 0;
    int n = a.size();
    forn(i, 3) {
        ll sum = 0;
        while (ptr < n && a[ptr] + sum <= up) sum += a[ptr++];
    }    
    return ptr == n;
}

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    int n;
    ll p, q, r, s;
    cin >> n >> p >> q >> r >> s;
    vector<ll> a(n);
    forn(i, n) a[i] = (p * i + q) % r + s;
    ll sum = 0;
    forn(i, n) sum += a[i];
    ll lf = 0, rg = 1e15;
    while (rg - lf > 2) {
        ll mid = (lf + rg) / 2;
        if (can(a, mid)) {
            rg = mid;    
        } else {
            lf = mid + 1;
        }
    }
    cout.precision(12);
    cout << fixed;
    for (ll mx = lf; mx <= rg; mx++) {
        if (can(a, mx)) {
            cout << ld(sum - mx) / sum << endl;
            return;    
        }
    }
    throw;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
