# include <cstdio>
# include <cstring>

using namespace std;

int n;
char c[128];

int main ()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("output3.txt", "w", stdout);

    int t, t1, i, ans, len;
    char side;
    scanf ("%d", &t1);
    for (t = 1; t <= t1; t ++)
    {
        scanf ("%s", c);
        n = strlen (c);
        ans = 0;
        len = 0;
        side = c[len];
        for (i = 1; i < n; i ++)
        {
            if (side != c[i])
            {
                ans ++;
                side = c[i];
            }
        }
        if (side == '-')
            ans ++;
        printf ("Case #%d: %d\n", t, ans);
    }
    return 0;
}
