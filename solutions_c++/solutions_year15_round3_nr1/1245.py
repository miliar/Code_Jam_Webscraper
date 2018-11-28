#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1.out", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, R, C, W;
    int cas = 1, ans = 0;
    scanf("%d", &T);

    while (T --)
    {
        ans = 0;
        scanf("%d %d %d", &R, &C, &W);

        ans = (R - 1) * (C / W );
        ans += (C / W + (C % W > 0) + W - 1);

        printf("Case #%d: %d\n", cas ++, ans);
    }

    return 0;
}
