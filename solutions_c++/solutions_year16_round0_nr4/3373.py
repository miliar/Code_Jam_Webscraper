#include <cstdio>

int main()
{
    int tests;
    scanf ("%d", &tests);

    for (int t=1; t<=tests; t++)
    {
        int a, b, c;
        scanf ("%d%d%d", &a, &b, &c);

        printf("Case #%d: ", t);

        for (int i=1, pos=1; i<=a; i++, pos++)
        {
            printf("%d ", pos);

            if (b > 1)
                pos += a;
        }

        printf("\n");
    }

    return 0;
}
