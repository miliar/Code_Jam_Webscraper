#include <iostream>
#include <string>

using namespace std;

int main()
{
    int count;
    cin >> count;
    for (int c = 1; c <= count; ++c)
    {
        cout << "Case #" << c << ": ";

        int m, n;
        cin >> m >> n;

        int g[m][n];

        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                cin >> g[i][j];
            }
        }

        bool possible = true;

        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                bool has1 = false;
                bool has2 = false;

                for (int k = 0; k < m; ++k)
                    if (g[i][j] < g[k][j])
                        has1 = true;

                for (int k = 0; k < n; ++k)
                    if (g[i][j] < g[i][k])
                        has2 = true;

                if (has1 and has2)
                {
                    possible = false;
                    break;
                }
            }
            if (!possible) break;
        }

        if (possible)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}


