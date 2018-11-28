#include <stdio.h>

int t, t0;

int d, a[1010];

int main()
{
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        int i, x, c;
        int minc = 1000000000;
        scanf("%d", &d);
        for(i = 0; i < d; i++)
            scanf("%d", &a[i]);
        for(x = 1; x <= 1000; x++){
            c = x;
            for(i = 0; i < d; i++)
                c += (a[i] - 1) / x;
            if (minc > c)
                minc = c;
            }
            printf("Case #%d: %d\n", t0 + 1, minc);
        }

    return 0;
}
