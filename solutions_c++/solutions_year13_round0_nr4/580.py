#include <cstdio>
#include <algorithm>
using namespace std;

int K, N;
int keys[210];
int type[210];
int qins[210], ins[210][410];

int dp[1<<21], mask;
int qseq, seq[210];

int solve() {
    if (qseq == N)
        return 1;
    if (dp[mask] != -1)
        return dp[mask];
    for (int i = 0; i < N; i++) if (!(mask & (1 << i))) {
        if (keys[type[i]] > 0) {
            mask ^= 1 << i;
            keys[type[i]]--;
            for (int j = 0; j < qins[i]; j++)
                keys[ins[i][j]]++;
            seq[qseq++] = i;
            if (solve())
                return 1;
            qseq--;
            for (int j = 0; j < qins[i]; j++)
                keys[ins[i][j]]--;
            keys[type[i]]++;
            mask ^= 1 << i;
        }
    }
    return dp[mask] = 0;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &K, &N);
        for (int i = 0; i <= 200; i++)
            keys[i] = 0;
        for (int i = 0, x; i < K; i++) {
            scanf("%d", &x);
            keys[x]++;
        }
        for (int i = 0; i < N; i++) {
            scanf("%d %d", &type[i], &qins[i]);
            for (int j = 0; j < qins[i]; j++)
                scanf("%d", &ins[i][j]);
        }
        for (int i = 0, lim = 1 << N; i < lim; i++)
            dp[i] = -1;
        mask = 0;
        qseq = 0;
        int ans = solve();
        printf("Case #%d:", t);
        if (ans) {
            for (int i = 0; i < qseq; i++)
                printf(" %d", seq[i]+1);
            puts("");
        }
        else {
            puts(" IMPOSSIBLE");
        }
    }
}
