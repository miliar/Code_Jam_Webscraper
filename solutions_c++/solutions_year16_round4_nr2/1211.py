#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t, kejs, i, j, n, r, s, p, N, K, m, m2;
double a[16], b[16], best, pa;

int main() {
        scanf("%d", &t);

        for (kejs = 1; kejs <= t; kejs++) {
                                                                printf("Case #%d: ", kejs);
                                                                best = 0;
                scanf("%d%d",&N, &K);
                                                                for (i = 0; i < N; i++) scanf("%lf", &a[i]);
                                                                for (m = 0; m < (1<<N); m++) {
                                                                        j = 0;
                                                                        for (i = 0; i < N; i++) if (m & (1<<i)) b[j++] = a[i];
                                                                        if (j == K) {
                                                                                pa = 0;
                                                                                for (m2 = 0; m2 < (1 << K); m2++) {
                                                                                        j = 0;
                                                                                        double p = 1;
                                                                                        for (i = 0; i < K; i++) {
                                                                                                if (m2 & (1 << i)) {
                                                                                                        j++;
                                                                                                        p *= b[i];
                                                                                                } else p *= (1-b[i]);
                                                                                        }
                                                                                        if (j == K / 2) pa += p;
                                                                                }
                                                                                if (best < pa) best = pa;
                                                                        }
                                                                }
                                                                printf("%.10lf\n", best);
        }
        return 0;
}
