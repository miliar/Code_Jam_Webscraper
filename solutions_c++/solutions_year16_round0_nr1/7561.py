#include <cstdio>
#include <algorithm>
#include <bitset>

#define f first
#define s second
#define pb push_back

using namespace std;

int main ()
{
    freopen ("file.in", "r", stdin);
    freopen ("file.out", "w", stdout);

    int t;
    scanf ("%d", &t);

    for (int h = 1; h <= t; ++h)
    {
        printf ("Case #%d: ", h);

        long long n;
        scanf ("%lld", &n);

        bitset <16> ap;
        int nr = 0;

        if (n == 0LL)
        {
            printf ("INSOMNIA\n");
            continue;
        }

        long long cn = n, nn = n;
        while (cn)
        {
            int x = (int)(cn % 10LL);
            cn /= 10LL;

            if (!ap[x]) ++nr, ap[x] = 1;
        }

        while (nr < 10)
        {
            n += 1LL * nn;

            long long cn = n;
            while (cn)
            {
                int x = (int)(cn % 10LL);
                cn /= 10LL;

                if (!ap[x]) ++nr, ap[x] = 1;
            }
        }

        printf ("%lld\n", n);
    }

    return 0;
}
