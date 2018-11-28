#include <bits/stdc++.h>
#define MAXN 30

using namespace std;

char a[MAXN][MAXN];
int b[MAXN][MAXN], c[MAXN][MAXN];
int g[MAXN], vis[MAXN];

int check(int N, int now) {
    if (now >= N) return 1;
    int x = g[now];
    int flag = 0;
    for (int i = 0; i < N; ++i) {
        if (c[x][i] && !vis[i]) {
            vis[i] = 1;
            if (!check(N, now + 1)) return 0;
            flag = 1;
            vis[i] = 0;
        }
    }
    if (!flag) return 0;
    return 1;
}

int main() {
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int N;
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) 
            scanf("%s", a[i]);
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                b[i][j] = a[i][j] - '0';
        int ans = N * N;
        for (int i = 0; i < 1 << (N * N); ++i) {
            int now = 0;
            int flag = 1;
            int tmpCnt = 0;
            for (int j = 0; j < N; ++j)
                for (int k = 0; k < N; ++k) {
                    c[j][k] = 0;
                    if (i & (1 << now)) c[j][k] = 1;
                    now++;
                    if (c[j][k] < b[j][k]) flag = 0;
                    if (c[j][k] > b[j][k]) tmpCnt++;
                }
            if (!flag) continue;
            for (int i = 0; i < N; ++i) g[i] = i;
            do {
                memset(vis, 0, sizeof(vis));
                if (!check(N, 0)) {
                    flag = 0;
                    break;
                }
            }while (next_permutation(g, g + N));
            if (flag) ans = min(ans, tmpCnt);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}