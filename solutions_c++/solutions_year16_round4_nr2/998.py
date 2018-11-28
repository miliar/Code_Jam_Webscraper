#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define all(x) begin(x), end(x)
typedef long long ll;

vector<double> p;

const int maxN = 1 << 16;
double ans[maxN];
void dfs(int n, int k1, int k2, double pr, int mask) {
    if (k1 + k2 == 0) {
        ans[mask] += pr;
        return;
    }
    if (n == 0) {
        return;
    }
    n--;
    if (k1) {
        dfs(n, k1 - 1, k2, pr * p[n], mask | (1 << n));
    }
    if (k2) {
        dfs(n, k1, k2 - 1, pr * (1 - p[n]), mask | (1 << n));
    }
    dfs(n, k1, k2, pr, mask);
}

int main() {
    srand(time(0));
    #define task "t"
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
    int t;
    cin >> t;
    for (int ii = 0; ii < t; ii++) {
        int n, k;
        cin >> n >> k;
        p.resize(n);
        fill(ans, ans + (1 << n), 0.0);
        for (auto &x : p) {
            cin >> x;
        }
        dfs(p.size(), k / 2, k / 2, 1.0, 0);

        cout.precision(12);

        cout << fixed << "Case #" << ii + 1 << ": " << *max_element(ans, ans + (1 << n)) << endl;
    }
    return 0;
}
