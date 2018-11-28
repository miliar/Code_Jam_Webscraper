#include "bits/stdc++.h"

using namespace std;

bool in(int mask, int x) {
    return (mask >> x) & 1;
}

int main() {
        int T;
        scanf("%d", &T);
        for (int z = 1; z <= T; ++z) {
            printf ("Case #%d: ", z);
            int n, k;
            scanf("%d %d", &n, &k);
            vector <long double> p(n + 1);
            for (int i = 0; i < n; ++i) {
                double x;
                scanf("%lf", &x);
                p[i] = x;
            }

            long double ans = 0;
            for (int i = 0; i < (1 << n); ++i) {
                long double cur = 0;
                if (__builtin_popcount(i) == k) {
                    for (int s = i; s; s = (s - 1) & i) {
                        if (__builtin_popcount(s) == k / 2) {
                            long double cp = 1;
                            for (int x = 0; x < n; ++x) {
                                if (in(i, x) && in(s, x)) {
                                    cp *= p[x];
                                } else  if (in(i, x)) {
                                    cp *= (1 - p[x]);
                                }
                            }
                            cur += cp;
                        }
                    }
                }
                ans = max(ans, cur);
            }
            printf("%.10lf\n", (double) ans);
        }
}

// const int MAXN = 200;
//
// long double dp[MAXN + 100][MAXN + 100][2 * MAXN + 100];
//
// inline long double &take(int i, int j, int k) {
//     return dp[i][j][MAXN + 50 + k];
// }
//
// int main() {
//     int T;
//     scanf("%d", &T);
//     for (int z = 1; z <= T; ++z) {
//         printf ("Case #%d: ", z);
//         int n, k;
//         scanf("%d %d", &n, &k);
//         for (int i = 0; i < MAXN + 100; ++i) {
//             for (int j = 0; j  < MAXN + 100; ++j) {
//                 for (int k = -MAXN - 10; k < MAXN + 10; ++k) {
//                     take(i, j, k) = 0;
//                 }
//             }
//         }
//         vector <long double> p(n + 1);
//         for (int i = 0; i < n; ++i) {
//             double x;
//             scanf("%lf", &x);
//             p[i + 1] = x;
//         }
//         for (int i = 1; i <= n; ++i) {
//             take(i, 1, 0) = 0;
//             take(i, 1, 1) = max(take(i - 1, 1, 1), p[i]);
//             take(i, 1, -1) = max(take(i - 1, 1, 1), (1 - p[i]));
//             printf("%d %d -1: %.2lf\n", i, 1, (double)take(i, 1, -1));
//             printf("%d %d 1: %.2lf\n", i, 1, (double)take(i, 1, 1));
//             printf("%d %d 0: %.2lf\n", i, 1, (double)take(i, 1, 0));
//             for (int j = 2; j <= i; ++j) {
//                 for (int k = -i; k <= i; ++k) {
//                     take(i, j, k) = max((k != -i ? take(i - 1, j - 1, k - 1) * p[i] : 0) + (k != i ? take(i - 1, j - 1, k + 1) * (1 - p[i]) : 0), take(i - 1, j, k));
//                     printf("%d %d %d: %.2lf\n", i, j, k, (double)take(i, j, k));
//
//                 }
//
//             }
//
//         }
//         printf("%.10lf\n", (double)take(n, k, 0));
//     }
// }
