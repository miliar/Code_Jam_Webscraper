#include <cstdio>

int T[5][4];
bool chosen1[17], chosen2[17];

int main()
{
    int t, whichRow, res;
    bool found;

    scanf ("%d", &t);

    for (int test = 1; test <= t; test++)
    {
        scanf ("%d", &whichRow);

        for (int i=1; i<5; i++)
            for (int j=0; j<4; j++)
                scanf ("%d", &T[i][j]);

        for (int i=0; i<4; i++)
            chosen1[T[whichRow][i]] = 1;

        scanf ("%d", &whichRow);

        for (int i=1; i<5; i++)
            for (int j=0; j<4; j++)
                scanf ("%d", &T[i][j]);

        for (int i=0; i<4; i++)
            chosen2[T[whichRow][i]] = 1;

        found = 0;

        for (int i=1; i<17; i++)
        {
            if (!chosen1[i] or !chosen2[i])
                continue;

            if (!found)
            {
                found = 1;
                res = i;
            }

            else
                res = 0;
        }

        printf("Case #%d: ", test);

        if (!found)
            printf("Volunteer cheated!\n");

        else
            res == 0 ? printf("Bad magician!\n") : printf("%d\n", res);

        for (int i=1; i<17; i++)
            chosen1[i] = chosen2[i] = 0;
    }

    return 0;
}
