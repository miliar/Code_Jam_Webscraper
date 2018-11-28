#include <stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++)
    {
        char s[1010];
        int n;
        scanf("%d%s", &n, s);
        int cur = s[0] - '0';
        int need = 0;
        for (int i = 1; i <= n; i++)
        {
            if (cur >= i)
            {
                cur += s[i] - '0';
            }
            else
            {
                if (s[i] > '0')
                {
                    need += i - cur;
                    cur = i + s[i] - '0';
                }
            }
        }
        printf("Case #%d: %d\n", cases, need);
    }
    return 0;
}
