#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N, M;
int lawn[110][110];
int sosnooley[110][110];

int hmax[110];
int vmax[110];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T; cin >> T;

    for (int i = 0; i < T; ++i)
    {
        // Reading
        scanf("%d %d", &N, &M);
        for (int n = 0; n < N; ++n)
            for (int m = 0; m < M; ++m)
                scanf("%d", &lawn[n][m]);

        // Resetting
        for (int n = 0; n < N; ++n)
            for (int m = 0; m < M; ++m)
                sosnooley[n][m] = 0;

        for (int n = 0; n < N; ++n)
            hmax[n] = 0;

        for (int m = 0; m < M; ++m)
            vmax[m] = 0;

        // Solving
        printf("Case #%d: ", i + 1);

        // * Find maximums
        for (int n = 0; n < N; ++n)
            for (int m = 0; m < M; ++m)
                if ( lawn[n][m] > hmax[n] )
                    hmax[n] = lawn[n][m];

        for (int m = 0; m < M; ++m)
            for (int n = 0; n < N; ++n)
                if ( lawn[n][m] > vmax[m] )
                    vmax[m] = lawn[n][m];

        // * Make sure we didn't SOSNOOLEY
        for (int n = 0; n < N; ++n)
            for (int m = 0; m < M; ++m)
                if ( lawn[n][m] < hmax[n] )
                {
                    ++sosnooley[n][m];

                    if ( sosnooley[n][m] > 1 )
                    {
                        printf("NO\n");
                        goto next;
                    }
                }

        for (int m = 0; m < M; ++m)
            for (int n = 0; n < N; ++n)
                if ( lawn[n][m] < vmax[m] )
                {
                    ++sosnooley[n][m];

                    if ( sosnooley[n][m] > 1 )
                    {
                        printf("NO\n");
                        goto next;
                    }
                }


        printf("YES\n");

        next: ;
    }

    fclose(stdout);
    return 0;
}
