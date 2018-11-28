#include <iostream>
#include <cstdio>

using namespace std;

const int SZ = 200;

int a[SZ][SZ];
int str[SZ];
int col[SZ];

int cnt(int n, int m)
{

    for (int i = 0; i < n; i++)
    {
        str[i] = -1;
    }
    for (int j = 0; j < m; j++)
    {
        col[j] = -1;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            str[i] = max(str[i], a[i][j]);
            col[j] = max(col[j], a[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (str[i] > a[i][j] && col[j] > a[i][j])
            {
                return 0;
            }
        }
    }
    return 1;

}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n, m;
        cin >> n >> m;

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < m; k++)
            {
                cin >> a[j][k];
            }
        }
        int p = cnt(n, m);
        cout << "Case #" << i + 1 << ": ";
        if (p == 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
    }


    return 0;
}
