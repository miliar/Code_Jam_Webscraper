#include <bits/stdc++.h>
using namespace std;
const int maxn = 4;

bool a[maxn][maxn], tmp[maxn];
int n;

bool fail() {
    for (int i = 0; i < n; i++) {
        if (i < n - 1) {
            for (int j = 0; j < n; j++) {
                a[i][j] ^= a[n - 1][j] ^= a[i][j] ^= a[n - 1][j];
            }
        }

        memcpy(tmp, a[n - 1], sizeof(tmp));
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                for (int l = 0; l < n; l++) {
                    int mx = 1;
                    if (n >= 2) {
                        if (a[0][j]) {
                            a[n - 1][j] = false;
                            if (n >= 3 && j != k) {
                                if (a[1][k]) {
                                    a[n - 1][k] = false;
                                    if (n >= 4) {
                                        if (a[2][l]) {
                                            a[n - 1][l] = false;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    int cnt = a[n - 1][0] + a[n - 1][1] + 
                                a[n - 1][2] + a[n - 1][3];
                    memcpy(a[n - 1], tmp, sizeof(a[n - 1]));
                    if (cnt == 0) {
                        if (i < n - 1) {
                            for (int j = 0; j < n; j++) {
                                a[i][j] ^= a[n - 1][j] ^= a[i][j] ^= a[n - 1][j];
                            }
                        }    
                        return true;
                    }
                }
            }
        }

        if (i < n - 1) {
            for (int j = 0; j < n; j++) {
                a[i][j] ^= a[n - 1][j] ^= a[i][j] ^= a[n - 1][j];
            }
        }    
    }

    return false;
}

void solve() {
    memset(a, 0, sizeof(a));
    cin >> n;
    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < n; j++) {
            a[i][j] = (line[j] == '1');
        }
    }

    int res = 1e9;
    for (int mask = 0; mask < (1 << (n * n)); mask++) {
        bool bad = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] && ((mask >> (n * i + j)) & 1)) {
                    bad = true;
                }
            }
        }
        if (bad) {
            continue;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((mask >> (n * i + j)) & 1) {
                    a[i][j] = true;
                }
            }
        }

        if (!fail()) {
            int cost = __builtin_popcount(mask);
            res = min(cost, res);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((mask >> (n * i + j)) & 1) {
                    a[i][j] = false;
                }
            }
        }
    }

    cout << res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
