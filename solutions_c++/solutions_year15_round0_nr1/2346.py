#include<cstdio>

using namespace std;

int T, Smax, ap[100009];

bool ok (int val)
{
    int curr_sum = ap[0] + val;

    for (int i=1; i<=Smax; i++)
        if (ap[i])
        {
            if (curr_sum >= i)
                curr_sum += ap[i];
            else
                return 0;
        }

    return 1;
}

int main ()
{
//freopen ("input", "r", stdin);
//freopen ("output", "w", stdout);

int test = 0;
scanf ("%d", &T);
while (T)
{
    printf ("Case #%d: ", ++test);
    T --;

    scanf ("\n%d ", &Smax);
    for (int i=0; i<=Smax; i++)
    {
        char curr;
        scanf ("%c", &curr);
        ap[i] = curr - '0';
    }

    int p, u, mij, ras;
    p = 0;
    u = Smax + 10;
    while (p <= u)
    {
        mij = (p + u) >> 1;
        if (ok (mij))
            ras = mij, u = mij - 1;
        else
            p = mij + 1;
    }

    printf ("%d\n", ras);

    for (int i=0; i<=Smax; i++)
        ap[i] = 0;
}

return 0;
}
