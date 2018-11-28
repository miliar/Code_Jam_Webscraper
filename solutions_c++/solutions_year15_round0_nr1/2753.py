#include<stdio.h>

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("out_A.txt", "w", stdout);

    int x, y, T, S, k, stand;
    char shy[2000];
    scanf("%d", &T);
    for (x = 1; x <= T; x++) {
        scanf("%d %s", &S, shy);
        stand = y = 0;
        for (k = 0; shy[k]; k++) {
            if (shy[k] != '0') {
                if (stand < k) {
                    y = k - stand;
                    stand += y;
                }
                stand += shy[k] - '0';
            }
        }
        printf("Case #%d: %d\n", x, y);
    }
    return 0;
}
