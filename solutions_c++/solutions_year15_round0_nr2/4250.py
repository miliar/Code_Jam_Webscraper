#include <stdio.h>

int t;
int d, p[1010];
int cnt, ans;

int main()
{
    freopen("/Users/IohcEjnim/Desktop/MyData/Informatics/Sources/TEMP/TEMP/B-large.in", "r", stdin);
    freopen("/Users/IohcEjnim/Desktop/MyData/Informatics/Sources/TEMP/TEMP/Result.out", "w", stdout);
    int tn, i, j;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d", &d);
        for (i = 1; i <= d; i++) scanf("%d", &p[i]);
        ans = 0x3fffffff;
        for (i = 1; i <= 1000; i++)
        {
            cnt = 0;
            for (j = 1; j <= d; j++) cnt += (p[j]-1)/i;
            if (cnt+i < ans) ans = cnt+i;
        }
        printf("Case #%d: ", tn);
        printf("%d\n", ans);
    }
}