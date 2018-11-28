#include <stdio.h>

int t, sm;
int num[1010];
int cnt, ans;

int main()
{
    int tn, i;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d", &sm);
        for (i = 0; i <= sm; i++) scanf("%1d", &num[i]);
        cnt = ans = 0;
        for (i = 0; i <= sm; i++)
        {
            if (cnt < i)
            {
                ans += i-cnt;
                cnt = i;
            }
            cnt += num[i];
        }
        printf("Case #%d: ", tn);
        printf("%d\n", ans);
    }
}