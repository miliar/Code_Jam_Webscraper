#include <cstdio>

int T;
int N, M;
int m[101][101];
int maxr[101];
int maxc[101];



int main()
{
    freopen("lawn.in", "r", stdin);
    freopen("lawn.out", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++)
        {
            maxr[i] = 0;
        }

        for (int i = 0; i < M; i++)
        {
            maxc[i] = 0;
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                scanf("%d", &m[i][j]);
                if (m[i][j] > maxr[i])
                {
                    maxr[i] = m[i][j];
                }
                if (m[i][j] > maxc[j])
                {
                    maxc[j] = m[i][j];
                }
            }
        }
        /*
        for (int i = 0; i < N; i++)
        {
            printf("max on row %d: %d\n", i, maxr[i]);
        }

        for (int i = 0; i < M; i++)
        {
            printf("max on column %d: %d\n", i, maxc[i]);
        }
        */

        bool OK = true;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                // check if it's less or equal to
                // max of the row or of the column
                if ((m[i][j] < maxr[i]) && (m[i][j] < maxc[j]))
                {
                    OK = false;
                }
            }
        }
        if (OK)
        {
            printf("Case #%d: YES\n", t);
        }
        else
        {
            printf("Case #%d: NO\n", t);
        }
    }
    return 0;
}
