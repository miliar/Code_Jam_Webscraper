#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[5][5];
int p[20];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;

    for (int T = 0; T < t; T++)
    {
        memset(p, 0, sizeof(p));
        int k;
        cin >> k;

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin >> a[i][j];
            }
        }
        k--;
        for (int i = 0; i < 4; i++)
        {
            p[a[k][i]]++;
        }

        int ans = -1;
        int bad = 0;

        cin >> k;

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin >> a[i][j];
            }
        }
        k--;
        for (int i = 0; i < 4; i++)
        {
            p[a[k][i]]++;
            if (p[a[k][i]] == 2)
            {
                if (ans == -1)
                {
                    ans = a[k][i];
                }
                else
                {
                    bad = 1;
                }
            }
        }

        if (bad)
        {
            cout << "Case #" << T + 1 << ": " << "Bad magician!" << endl;
        }
        else if (ans == -1)
        {
            cout << "Case #" << T + 1 << ": " << "Volunteer cheated!" << endl;
        }
        else
        {
            cout << "Case #" << T + 1 << ": " << ans << endl;
        }


    }


    return 0;
}
