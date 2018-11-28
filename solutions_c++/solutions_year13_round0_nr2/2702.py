#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

const int MaxN = 150;
int grass[MaxN][MaxN];
bool used[MaxN][MaxN];
int n, m;

void readData() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grass[i][j];
            used[i][j] = false;
        }
    }
}

bool solve() {
    vector<int> countX(n), countY(m);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grass[i][j] == 1) {
                countX[i]++;
            }
            if (grass[i][j] == 1) {
                countY[j]++;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        if (countX[i] == m) {
            for (int j = 0; j < m; ++j) {
                used[i][j] = true;
            }
        }
    }
    for (int i = 0; i < m; ++i) {
        if (countY[i] == n) {
            for (int j = 0; j < n; ++j) {
                used[j][i] = true;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grass[i][j] == 1 && !used[i][j]) {
                return false;
            }
        }
    }
    return true;
}


int main() {
    bool answer = 0;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        readData();
        answer = solve();
        cout << "Case #" << i + 1 << ": ";
        if (answer) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
