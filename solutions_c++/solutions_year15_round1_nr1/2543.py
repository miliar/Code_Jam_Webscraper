#include <stdio.h>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("Answer 1 Large", "w", stdout);

    int t, n;
    scanf("%d", &t);

    for(int j = 1; j <= t; j++) {
        scanf("%d", &n);
        int a[n], b[n - 1], ans1 = 0, ans2 = 0, max = 0;

        for(int i = 0; i < n; i++)
            scanf("%d", &a[i]);

        for(int i = 1; i < n; i++) {
            b[i - 1] = a[i - 1] - a[i];
            if(b[i - 1] > 0)
                ans1 += b[i - 1];
            if(b[i - 1] > max)
                max = b[i - 1];
        }

        for(int i = 0; i < n - 1; i++) {
            if(a[i] > max)
                ans2 += max;
            else
                ans2 += a[i];
        }

        printf("Case #%d: %d %d\n", j, ans1, ans2);
    }

    return 0;
}
