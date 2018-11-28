#include <cstdio>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int main()
{

    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1.out", "w", stdout);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, cas = 1;
    int D;
    int p[1010];
    int ans;

    scanf("%d", &T);

    while (T --)
    {
        scanf("%d", &D);

        int max_p = 1;
        for (int i = 0; i < D; i ++)
        {
            scanf("%d", &p[i]);
            if (p[i] > max_p)
                max_p = p[i];
        }

        ans = max_p;
        for (int i = 2; i <= max_p; i ++)
        {
            int sum = 0;
            for (int j = 0; j < D; j ++)
            {
                sum += ( (p[j] - 1 ) / i );
            }
            sum += i;
            if (ans > sum)
                ans = sum;
        }

        printf("Case #%d: %d\n", cas ++, ans);
    }
    return 0;
}

/*
3
1
3
4
1 2 1 2
1
4
*/
