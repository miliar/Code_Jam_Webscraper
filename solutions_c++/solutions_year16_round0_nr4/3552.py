#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t;
    scanf("%d", &t);
    int cs = 0;
    while (t--) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d: ", ++cs);
        if (k == 1) {
            printf("1\n");
        }
        else if (c == 1) {
            if (s == k) {
                for (int i = 1; i <= k; i++)
                    printf("%d ", i);
                printf("\n");
            }
            else {
                printf("IMPOSSIBLE\n");
            }
        }
        else {
            if (s < k-1)
                printf("IMPOSSIBLE");
            else {
                int i = 2, cnt = 0;
                while (cnt < k-1) {
                    printf("%d ", i++);
                    cnt++;
                }
                printf("\n");
            }
        }
    }
    return 0;
}
