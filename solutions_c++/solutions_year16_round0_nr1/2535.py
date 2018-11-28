#include <stdio.h>

int main()
{
    int t, tt;
    scanf("%d", &t);

    for (tt = 1; tt <= t; ++ tt)
    {
        long long a;
        scanf("%lld", &a);
        long long b = a;

        if (a != 0)
        {
            int moo = 0;
            while (moo != 1023)
            {
                long long hru = a;
                while (hru)
                {
                    moo |= (1 << (hru % 10));
                    hru /= 10;
                }
                a += b;
            }

            printf("Case #%d: %lld\n", tt, a - b);
        }
        else
        {
            printf("Case #%d: INSOMNIA\n", tt);
        }
    }

    return 0;
}
