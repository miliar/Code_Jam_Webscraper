#include <bits/stdc++.h>
using namespace std;
const int MAXN = 4 + 1;

int T, N, ans;
char G[MAXN][MAXN];
int g[MAXN][MAXN];

int p[MAXN * MAXN];

bool visit1[MAXN];
bool visit2[MAXN];

bool dfs(int idx) {
    if (idx == N) {
        return false;
    }
    for (int i = 0; i < N; ++i) {
        if (!visit1[i]) {
            visit1[i] = true;
            bool flag = true;
            for (int j = 0; j < N; ++j) {
                if (!visit2[i]) {
                    flag = false;
                    visit2[i] = true;
                    if (dfs(idx + 1)) {
                        return true;
                    }
                    visit2[i] = false;
                }
            }
            if (flag) {
                return true;
            }
            visit1[i] = false;
        }
    }
}

bool check() {
    memset(visit1, false, sizeof(visit1));
    memset(visit2, false, sizeof(visit2));
    return !dfs(0);
}

void iter() {
    for (int i = 0; i < (1 << (N * N)); ++i) {
        int cnt = 0;
        for (int j = 0; j < N * N; ++j) {
            int r = j / N;
            int c = j % N;
            if (G[r][c] == '1') {
                g[r][c] = 1;
            } else {
                if (i & (1 << j)) {
                    g[r][c] = 1;
                    ++cnt;
                } else {
                    g[r][c] = 0;
                }
            }
        }
        if (cnt < ans) {
            if (check()) {
                ans = cnt;
            }
        }
    }
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int i = 0; i < N; ++i) {
            cin >> G[i];
        }
        ans = N * N;
        iter();
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
