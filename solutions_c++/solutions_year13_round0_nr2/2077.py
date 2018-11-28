#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

#define LOCAL_EXEC 1


int
main ()
{
#if (LOCAL_EXEC == 1)
    freopen("D:\\Input.txt", "r", stdin);
    freopen("D:\\Output.txt", "w", stdout);
#endif

    int T;
    cin >> T;

    int lawn[100][100];
    int MaxRow[100];
    int MaxCol[100];

    for (int i = 1; i <= T; ++i)
    {
        int N, M;
        cin >> N >> M;

        for (int j = 0; j < N; ++j)
        {
            MaxRow[j] = 0;
            for (int k = 0; k < M; ++k)
            {
                cin >> lawn[j][k];

                MaxRow[j] = max(MaxRow[j], lawn[j][k]);
                if (j == 0)
                {
                    MaxCol[k] = lawn[j][k];
                }
                else
                {
                    MaxCol[k] = max(MaxCol[k], lawn[j][k]);
                }
            }
        }

        bool possible = true;

        for (int j = 0; j < N && possible; ++j)
        {
            for (int k = 0; k < M && possible; ++k)
            {
                if (lawn[j][k] != MaxRow[j] && lawn[j][k] != MaxCol[k])
                {
                    possible = false;
                }
            }
        }

        if (possible)
        {
            cout << "Case #" << i << ": YES" << endl;
        }
        else
        {
            cout << "Case #" << i << ": NO" << endl;
        }
    }

    return 0;
}
