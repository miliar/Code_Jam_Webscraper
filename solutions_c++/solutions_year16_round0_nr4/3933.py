#include<cstdio>

int main() {
    long long powers[100];
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d: ", i + 1);
        int question_count = k / c + (k % c > 0 ? 1 : 0);
        if (question_count > s) {
            printf("IMPOSSIBLE");
        } else {
            powers[0] = 1;
            for (int j = 1; j < c; ++j) {
                powers[j] = k * powers[j - 1];
            }
            for (int start = 0; start < k; start += c) {
                long long question = 1;
                for (int j = 0, limit = (k - start < c ? k - start : c); j < limit; ++j) {
                    question += powers[c - j - 1] * (start + j);
                }
                printf("%lld", question);
                if (start + c < k) {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
    return 0;
}
