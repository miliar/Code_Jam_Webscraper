#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d:", nc);
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        for (int i = 1; i <= s; i++)
        {
            printf(" %d", i);
        }
        printf("\n");
    }
}
