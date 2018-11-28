#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 200;

int n, m;
int h[MAXN][MAXN];

string solve() {
    vector<int> u(n);
    vector<int> v(m);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            u[i] = max(u[i], h[i][j]);
            v[j] = max(v[j], h[i][j]);
        }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (min(u[i], v[j]) != h[i][j])
                return "NO";
    return "YES";
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> h[i][j];
        cout << "Case #" << tt << ": " << solve() << '\n';
    }

    return 0;
}

