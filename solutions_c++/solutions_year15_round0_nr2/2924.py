#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    int num[1005], tot[1005];
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int ans = 0, D, up = 0;
        scanf("%d", &D);
        for (int i = 0; i < 1005; i++)
            num[i] = 0;
        for (int i = 0; i < D; i++)
        {
            int x;
            scanf("%d", &x);
            num[x]++;
            up = max(up, x);
        }
        ans = up;
        for (int i = 2; i <= up; i++)
        {
            int tmp = i;
            for (int j = 0; j <= up; j++)
                tot[j] = num[j];
            for (int j = up; j > i; j--)
            {
                int now = (j - 1) / i;
                tmp += tot[j] * now;
            }
            ans = min(ans, tmp);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
