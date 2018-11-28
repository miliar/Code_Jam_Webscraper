#include <cstdio>

int main(int argc, char * argv[]) {
    int TC, c = 0, A, B, K, i, j, result;
    bool overflow;
    scanf("%d", &TC);
    while(TC--) {
        result = 0;
        overflow = false;
        scanf("%d %d %d", &A, &B, &K);
        result = A + B - 1;

        if (A < K && B < K) {
            result = A * B;
        } else {
            if (A < B) {
                A ^= B;
                B ^= A;
                A ^= B;
            }
            result = K * B;
            for (i = K; i < A; i++) {
                for (j = 0; j < B; j++) {
                    if ((i & j) < K) {
                        result++;
                    }
                }
            }
        }

        printf("Case #%d: %d\n", ++c, result);
    }

    return 0;
}