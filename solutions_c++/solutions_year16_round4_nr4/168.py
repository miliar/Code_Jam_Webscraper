#include <bits/stdc++.h>
using namespace std;
const int MAXN = 6;
int TC, N,  a[MAXN];
char g[MAXN][MAXN+5];
bitset<MAXN> dm[MAXN];
bitset<MAXN> d;
bool r(int k) {
    if (k == N) return 1;
    int x = a[k];
    bool cando = 0;
    for (int i = 0; i < N; ++i) {
        if (d[i] == 0 && dm[x][i] == 1) {
            cando = 1;
            d[i] = 1;
            if (!r(k+1)) return 0;
            d[i] = 0;
        }
    }
    return cando;
}
int main () {
    scanf("%d", &TC);
    for (int T = 1; T <= TC; ++T) {
        scanf("%d", &N);
        int ans = N*N;
        for (int i = 0; i < N; ++i) scanf("%s", g[i]);
        for (int bs = 0; bs < (1<<(N*N)); ++bs) {
            bool pass = 1;
            for (int i = 0; i < N; ++i) {
                a[i] = i;
                for (int j = 0; j < N; ++j) {
                    if (g[i][j] == '1') dm[i][j] = 1;
                    else if (bs & (1<<(i*N + j))) dm[i][j] = 1;
                    else dm[i][j] = 0;
                }
            }
            do {
                d.reset();
                if (!r(0)) {
                    pass = 0;
                    break;
                }
            } while(next_permutation(a, a+N));
            if (pass) ans = min(ans, __builtin_popcount(bs));
        }
        printf("Case #%d: %d\n", T, ans);
    }
}