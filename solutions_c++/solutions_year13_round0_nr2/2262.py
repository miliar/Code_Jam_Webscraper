#include <iostream>

using namespace std;

int mCol[110], mRow[110];
int table[110][110];
int main()
{
    int t;
    cin >> t;
    for (int tt = 0; tt < t; tt++)
    {
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            mRow[i] = 0;
        for (int i = 0; i < m; i++)
            mCol[i] = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
            {
                cin >> table[i][j];
                mCol[j] = max(mCol[j], table[i][j]);
                mRow[i] = max(mRow[i], table[i][j]);
            }
        bool good = true;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                good &= (table[i][j] == mCol[j] || table[i][j] == mRow[i]);
        cout << "Case #" << tt + 1 << ": ";
        if (good)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;

    }
}
