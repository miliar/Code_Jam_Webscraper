# include <math.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define PN printf("\n")
# define PI 3.1415926536
# define MAXINT 0x7fffffff
# define GetMax(a, b) ((a)>(b)?(a):(b))
# define GetMin(a, b) ((a)<(b)?(a):(b))

# define MAXN 1009


int cmp(const void *a, const void *b)
{
    return (*(double *)a) > (*(double *)b) ? 1:-1;
}


int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t, n, cnt = 1, x, y;
    double test_naomi[MAXN], test_ken[MAXN];
    bool escape[MAXN];
    scanf("%d", &t);
    while(cnt <= t)
    {
        printf("Case #%d: ", cnt++);
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%lf", test_naomi+i);
        for(int j = 0; j < n; j++)
            scanf("%lf", test_ken+j);
        qsort(test_ken, n, sizeof(double), cmp);
        qsort(test_naomi, n, sizeof(double), cmp);
        memset(escape, false, sizeof(escape));
        x = y = 0;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(test_ken[j] > test_naomi[i] && !escape[j])
                {
                    y++;
                    escape[j] = true;
                    break;
                }
            }
        }
        memset(escape, false, sizeof(escape));
        for(int i = n-1; i >= 0; i--)
        {
            for(int j = n-1; j >= 0; j--)
            {
                if(test_ken[j] < test_naomi[i] && !escape[j])
                {
                    x++;
                    escape[j] = true;
                    break;
                }
            }
        }
        y = n - y;
        printf("%d %d\n",x, y);
    }
    return 0;
}
