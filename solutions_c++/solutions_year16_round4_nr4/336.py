#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int maxn = 30;

int e[maxn][maxn];
int c[maxn][maxn];
int subm[maxn];
int wm[1 << 25];
int ans[maxn];

int tr(int mask, int n) {
    int cur_ans = 0;
    for (int i = 0; i < n; ++i) subm[i] = 0, ans[i] = 0;
    for (int i = 0, k = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j, ++k) {
            c[i][j] = mask & (1 << k);
            if (c[i][j]) subm[j] |= (1 << i), ++cur_ans;
            else c[i][j] = 0;
            if (e[i][j] && !c[i][j]) return n * n;
        }
    }
    for (int jm = 1; jm < (1 << n); ++jm) {
        wm[jm] = 0;
        int jk = 0;
        int awm = (1 << n) - 1;
        for (int t = 0; t < n; ++t) {
            if (!(jm & (1 << t))) continue;
            ++jk;
            wm[jm] |= subm[t];
            awm &= subm[t];
        }
        int wk = 0;
        for (int t = 0; t < n; ++t) {
            if ((wm[jm] & (1 << t))) ++wk;
        }
        if (wk < jk) return n * n;
        if (wk > jk) continue;
        //printf("%d %d %d\n", jm, wm[jm], awm);
        for (int t = 0; t < n; ++t) {
            if (!(awm & (1 << t))) continue;    
            ans[t] = 1;
            //printf("!%d\n", t);
        }
    }
    for (int i = 0; i < n; ++i) {
        if (ans[i] == 0) return n * n;
    }
    /*
    printf("\n");
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            printf("%d", c[i][j]);
        }
        printf("\n");
    }
    printf("%d\n", cur_ans);
    */
    return cur_ans;
}

void Solve() {
    int n;
    int m = 0;
    scanf("%d\n", &n);
//    for (int i = 0; i < (1 << n); ++i) wm[i] = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char c;
            scanf("%c", &c);
            e[i][j] = (c == '1');
            if (e[i][j]) {
                ++m;
  //              subm[j] |= (1 << i);
            }
        }
        scanf("\n");
    }
    int ans_t = n * n;
    for (int jm = 0; jm < (1 << (n * n)); ++jm) {
        ans_t = min(ans_t, tr(jm, n));
    }
    printf("%d\n", ans_t - m);
}

int main() {
    freopen("d.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        Solve();
    }
}
