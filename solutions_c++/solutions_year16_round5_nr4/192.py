#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
/*
const int maxn=1e5;
const int maxm=1e3;
cosnt ld eps;
*/
bool is_b(const string& s) {
    for (auto c : s) {
        if (c == '0') return false;
    }
    return true;
}

void Solve() {
    int n, l;
    cin >> n >> l;
    int imp = 0;
    for (int i = 0; i <= n; ++i) {
        string s;
        cin >> s;
        if (i < n && is_b(s)) {
            imp = 1;
        }
    }
    if (imp) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if (l == 1) {
        cout << "0 0?\n";
        return;
    }

    for (int i = 1; i < l; ++i) {
        cout << "?";
    }
    cout << " ";
    cout << "10?";
    for (int i = 0; i < 50; ++i) {
        cout << "10";
    }
    cout << "\n";
}

int main() {
    freopen("d.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        Solve();
    }
}
