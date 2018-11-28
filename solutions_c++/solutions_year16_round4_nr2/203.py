#include <bits/stdc++.h>
using namespace std;
const int MAXN = 16 + 1;

int T, N, K;
double P[MAXN];
double path[MAXN];
double ans;

void check() {
    double p = 0.0;
    for (int i = 0; i < (1 << K); ++i) {
        int cnt = 0;
        for (int j = 0; j < K; ++j) {
            if (i & (1 << j)) {
                ++cnt;
            }
        }
        if (cnt == K / 2) {
            double p0 = 1.0;
            for (int j = 0; j < K; ++j) {
                if (i & (1 << j)) {
                    p0 *= path[j];
                } else {
                    p0 *= 1.0 - path[j];
                }
            }
            p += p0;
        }
    }
    ans = max(ans, p);
}

void dfs(int idx, int d) {
    if (d == K) {
        check();
        return;
    }
    if (idx >= N) {
        return;
    }
    dfs(idx + 1, d);
    path[d] = P[idx];
    dfs(idx + 1, d + 1);
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> K;
        for (int i = 0; i < N; ++i) {
            cin >> P[i];
        }
        ans = 0.0;
        dfs(0, 0);
        cout << "Case #" << t << ": ";
        printf("%.10f\n", ans);
    }
    return 0;
}
