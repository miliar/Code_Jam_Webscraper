#include <cstdio>
using namespace std;
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

void solve(int t) {
    int n, m;
    cin >> n >> m;
    vector<vector<int> > a(n);
    for (int i = 0; i < n; ++i) {
        a[i].resize(m);
        for (int j = 0; j < m; ++j) cin >> a[i][j];
    }
    bool ok = true;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            int r = a[i][j];
            for (int k = 0; k < m; ++k) r = max(r, a[i][k]);
            int c = a[i][j];
            for (int k = 0; k < n; ++k) c = max(c, a[k][j]);
            if (a[i][j] != min(r, c)) ok = false;
        }
    cout << "Case #" << t << ": ";
    if (ok) cout << "YES"; else cout << "NO";
    cout << endl;
}


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
}

