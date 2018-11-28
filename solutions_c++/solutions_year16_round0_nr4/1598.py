#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int K, C, S;
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d: ", cas);
        if (C == 1)
        {
            if (S < K) puts("IMPOSSIBLE");
            else
            {
                for (int i = 0; i < K; i++)
                    printf("%d%c", i + 1, (i == K - 1)?'\n':' ');
            }
            continue;
        }
        int minS = (K + 1) / 2;
        if (S < minS) puts("IMPOSSIBLE");
        for (int i = 0; i < minS; i++)
            printf("%d%c", (i + 1) * K - i, (i == minS - 1)?'\n':' ');
    }
    return 0;
}
