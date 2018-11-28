#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 15

using namespace std;

char mat[MaxN][MaxN];
bool f[5][1 << 16];
int cmap[5][5], N;

int lowbit(int x) {
    return x & (-x);
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int i, j, T, T0 = 0;
    scanf("%d", &T);
    f[1][1] = 1;
    for (int i = 2; i <= 4; ++i) {
        for (int j = 1; j < (1 << (i * i)); ++j) {
            int cnt = 0;
            for (int k = 0; k < i; ++k)
                for (int l = 0; l < i; ++l) {
                    if (j & (1 << cnt))
                        cmap[k][l] = 1;
                    else
                        cmap[k][l] = 0;
                    ++cnt;
                }
            f[i][j] = 1;
            for (int k = 0; k < i; ++k) {
                for (int l = 0; l < i; ++l) {
                    if (cmap[k][l] == 1) {
                        int res = 0;
                        for (int k1 = 0; k1 < i; ++k1) {
                            for (int l1 = 0; l1 < i; ++l1) {
                                if (k1 == k || l1 == l)
                                    continue;
                                res = res * 2 + cmap[k1][l1];
                            }
                        }
                        if (!f[i - 1][res])
                            f[i][j] = 0;
                    }
                }
                if (f[i][j] == 0)
                    break;
            }
        }
    }
    for ( ; T; --T) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) {
            scanf("%s", &mat[i]);
        }
        int now = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j)
                now = now * 2 + mat[i][j] - '0';
        }
        int ans;
        ans = ~0U >> 1;
        for (int i = 0; i < (1 << N * N); ++i) {
            if (f[N][i] && (now & i) == now) {
                int c = i - now;
                int cnt = 0;
                while(c > 0) {
                    c -= lowbit(c);
                    ++cnt;
                }
                ans = min(ans, cnt);
            }
        }
        printf("Case #%d: %d\n", ++T0, ans);
    }
    return 0;
}
