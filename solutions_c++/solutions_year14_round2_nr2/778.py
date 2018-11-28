#include <cstdlib>
#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int A, B, K;
        scanf("%d %d %d", &A, &B, &K);
        int res = 0;
        for (int a = 0; a < A; a++) {
            for (int b = 0; b < B; b++) {
                if ((a&b) < K) res++;
            }
        }
        printf("Case #%d: %d\n", t+1, res);
    }

    return 0;
}
