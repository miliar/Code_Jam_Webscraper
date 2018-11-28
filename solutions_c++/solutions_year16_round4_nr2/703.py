#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
const int NMAX = 17;
int tests, N, K;
double A[NMAX], B[NMAX], result, best[NMAX][NMAX];

int cntBits(int mask) {
    return mask ? 1 + cntBits(mask & (mask - 1)) : 0;
}

double get() {
    memset(best, 0, sizeof(best));
    best[0][0] = 1.0;

    for (int i = 1; i <= K; i++) {
        for (int bf = 0; bf < i; bf++) {
            best[i][bf] += best[i - 1][bf] * (1.0 - B[i]);
            best[i][bf + 1] += best[i - 1][bf] * B[i];
        }
    }

    return best[K][K / 2];
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        printf("Case #%d: ", test);

        scanf("%d%d", &N, &K);
        for (int i = 1; i <= N; i++) {
            scanf("%lf", &A[i]);
        }

        result = 0.0;
        for (int mask = 0; mask < (1 << N); mask++) {
            if (cntBits(mask) == K) {
                int r = 0;
                for (int i = 1; i <= N; i++) {
                    if (mask & (1 << (i - 1))) {
                        B[++r] = A[i];
                    }
                }

                result = max(result, get());
            }
        }

        printf("%.10lf\n", result);
    }
    return 0;
}
