#include <bits/stdc++.h>

using namespace std;

int n;
std::string a[26];
int b[26][26];
int d[26];
bool used[26];

bool dfs(int at) {
    if (at == n) {
        return true;
    }
    int id = d[at];
    bool found = false;
    for (int i = 0; i < n; ++i) {
        if (used[i] || !b[id][i]) {
            continue;
        }
        used[i] = true;
        found = true;
        if (!dfs(at + 1)) {
            return false;
        }
        used[i] = false;
    }
    if (!found) {
        return false;
    }
    return true;
}

bool check() {
    for (int i = 0; i < n; ++i) {
        d[i] = i;
    }
    do {
        for (int i = 0; i < n; ++i) {
            used[i] = false;
        }
        if (!dfs(0)) {
            return false;
        }
    } while (next_permutation(d, d + n));
    return true;
}

void update(int state, int& res) {
    int cost = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int pos = i * n + j;
            b[i][j] = (state >> pos) & 1;
            if (b[i][j] == 0 && a[i][j] == '1') {
                return;
            }
            if (b[i][j] == 1 && a[i][j] == '0') {
                ++cost;
            }
        }
    }
    // printf("cost : %d\n", cost);
    if (check()) {
        res = min(res, cost);
    }
}

int main() {

    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {

        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        int res = n * n;

        for (int state = 0; state < (1 << (n * n)); ++state) {
            update(state, res);
        }

        printf("Case #%d: %d\n", test, res);
    }

    return 0;
}
