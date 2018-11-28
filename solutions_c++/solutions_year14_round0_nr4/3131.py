#include <stdio.h>
#include <stdlib.h>

int s(const void *a, const void *b)
{
    if(*(double*)a > *(double*)b) return 1;
    else if(*(double*)a < *(double*)b) return -1;
    else return 0;
}

main()
{
    int cases, t, n;
    int i, pa1, pa2, pb1, pb2, point;
    double a[1005], b[1005];
    scanf("%d", &cases);
    for(t=1; t<=cases; t++)
    {
        scanf("%d", &n);
        for(i=1; i<=n; i++) scanf("%lf", &a[i-1]);
        for(i=1; i<=n; i++) scanf("%lf", &b[i-1]);
        qsort(a, n, sizeof(double), s);
        qsort(b, n, sizeof(double), s);
        pa1 = pb1 = 0;
        pa2 = pb2 = n-1;
        printf("Case #%d: ", t);
        point = 0;
        for(i=1; i<=n; i++)
        {
            if(a[pa1] < b[pb1] || a[pa2] < b[pb2])
            {
                pa1++;
                pb2--;
            }
            else
            {
                pa1++;
                pb1++;
                point++;
            }
        }
        printf("%d", point);
        pa1 = pb1 = 0;
        pa2 = pb2 = n-1;
        point = 0;
        for(i=1; i<=n; i++)
        {
            if(a[pa2] > b[pb2])
            {
                pa2--;
                pb1++;
                point++;
            }
            else
            {
                pa2--;
                pb2--;
            }
        }
        printf(" %d\n", point);
    }
}
