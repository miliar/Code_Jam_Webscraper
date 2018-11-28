#include <stdio.h>
#include <stdlib.h>
#define debug(...) (void)0
bool possible(int r, int c, int m)
{
    int t;
    if (r > c)
    {
        t = r;
        r = c;
        c = t;
    }
    if (r == 1)
    {
        return true;
    }
    if (r == 2)
    {
        debug("m=%d\n", m);
        if (m == 1 || (m >= 4 && m % 2 == 0))
            return true;
        else
            return false;
    }
    if (r >= 3)
    {
        if (m >= r * r)
            return true;
        else
            return possible(r - 1, r - 1, m);
    }
    return false;
}

int solve2(int *p, int r, int c, int m)
{
    if (m >= r * r)
    {
        for (int i = 0; i < c; i++)
            for (int j = 0; j < r; j++)
            {
                if (i * r + j < m)
                {
                    debug("x=%d\n", j * c + i);
                    fflush(stdout);
                    p[j * c + i] = '.';

                }
            }
        int n = m / r;
        int l = m % r;
        if (l == 1)
        {
            debug("y=%d\n", (r - 1) * c + n - 1);
            debug("z=%d\n", l * c + n);
            fflush(stdout);
            p[(r - 1) * c + n - 1] = '*';
            p[l * c + n] = '.';
        }

    }
    else
    {
        int x = 1;
        for (x = 1; x <= m; x++)
        {
            if (x * x > m)
                break;
        }
        x--;
        debug("x=%d\n", x);
        fflush(stdout);
        for (int i = 0; i < x; i++)
            for (int j = 0; j < x; j++)
                p[i * c + j] = '.';
        int n = m - x * x;

        if (n == 1)
        {
            p[x] = '.';
            p[c + x] = '.';
            debug("www=%d\n", (x - 1) * c + (x - 1));
            fflush(stdout);
            p[(x - 1) * c + (x - 1)] = '*';

        }
        else if (n <= x)
        {
            for (int k = 0; k < n; k++)
            {
                p[k * c + x] = '.';
            }
        }
        else
        {
            for (int k = 0; k < x; k++)
            {
                p[x * c + k] = '.';
            }
            n = n - x;

            if (n == 1)
            {
                p[x] = '.';
                p[c + x] = '.';
                p[x * c + (x - 1)] = '*';
            }
            else
            {
                for (int k = 0; k < n; k++)
                {
                    p[k * c + x] = '.';
                }

            }
        }
    }

    return 0;
}

int solve(int r, int c, int m)
{
    int a[r * c];
    int i, j;
    debug("call solve!\n");
    for (i = 0; i < r * c; i++)
    {
        debug("write\n");
        fflush(stdout);
        a[i] = '*';
    }
    debug("wrote!\n");
    fflush(stdout);
    if (r <= c)
    {
        debug("call solve2\n");
        fflush(stdout);
        solve2(a, r, c, r * c - m);
        debug("solve2 return\n");
        fflush(stdout);
    }
    else
    {
        debug("call solve2\n");
        fflush(stdout);
        solve2(a, c, r, r * c - m);
        debug("solve2 return\n");
        fflush(stdout);
    }
    a[0] = 'c';
    for(int xxx= 0; xxx < r * c; xxx ++) {
        //printf("%c ", a[xxx]);
    }
    //printf("\n");
    if (r <= c)
    {
        for (i = 0; i < r; i++)
        {
            for (j = 0; j < c; j++)
            {
                printf("%c", a[i * c + j]);
            }
            printf("\n");
        }
    }
    else
    {
        for (i = 0; i < r; i++)
        {
            for (j = 0; j < c; j++)
                printf("%c", a[j * r + i]);
            printf("\n");
        }
    }
    return 0;

}

int cal(int i, int r, int c, int m)
{
    printf("Case #%d:\n", i);
    //printf("%d %d %d\n", r, c, m);
    if (possible(r, c, r * c - m))
    {
        solve(r, c, m);
    }
    else
    {
        printf("Impossible\n");
    }
    return 0;
}

int main()
{
    int t;
    scanf("%d", &t);
    debug("%d\n", t);
    for (int i = 1; i <= t; i++)
    {
        int r, c, m;
        scanf("%d%d%d", &r, &c, &m);
        debug("%d %d %d\n", r, c, m);
        cal(i, r, c, m);
    }
    return 0;
}
