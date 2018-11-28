#include<stdio.h>

char s[100000];
int a[100000];
int main()
{
    int t, n, i, tt;
    scanf("%d", &t);
    for(tt = 1; tt <= t; tt ++)
    {
        scanf("%d", &n);
        scanf("%s", s);
        for(i = 0; i <= n; i++)
        {
            a[i] = s[i] - '0';
        }
        int ans = 0, st = 0;
        for(i = 0; i <= n; i++)
        {
            if(st < i)
            {
                ans += i - st;
                st += i - st;
                //printf("Ans = %d, i = %d st = %d\n",ans, i, st);
            }
            st += a[i];
        }

        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
