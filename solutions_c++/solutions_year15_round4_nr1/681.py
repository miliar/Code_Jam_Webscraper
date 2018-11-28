#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
 
#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
 
typedef long long int64;
 
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int> > a(n, vector<int> (m, 0));
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < m; ++j) {
            if (s[j] == '<') a[i][j] = 1;
            if (s[j] == '>') a[i][j] = 2;
            if (s[j] == '^') a[i][j] = 3;
            if (s[j] == 'v') a[i][j] = 4;
        }
    }
    vector<vector<vector<bool> > > ok(n, vector<vector<bool> > (m, vector<bool> (5, true)));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (a[i][j] != 0) {
                ok[i][j][1] = false;
                break;
            }
    for (int i = 0; i < n; ++i)
        for (int j = m - 1; j >= 0; --j)
            if (a[i][j] != 0) {
                ok[i][j][2] = false;
                break;
            }
    for (int j = 0; j < m; ++j)
        for (int i = 0; i < n; ++i)
            if (a[i][j] != 0) {
                ok[i][j][3] = false;
                break;
            }
    for (int j = 0; j < m; ++j)
        for (int i = n - 1; i >= 0; --i)
            if (a[i][j] != 0) {
                ok[i][j][4] = false;
                break;
            }
    int ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (!ok[i][j][a[i][j]]) {
                bool flag = false;
                for (int k = 1; k <= 4; ++k)
                    if (ok[i][j][k]) {
                       flag = true;
                       ++ans;
                       break;
                    }
                if (!flag) {
                    cout << "IMPOSSIBLE" << endl;
                    return;
                }
            }
    cout << ans << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
