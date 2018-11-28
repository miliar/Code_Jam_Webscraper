#include <bits/stdc++.h>

using namespace std;
int t, T, r, c, w, sol;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &t);
    for(T = 1; T <= t; T++)
    {
        scanf("%d%d%d", &r, &c, &w);
        if(w == c)
        {
            printf("Case #%d: %d\n", T, w);
            continue;
        }
        if(2 * w >= c)
        {
            printf("Case #%d: %d\n", T, w + 1);
            continue;
        }
        if(w == 1)
        {
            printf("Case #%d: %d\n", T, c);
            continue;
        }
        sol = c / w+(c%w==0?0:1);
        sol += (w - 1);
        printf("Case #%d: %d\n", T, sol);

    }
    return 0;
}
