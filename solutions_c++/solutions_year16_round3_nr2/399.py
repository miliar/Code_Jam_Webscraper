/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 55;
typedef unsigned long long ull;

int A[MAXN][MAXN];

void zeroizeMatrix(int B)
{
    for (int i = 1; i <= B; i++)
    {
        for (int j = 1; j <= B; j++)
            A[i][j] = 0;
    }
}

void fillMatrix(int from, int to)
{
    for (int i = from; i <= to; i++)
    {
        for (int j = i + 1; j <= to; j++)
            A[i][j] = 1;
    }
}

void printMatrix(int B)
{
    for (int i = 1; i <= B; i++)
    {
        for (int j = 1; j <= B; j++)
        {
            cout << A[i][j];
        }
        cout << endl;
    }
}

int main()
{
    freopen("inputB.in", "r", stdin);
    freopen("outputB.out", "w", stdout);

    int _T;
    cin >> _T;

    for (int _t = 1; _t <= _T; _t++)
    {
        ull B, M;
        cin >> B >> M;
        ull maxWays = (ull)1 << (B - 2);
        string verdict = (M <= maxWays ? "POSSIBLE" : "IMPOSSIBLE");
        cout << "Case #" << _t << ": " << verdict << endl;

        if (verdict == "IMPOSSIBLE")
        {
            continue;
        }

        zeroizeMatrix(B);

        if (M != maxWays)
        {
            fillMatrix(2, B);
            int i = 2;
            ull ways = (ull)1 << (B - 3);

            while(M != 0)
            {
                if (ways <= M)
                {
                    A[1][i] = 1;
                    M -= ways;
                }
                i++;
                ways /= 2;
            }
        }
        else
        {
            fillMatrix(1, B);
        }

        printMatrix(B);
    }

    return 0;
}
