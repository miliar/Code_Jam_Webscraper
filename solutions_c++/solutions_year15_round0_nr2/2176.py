#include <iostream>
#include <stdio.h>

using namespace std;
int T, d, p[1009];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d", &d);
        int pmax = 0;
        for (int i = 1; i <= d; ++i)
        {
            scanf("%d", &p[i]);
            pmax = max(pmax, p[i]);
        }
        int ans = 1009;
        for (int i = 1; i <= pmax; ++i)
        {
            int tmp = 0;
            for (int j = 1; j <= d; ++j)
            {
                tmp += p[j] / i;
                if (p[j] % i == 0) tmp--;
            }
            tmp += i;
            ans = min(ans, tmp);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
