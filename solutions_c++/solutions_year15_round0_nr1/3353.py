#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("a-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);

    int T, m;
    char s[1024];
    scanf("%d", &T);
    for (int c = 1; c <= T; ++c)
    {
        scanf("%d %s", &m, &s);
        int sum = 0, ans = 0;
        for (int i = 0; i <= m; ++i)
        {
            int cnt = (int)(s[i] - '0');
            if (cnt > 0)
            {
                if (sum < i)
                {
                    ans += i - sum;
                    sum = i;
                }
                sum += cnt;
            }
        }
        printf("Case #%d: %d\n", c, ans);
    }

    fclose(stdout);
    return 0;
}
