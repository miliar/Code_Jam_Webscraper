#include <iostream>
#include <vector>
#include <cstdio>
#include <iomanip>
#include <algorithm>

#define inf 1e13
#define maxn 16
#define ll unsigned long long
using namespace std;

string sol[20][3];

void solve() {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    sol[0][0] = "P";
    sol[0][1] = "R";
    sol[0][2] = "S";

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (sol[i-1][j] < sol[i-1][(j+1)%3])
                sol[i][j] = sol[i-1][j] + sol[i-1][(j+1)%3];
            else sol[i][j] = sol[i-1][(j+1)%3] + sol[i-1][j];
        }
    }

    string ans = "Z";
    for (int j = 0; j < 3; ++j) {
        if (count(sol[n][j].begin(), sol[n][j].end(), 'P') == p &&
            count(sol[n][j].begin(), sol[n][j].end(), 'R') == r &&
            count(sol[n][j].begin(), sol[n][j].end(), 'S') == s  )
                ans = min(ans, sol[n][j]);
    }

    if (ans == "Z")
        cout << "IMPOSSIBLE";
    else cout << ans;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int tests;

    cin >> tests;

    for (int k = 1;k <= tests; ++k) {
        cout << "Case #" << k << ": ";
        solve();
        cout << "\n";
    }
}
