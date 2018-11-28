#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int n,m;
        cin >> n >> m;
        vvi a(n, vi(m));
        vi r(n, 0), c(m, 0);
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
            scanf("%d", &a[i][j]);
            r[i] = max(r[i], a[i][j]);
            c[j] = max(c[j], a[i][j]);
        }
        bool ok = 1;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j)
            if (a[i][j] < r[i] && a[i][j] < c[j]) {
                ok = 0;
            }
        if (ok) {
            cout << "YES\n";
        } else cout << "NO\n";
    }
    return 0;
}
