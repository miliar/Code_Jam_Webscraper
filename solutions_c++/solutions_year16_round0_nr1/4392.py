# include <cstdio>

using namespace std;

int used[12];

int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("output1.txt", "w", stdout);

    int t, t1, i, cnt, x, n;
    scanf ("%d", &t1);
    for (t = 1; t <= t1; t ++)
    {
        for (i = 0; i < 10; i ++)
            used[i] = 0;
        cnt = 0;
        scanf ("%d", &n);
        printf ("Case #%d: ", t);
        if (!n)
        {
            printf ("INSOMNIA\n");
            continue;
        }
        for (i = 1; i <= 100; i ++)
        {
            x = i * n;

            while (x)
            {
                if (!used[x % 10])
                    cnt ++;
                used[x % 10] = 1;
                x /= 10;
            }
            if (cnt == 10)
            {
                printf ("%d\n", i * n);
                break;
            }
        }
    }

    return 0;
}
