#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, S_max;
    char str[1010];

    int cas = 1;
    int ans = 0;
    int sum = 0;
    scanf("%d", &T);

    while (T --)
    {
        ans = sum = 0;
        scanf("%d %s", &S_max, str);

        for (int i = 0; i <= S_max; i ++)
        {
            if (str[i] - '0' > 0 &&  sum < i )
            {
                ans += (i - sum);
                sum = i;
            }
            sum += (str[i] - '0');
        }

        printf("Case #%d: %d\n", cas ++, ans);
    }

    return 0;
}
