#include <iostream>
#include <cmath>
#include <string.h>

using namespace std;

int A[100][100];

void Solve(int t)
{
    cout << "Case #" << t << ": ";
    memset(A, 0, sizeof(A));
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> A[i][j];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
        {
            bool Vert = true, Horizont = true;
            for (int l = 0; l < n; ++l)
                if (A[l][j] > A[i][j])
                    Vert = false;
            for (int l = 0; l < m; ++l)
                if (A[i][l] > A[i][j])
                    Horizont = false;
            if (!Vert && !Horizont)
            {
                cout << "NO" << endl;
                return ;
            }
        }
    cout << "YES" << endl;
    return ;
}

int main()
{
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
        Solve(i + 1);
    return 0;
}
