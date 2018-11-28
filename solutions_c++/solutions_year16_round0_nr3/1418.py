#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T, N, J;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", cas);
        N = (N - 4) >> 1;
        for (int i = 0; i < J; i++)
        {
            printf("11");
            for (int j = 0; j < N; j++)
                if ((i >> j) & 1) printf("11");
                else              printf("00");
            printf("11 ");
            for (int j = 2; j <= 10; j++)
                printf("%d%c", j + 1, (j == 10)?'\n':' ');
        }
    }
    return 0;
}
