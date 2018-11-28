#include <cstdio>
#include <algorithm>
using namespace std;

int pts(double *A, double *B, int n) {
    int res = 0, bi = n - 1;
    for (int ai = n - 1; ai >= 0; ai--) {
        while (bi >= 0 && B[bi] > A[ai]) bi--;
        if (bi-- == -1) break;
        res++;
    }
    return res;
}

int n;
double N[1005], K[1005];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%lf", N + i);
        for (int i = 0; i < n; i++) scanf("%lf", K + i);
        sort(N, N + n);
        sort(K, K + n);
        printf("Case #%d: %d %d\n", t, pts(N, K, n), n - pts(K, N, n));
    }
    return 0;
}
