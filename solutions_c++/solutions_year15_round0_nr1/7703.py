#include <cstdio>

const int maxN = 1000;

char W[maxN + 2];

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        int n;
        scanf ("%d", &n);

        scanf ("%s", W);

        int standingCtr = 0, res = 0;

        for (int i=0; i<=n; i++)
        {
            if (standingCtr < i)
            {
                res += (i - standingCtr);
                standingCtr = i;
            }

            standingCtr += (W[i] - '0');
        }

        printf("Case #%d: %d\n", test, res);
    }

    return 0;
}
