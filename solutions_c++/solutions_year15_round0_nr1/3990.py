#include <stdio.h>


char counter[1100];

int main()
{
    int T;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &T);

    for (int cn = 1; cn <= T; cn++) {
        int n;

        scanf("%d%s", &n, counter);

        int sum = 0;
        int ans = 0;

        for (int i = 0; i <= n; i++) {
            if (sum < i) {
                ans += i - sum;
                sum += i - sum;
                
            }
            sum += counter[i] - '0';
        }
        printf("Case #%d: %d\n", cn, ans);
        
    }
    return 0;
}
