#include <cstdio>

char s[1111];

int main() {
    int sum, i, fri, smax, T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d%s", &smax, s);
        sum = 0;
        fri = 0;
        for (i = 1; i <= smax; i++) {
            sum += s[i - 1] - '0';
            if (sum < i) {
                fri += i - sum;
                sum = i;
            }
        }
        printf("%d\n", fri);
    }
    return 0;
}
