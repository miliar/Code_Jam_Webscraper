#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int T, N, cas = 0;
int sk[30][30], p[30], d[30];

int dfs(int dep) {
    if (dep == N) return true;
    bool ok = true, found = false;
    int cur = p[dep];
    for (int i = 0; i < N; ++i) if (sk[cur][i] && !d[i]) {
        found = true;
        d[i] = 1;
        ok &= dfs(dep + 1);
        d[i] = 0;
    }
    ok &= found;
    return ok;
}

bool check() {
    for (int i = 0; i < N; ++i) p[i] = i;
    bool bSuccess = true;
    do {
        bSuccess &= dfs(0);
    } while(next_permutation(p, p + N));
    return bSuccess;
}

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d_out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &N);
        memset(sk, 0, sizeof(sk));
        for (int i = 0; i < N; ++i) {
            char s[128];
            scanf("%s", s);
            for (int j = 0; j < N; ++j) if (s[j] == '1') sk[i][j] = 1;
        }
        int ans = 25 * 25;
        int tot = N * N;
        for (int msk = 0; msk < (1 << tot); ++msk) {
            int cnt = 0;
            for (int i = 0; i < tot; ++i) if (msk >> i & 1) {
                ++cnt;
                ++sk[i / N][i % N];
            }
            if (check()) ans = min(ans, cnt);
            for (int i = 0; i < tot; ++i) if (msk >> i & 1) {
                --sk[i / N][i % N];
            }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
