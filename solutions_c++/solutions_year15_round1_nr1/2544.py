#include <stdio.h>

int t, n;
int c[1010];
int a, b, max;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("result.out", "w", stdout);
    int i, tn;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d", &n);
        for (i = 1; i <= n; i++) scanf("%d", &c[i]);
        a = b = max = 0;
        for (i = 1; i < n; i++)
            if (c[i] > c[i+1])
            {
                a += c[i]-c[i+1];
                if (c[i]-c[i+1] > max) max = c[i]-c[i+1];
            }
        for (i = 1; i < n; i++)
        {
            if (c[i] < max) b += c[i];
            else b += max;
        }
        printf("Case #%d: %d %d\n", tn, a, b);
    }
}