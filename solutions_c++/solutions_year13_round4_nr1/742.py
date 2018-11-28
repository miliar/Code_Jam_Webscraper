#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

const long long mod = 1000002013;

int n, m;
struct train {
    int o, e, p;
} a[1010];

struct event {
    int t, time;
    bool in;
} e[2222];

vector<pair<int, int> > tic;
int ne;

bool cmp (event e1, event e2) {
    return (e1.time < e2.time) || (e1.time == e2.time && e1.in > e2.in);
}

long long cost(int b, int e) {
    long long k = e - b;
    long long x = n - k;
    return ((long long)n*(n + 1) - x*(x + 1)) / 2;
}

void solve() {
    cin >> n >> m;
    ne = 0;
    for (int i = 1; i <= m; i++) {
        cin >> a[i].o >> a[i].e >> a[i].p;
        e[++ne] = (event) {i, a[i].o, true};
        e[++ne] = (event) {i, a[i].e, false};
    }
    sort(e + 1, e + 1 + ne, cmp);
    tic.clear();
    long long res = 0;
    for (int i = 1; i <= ne; i++) {
        int tr = e[i].t;
        int cur;
        if (e[i].in) {
            cur = a[tr].o;
            tic.push_back(make_pair(cur, a[tr].p));
        } else {
            cur = a[tr].e;
            int p = a[tr].p;
            while (p >= (tic.back()).second) {
                int x = (tic.back()).first;
                int y = (tic.back()).second;
                p -= y;
                res += cost(x, a[tr].e) % mod * y % mod;
                res %= mod;
                tic.pop_back();
            }
            if (p > 0) {
                int x = (tic.back()).first;
                int &y = (tic.back()).second;
                y -= p;
                res += cost(x, a[tr].e) % mod * p % mod;
                res %= mod;
            }
        }
    }
    long long sum = 0;
    for (int i = 1; i <= m; i++) {
        sum += cost(a[i].o, a[i].e) % mod * a[i].p % mod;
        sum %= mod;
    }
    cout << (sum - res + mod) % mod << endl;
}

int main() {

    freopen("Alarge.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int T = 0, cnt = 0;
    cin >> T;
    while (T > 0) {
        cout << "Case #" << ++cnt << ": ";
        solve();
        --T;
    }

}
