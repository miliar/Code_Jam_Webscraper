#include <iostream>
using namespace std;

int matrix[105][105];
int row_left_max[105][105];
int row_right_max[105][105];
int col_up_max[105][105];
int col_down_max[105][105];

inline int max(int a, int b)
{
    return a > b ? a : b;
}

int main ()
{
    int kase, ncase = 0;
    int N, M;
    bool flag;
    int rowMax, colMax;

    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    scanf("%d", &kase);
    while (kase--)
    {
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                scanf("%d", &matrix[i][j]);
            }
        }

        for (int i = 0; i < N; ++i)
        {
            row_left_max[i][0] = 0;
            for (int j = 1; j < M; ++j)
            {
                row_left_max[i][j] = max(row_left_max[i][j-1], matrix[i][j-1]);
            }
        }

        for (int i = 0; i < N; ++i)
        {
            row_right_max[i][M-1] = 0;
            for (int j = M - 2; j >= 0; --j)
            {
                row_right_max[i][j] = max(row_right_max[i][j+1], matrix[i][j+1]);
            }
        }

        for (int i = 0; i < M; ++i)
        {
            col_up_max[0][i] = 0;
            for (int j = 1; j < N; ++j)
            {
                col_up_max[j][i] = max(col_up_max[j-1][i], matrix[j-1][i]);
            }
        }

        for (int i = 0; i < M; ++i)
        {
            col_down_max[N - 1][i] = 0;
            for (int j = N - 2; j >= 0; --j)
            {
                col_down_max[j][i] = max(col_down_max[j+1][i], matrix[j+1][i]);
            }
        }

        flag = true;
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < M; ++j)
            {
                rowMax = max(row_left_max[i][j], row_right_max[i][j]);
                colMax = max(col_up_max[i][j], col_down_max[i][j]);
                if (matrix[i][j] < rowMax && matrix[i][j] < colMax)
                {
                    flag = false;
                }
            }

            if (!flag)
                break;
        }

        if (flag)
        {
            printf("Case #%d: YES\n", ++ncase);
        }
        else
        {
            printf("Case #%d: NO\n", ++ncase);
        }
    }

    return 0;
}
