#include <stdio.h>

int main() {
    int t;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int n;
        scanf("%d ", &n);
        char c;
        int curr = 0;
        int ans = 0;
        for (int i = 0; i <= n; ++i) {
            scanf("%c", &c);
//            printf("%c\n", c);
            int num = c - '0';
            if (curr < i) {
                ans += i - curr;
                curr = i + num;
            } else {
                curr += num;
            }
        }
        scanf("\n");
        printf("Case #%d: %d\n", cs, ans);
    }
    return 0;
}
