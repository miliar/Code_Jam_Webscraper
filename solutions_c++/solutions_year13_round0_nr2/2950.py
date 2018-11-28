#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int T;
int N, M;

int lawn[105][105];
bool good[105][105];

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    cin >> T;

    for (int cas = 1; cas <= T; cas++)
    {
        memset(good, false, sizeof(good));
        cin >> N >> M;

        for (int i = 0; i < N; i++)
        {
            int maxxy = 0;
            for (int j = 0; j < M; j++)
            {
                cin >> lawn[i][j];
                maxxy = max(maxxy, lawn[i][j]);
            }
            for (int j = 0; j < M; j++)
            {
                if (lawn[i][j] == maxxy)
                {
                    good[i][j] = true;
                }
            }
        }

        for (int j = 0; j < M; j++)
        {
            int maxxy = 0;
            for (int i = 0; i < N; i++)
            {
                maxxy = max(maxxy, lawn[i][j]);
            }
            for (int i = 0; i < N; i++)
            {
                if (lawn[i][j] == maxxy)
                {
                    good[i][j] = true;
                }
            }
        }

        bool yes = true;

        for (int i = 0; i < N && yes; i++)
        {
            for (int j = 0; j < M && yes; j++)
            {
                if (good[i][j] == false)
                {
                    yes = false;
                }
            }
        }
        if (yes)
        {
            printf("Case #%d: YES\n", cas);
        }else
        {
            printf("Case #%d: NO\n", cas);
        }



    }

    return 0;
}
