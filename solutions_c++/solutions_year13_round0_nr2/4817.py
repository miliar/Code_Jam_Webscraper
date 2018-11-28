#include <iostream>

using namespace std;

int main()
{
    int T, N, M;
    cin >> T;
    int height = 100;
    int piece;
    bool results[T];
    bool cut;
    for (int i = 0; i < T; i++)
    {
        cin >> N;
        cin >> M;
        int current[N][M];
        int goal[N][M];
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                cin >> piece;
                goal[j][k] = piece;
            }
        }

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
                current[j][k] = height;
        }

        for (int j = (height - 1); j > 0; j--)
        {
            for (int k = 0; k < N; k++)
            {
                cut = true;
                for (int l = 0; l < M; l++)
                {
                    piece = goal[k][l];
                    if (piece > j)
                        cut = false;
                }

                if (cut)
                {
                    for (int l = 0; l < M; l++)
                        current[k][l] = j;
                }
            }
            for (int k = 0; k < M; k++)
            {
                cut = true;
                for (int l = 0; l < N; l++)
                {
                    piece = goal[l][k];
                    if (piece > j)
                        cut = false;
                }

                if (cut)
                {
                    for (int l = 0; l < N; l++)
                        current[l][k] = j;
                }
            }
        }

        results[i] = true;
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                if (current[j][k] != goal[j][k])
                    results[i] = false;
            }
        }
    }

    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << (1 + i) << ": ";
        if (results[i])
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
