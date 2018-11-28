#include <cstdio>
#include <algorithm>

double A[1000], B[1000];

int main()
{
    int t, n, optDicWar, optWar;

    scanf ("%d", &t);

    for (int test = 1; test <= t; test++)
    {
        scanf ("%d", &n);

        for (int i=0; i<n; i++)
            scanf ("%lf", &A[i]);

        std::sort(A, A + n);

        for (int i=0; i<n; i++)
            scanf ("%lf", &B[i]);

        std::sort (B, B + n);

        optDicWar = optWar = 0;

        for (int i=0, j=0; i<n and j<n; i++, j++)    //  i - Bit, j - Ait;
        {
            while (j < n and A[j] < B[i])
                j++;

            if (j < n)
                optDicWar++;
        }

        for (int i=0, j=0; i<n and j<n; i++, j++)    //  i - Ait, j - Bit;
        {
            while (j < n and B[j] < A[i])
                j++, optWar++;
        }

        printf("Case #%d: %d %d\n", test, optDicWar, optWar);
    }
}
