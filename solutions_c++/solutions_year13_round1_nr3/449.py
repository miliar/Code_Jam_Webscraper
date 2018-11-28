#include <cstdio>
#include <cstdlib>
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    const int MAXK = 7, MAXN = 3;
    int t, i, r, n, m, k, j, p[MAXK], a[MAXN];
    scanf("%d", &t);
    for(i = 1; i <= t; i++)
    {
        scanf("%d%d%d%d", &r, &n, &m, &k);
        printf("Case #%d:\n", i);
        for(int l = 0; l < r; l++)
        {
            for(j = 0; j < k; j++)
                scanf("%d", &p[j]);
            while(1)
            {
                for(j = 0; j < n; j++)
                    a[j] = rand() % 4 + 2;
                for(j = 0; j < k; j++)
                    if(p[j] != 1 && a[0] * a[1] * a[2] != p[j] && a[0] != p[j] &&
                        a[1] != p[j] && a[2] != p[j] && a[0] * a[1] != p[j] &&
                        a[0] * a[2] != p[j] && a[1] * a[2] != p[j])
                            break;
                if(j == k)
                {
                    printf("%d%d%d\n", a[0], a[1], a[2]);
                    break;
                }
            }
        }
    }
    return 0;
}
