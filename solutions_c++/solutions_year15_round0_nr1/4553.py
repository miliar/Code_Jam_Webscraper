#include <bits/stdc++.h>

using namespace std;
int t, T, i, cnt, sol, smax;
char c;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &t);
    for(T = 1; T <= t; T++)
    {
        scanf("%d", &smax);
        scanf("%c", &c);
        scanf("%c", &c);
        sol = 0;
        cnt = int(c - '0');
        for(i = 1; i <= smax; i++)
        {
            scanf("%c", &c);
            if(i > cnt)
            {
                sol += i - cnt;
                cnt += i - cnt;
            }
            cnt += int(c - '0');
        }
        printf("Case #%d: %d\n", T, sol);
    }
    return 0;
}
