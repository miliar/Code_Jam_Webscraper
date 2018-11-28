#include <stdio.h>
#include <stdlib.h>
#include <math.h>

long long pow(int k, int c)
{
    if (c == 0)
        return 1;
    long long x = pow(k, c/2);
    if (c%2 == 0)
        return x*x;
    else
        return x*x*k;
}

int main()
{
    int test, k, c, s;
    //freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d: ", t);
        if (c == 1)
        {
            if (s < k)
                printf("IMPOSSIBLE\n");
            else
            {
                for (int i = 1; i <= k; i++)
                    printf("%d ", i);
                printf("\n");
            }
            //continue;
        }
        else
        {
            if (c > k)
                c = k;
            if (s < (int)ceil(double(k)/c))
                printf("IMPOSSIBLE\n");
            else
            {
                long long offset = 0, lastg, ans = 0, loop = 0;
                long long group = (int)ceil(double(k)/c);
                for (int x = 1; x <= group; x++)
                {
                    lastg = c*x;
                    if (lastg > k)
                        lastg = k;
                    //ans = offset;
                    ans = 0;
                    for (int y = 0; y < c; y++)
                    {
                        loop++;
                        ans += offset * pow(k, c-1-y);
                        offset++;
                        if (loop >= k)
                            break;
                    }
                    ans++;
                    printf("%lld ", ans);
                    //offset += pow(k, c-1)*c;
                }
                printf("\n");
            }
        }
    }
    return 0;
}
