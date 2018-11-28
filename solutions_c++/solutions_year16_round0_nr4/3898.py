#include <iostream>
#include <stdio.h>

using namespace std;
int k, c, s;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d:", cas);
        scanf("%d %d %d", &k, &c, &s);
        if (s < k)
        {
            printf(" IMPOSSIBLE\n");
            continue;
        }
        long long kc = 1;
        for (int i = 1; i < c; ++i)
        {
            kc *= s;
        }
        for (int i = 0; i < k; ++i)
        {
            printf(" %I64d", kc * i + 1);
        }
        printf("\n");
    }
    return 0;
}
