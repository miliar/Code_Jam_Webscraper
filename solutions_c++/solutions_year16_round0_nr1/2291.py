#include<cstdio>

using namespace std;

int N;

int main ()
{
freopen ("input", "r", stdin);
freopen ("output", "w", stdout);

int Tests;
scanf ("%d", &Tests);
for (int test_id = 1; test_id <= Tests; test_id ++)
{
    printf ("Case #%d: ", test_id);
    scanf ("%d", &N);
    if (N == 0)
    {
        printf ("INSOMNIA\n");
        continue;
    }
    int msk = 0;
    for (int i=1;; i++)
    {
        long long aux = 1LL * N * i;
        while (aux) msk |= 1 << (aux % 10), aux /= 10;
        if (msk == 1023)
        {
            printf ("%lld\n", 1LL * N * i);
            break;
        }
    }
}

return 0;
}
