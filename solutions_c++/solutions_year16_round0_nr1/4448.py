#include <cstdio>

bool vis[10];
int vis_ctr;

void check(int n)
{
    while (n > 0)
    {
        if (!vis[n % 10])
            vis_ctr++;

        vis[n % 10] = 1;
        n /= 10;
    }
}

int main()
{
    int tests;
    scanf ("%d", &tests);

    for (int t=1; t<=tests; t++)
    {
        int n;
        scanf ("%d", &n);

        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        int v;
        for (v=n; vis_ctr<10; v+=n)
            check(v);

        printf("Case #%d: %d\n", t, v - n);

        vis_ctr = 0;

        for (int i=0; i<10; i++)
            vis[i] = 0;
    }

    return 0;
}
