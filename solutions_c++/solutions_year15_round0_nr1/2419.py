#include <stdio.h>

int testsCnt;
char s[1010];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &testsCnt);
    for (int testN = 1; testN <= testsCnt; testN++) {
        scanf("%*d %s", s);
        int sum = 0, res = 0;
        for (int i = 0; s[i]; i++) {
            if (sum < i) {
                res += i - sum;
                sum = i;
            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", testN, res);
    }
}