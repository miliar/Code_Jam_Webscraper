#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int t, n, m, a[101][101], b[101][101], c = 1,x,y;
bool used[1001];

int main()
{
    freopen("tx.in", "r", stdin);
    freopen("tx.out", "w", stdout);
    cin >> t;
    while (t--)
    {
        cin >> n;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                cin >> a[i][j];
        cin >> m;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j<= 4; j++)
                cin >> b[i][j];
        for (int i = 1; i <= 4; i++)
            used[a[n][i]] = 1;
        for (int i = 1; i <= 4; i++)
            if (used[b[m][i]]) x++, y = b[m][i];
        if (!x)
            cout << "Case #" << c << ": Volunteer cheated!" << endl;
        else if (x > 1)
            cout << "Case #" << c << ": Bad magician!" << endl;
        else
            cout << "Case #" << c << ": " << y << endl;
        c++, x = 0;
        for (int i = 1; i <= 16; i++)
            used[i] = 0;
    }

    return 0;
}
