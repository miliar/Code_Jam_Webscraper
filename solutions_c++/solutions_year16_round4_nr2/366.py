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

#define MaxN 310

using namespace std;

int N, K;
double p[MaxN];
double a[MaxN];
double f[MaxN][MaxN], ans;

void check() {
    memset(f, 0, sizeof(f));
    f[0][K / 2] = 1;
    for (int i = 1; i <= K; ++i) {
        for (int j = 0; j <= K; ++j) {
            if (j > 0)
                f[i][j] += f[i - 1][j - 1] * p[i];
            if (j < K)
                f[i][j] += f[i - 1][j + 1] * (1 - p[i]);
        }
    }
    ans = max(ans, f[K][K / 2]);

}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, T0 = 0;
    scanf("%d", &T);
    for ( ; T; --T) {
        scanf("%d%d", &N, &K);
        for (int i = 1; i <= N; ++i)
            scanf("%lf", &a[i]);
        sort(a + 1, a + N + 1);
        ans = 0;
        for (int i = 0; i <= K; ++i) {
            for (int j = 1; j <= i; ++j)
                p[j] = a[j];
            int tot = i;
            for (int j = N; j >= N - (K - i) + 1; --j)
                p[++tot] = a[j];
            check();
        }
        printf("Case #%d: %.8lf\n", ++T0, ans);
    }
    return 0;

}
