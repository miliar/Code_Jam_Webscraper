#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    int s, c, k;

    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d:", t);
        scanf("%d %d %d", &k, &c, &s);
        if (s >= k)
        {
            for(int i = 1; i <= k; ++i)
                printf(" %d", i);
        }
        else
            printf("IMPOSSIBLE");
        printf("\n");
    }

    return 0;
}
