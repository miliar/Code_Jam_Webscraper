#include <cstdio>
#include <algorithm>
#include <cstring>

#define f first
#define s second
#define pb push_back

using namespace std;

char str[128];

int main ()
{
    freopen ("file.in", "r", stdin);
    freopen ("file.out", "w", stdout);

    int t;
    scanf ("%d\n", &t);

    for (int h = 1; h <= t; ++h)
    {
        gets (str);

        int n = strlen (str);
        int nrm = 0;

        for (int i = 0; i < n; ++i)
            if (str[i] == '-') ++nrm;

        int moves = 0;
        while (nrm)
        {
            int poz = 0;

            ++moves;
            if (str[0] == '-')
                while (poz < n && str[poz] == '-')
                    str[poz++] = '+', --nrm;

            else
                while (poz < n && str[poz] == '+')
                    str[poz++] = '-', ++nrm;
        }

        printf ("Case #%d: %d\n", h, moves);
    }

    return 0;
}
