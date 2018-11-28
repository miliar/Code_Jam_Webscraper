#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("a-large.in", "r", stdin);
    freopen("a-large.out", "w", stdout);

    int test;
    scanf("%i", &test);
    for(int t = 1; t <= test; t++)
    {
        int n;
        scanf("%i", &n);

        int res = 0, sum = 0;
        for(int i = 0; i <= n; i++)
        {
            char cnt;
            scanf(" %c", &cnt);
            cnt -= '0';

            res = max(res, i - sum);
            sum += cnt;
        }

        printf("Case #%i: %i\n", t, res);
    }

    return 0;
}
