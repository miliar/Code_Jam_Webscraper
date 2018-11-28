#include <stdio.h>
#include <string.h>
#include <math.h>

bool test(int n)
{
    int ct = 0;
    int a[10];
    while (n)
    {
        a[ct++] = n % 10;
        n /= 10;
    }
    int i;
    for (i = 0;i < ct;i++)
    {
        if (a[i] != a[ct - 1 - i])
            return 0;
    }
    return 1;
}

bool ok(int n)
{
    int t = sqrt(n);
    if ( t * t != n)
        return 0;
    if (test(n) && test(t))
        return 1;
    return 0;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k;
    int t,ct;
    scanf("%d", &t);
    int a,b;
    for (k = 1;k <= t;k++)
    {
        scanf("%d%d", &a, &b);
        printf("Case #%d: ", k);
        ct = 0;
        for (i = a;i <= b;i++)
        {
            if (ok(i))
                ct++;
        }
        printf("%d\n", ct);
    }
    return 0;
}
