#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int n;
    cin >> n;
    int a[4][4], b[4][4];
    for (int i = 0; i < n; i++)
    {
        int m, l;
        cin >> m;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> a[j][k];
        cin >> l;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> b[j][k];
        int ans = -1;
        for (int k = 0; k < 4; k++)
        for (int j = 0; j < 4; j++)
        {
            if (a[m - 1][k] == b[l - 1][j] && ans == -1)
                ans = a[m - 1][k];
            else
                if (a[m - 1][k] == b[l - 1][j] && ans != -1)
                    ans = -2;
        }
        cout << "Case #" << i + 1 << ": ";
        if (ans == -1)
            cout << "Volunteer cheated!" << endl;
        if (ans == -2)
            cout << "Bad magician!" << endl;
        if (ans > -1)
            cout << ans << endl;
    }
}
