#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T, n;
    char str[1005];
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int ans = 0, bef = 0, cur = 0;
        scanf("%d %s", &n, str);
        for (int i = 0; i <= n; i++)
        {
            cur = str[i] - '0';
            if ((bef < i) && (cur != 0))
            {
                ans += i - bef;
                bef += i - bef;
            }
            bef += cur;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
