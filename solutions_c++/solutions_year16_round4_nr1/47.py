#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>

using namespace std;
using ll = long long;
using ull = unsigned long long;
constexpr int TEN(int n) {return (n==0)?1:10*TEN(n-1);}

string s = "RPS";
string rev(int n, int w) {
    if (n == 0) {
        return string("") + s[w];
    }
    string s1 = rev(n-1, w), s2 = rev(n-1, (w+2)%3);
    return min(s1, s2) + max(s1, s2);
}

void solve() {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    int g[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            g[i][j] = (i == j) ? 1 : 0;
        }
    }
    int g2[3][3];
    for (int fe = 1; fe <= n; fe++) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                g2[i][j] = g[i][j] + g[(i+2)%3][j];
            }
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                g[i][j] = g2[i][j];
            }
        }
    }

    for (int i = 0; i < 3; i++) {
        if (g[i][0] == r and g[i][1] == p and g[i][2] == s) {
            cout << rev(n, i) << endl;
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}