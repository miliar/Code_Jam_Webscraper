#include<cstdio>
#include <cstring>

int t, x;
bool viz[10];

bool ok(bool *v)
{
    for (int i = 0; i < 10; i++)
        if (!v[i])
            return false;
    return true;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    scanf("%d", &t);
    for (int index = 1; index <= t; index++)
    {
        scanf("%d", &x);
        int z = x;
        memset(viz, false, sizeof(viz));
        if (x == 0)
            {
                printf("Case #%d: INSOMNIA\n", index);
                continue;
            }
        while (!ok(viz))
        {
            int w = x;
            while (w)
                viz[w%10] = true, w/=10;
            x+= z;
        }
        printf("Case #%d: %d\n", index, x - z);
    }

    return 0;
}
