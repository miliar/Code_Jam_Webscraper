# include <cstdio>

using namespace std;

int main ()
{
    freopen ("D-small-attempt0.in", "r", stdin);
    freopen ("output4.txt", "w", stdout);

    int t, t1, a, b, c, i;
    scanf ("%d", &t1);
    for (t = 1; t <= t1; t ++)
    {
        scanf ("%d%d%d", &a, &b, &c);
        printf ("Case #%d: ", t);
        if (a == c)
        {
            for (i = 1; i <= c; i ++)
                printf ("%d ", i);
        }
        printf ("\n");
    }
    return 0;
}
