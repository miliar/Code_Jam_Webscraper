#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int res[511][511];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin >> t;
    printf("Case #1:\n");

    int n, k;
    cin >> n >> k;

    int cnt = 0;

    int maxValue = (1 << min(n - 1, 20)) - 1;

    for (int i = 1; i < maxValue; i += 2)
    {
        int g = (1 << (n - 1)) + i;

        bool ok;
        int div;
        for (int j = 2; j <= 10; j++)
        {
            ok = false;
            for (int t = 2; t <= 100; t++)
            {
                int x = 0;
                int s = 1;
                for (int p = 0; p < n; p++)
                {
                    if ((g & (1 << p)) > 0) x = (x + s) % t;
                    s = (s * j) % t;
                }

                if (x == 0)
                {
                    res[cnt + 1][j] = t;
                    ok = true;
                    break;
                }
            }

            if (!ok) break;
        }

        if (ok)
        {
            cnt++;
            res[cnt][1] = g;
        }

        if (cnt == k) break;
    }

    for (int i = 1; i <= k; i++)
    {
        int p = res[i][1];
        for (int j = n - 1; j >= 0; j--)
        {
            int x = ((p & (1 << j)) > 0);
            printf("%d", x);
        }

        for (int j = 2; j <= 10; j++)
            printf(" %d", res[i][j]);

        printf("\n");
    }
}
