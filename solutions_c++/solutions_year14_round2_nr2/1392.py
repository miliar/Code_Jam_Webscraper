#include<stdio.h>

int main()
{
    int t, a, b, k, x, y, i, j;
    scanf("%d", &t);
    for (x = 1; x <= t; x++) {
        scanf("%d %d %d", &a, &b, &k);
        y = 0;
        for (i = 0; i < a; i++) {
            for (j = 0; j < b; j++) {
                if( (i&j) < k )
                    y++;
            }
        }
        printf("Case #%d: %d\n", x, y);
    }
    return 0;
}
