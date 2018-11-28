#include <cstdio>
using namespace std;

int main() {
    int T, R, N, M, K;
    int a[7], d[3];

    scanf("%d", &T);
    scanf("%d %d %d %d", &R, &N, &M, &K);
    printf("Case #1:\n");
    while (R--) {
        for (int i = 0; i < K; i++)
            scanf("%d", &a[i]);

        for (int i = 222; i <= 555; i++) {
            int n = i;
            for (int j = 0; j < 3; j++) {
                d[j] = n%10;
                n /= 10;
            }
            if (d[0] > M || d[1] > M || d[2] > M)
                continue;

            int cnt = 0;
            for (int j = 0; j < K; j++) {
                for (int k = 0; k < 8; k++) {
                    int prod = 1;
                    for (int l = 0; l < 3; l++)
                        if (k & 1<<l)
                            prod *= d[l];
                    if (prod == a[j]) {
                        cnt++;
                        break;
                    }
                }
            }

            if (cnt == K) {
                printf("%d\n", i);
                break;
            }
        }
    }
}
