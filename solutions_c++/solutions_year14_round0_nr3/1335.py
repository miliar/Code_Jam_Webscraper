#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int SZ = 100;

int a[SZ][SZ];
int used[SZ][SZ];

void fillrow(int r, int c, int &m)
{
    int t = 0;
    if (m == c - 1)
    {
        m--;
        t = 1;
    }
    for (int i = c - 1; i >= 0 && m; i--)
    {
        a[r][i] = 9;
        m--;
    }
    if (t)
    {
        m++;
    }
}

void fillcell(int r, int c, int &m)
{
    int t = 0;
    if (m == r - 1)
    {
        m--;
        t = 1;
    }
    for (int i = r - 1; i >= 0 && m; i--)
    {
        a[i][c] = 9;
        m--;
    }
    if (t)
    {
        m++;
    }
}

int getmine(int i, int j)
{
    if (i < 0 || j < 0)
    {
        return 0;
    }
    if (a[i][j] == 9)
    {
        return 1;
    }
    return 0;
}

void dfs(int i, int j, int r, int c)
{
    if (i < 0 || j < 0 || i >= r || j >= c)
    {
        return;
    }
    if (a[i][j] || used[i][j])
    {
        used[i][j] = 1;
        return;
    }

    used[i][j] = 1;

    dfs(i - 1, j - 1, r, c);
    dfs(i - 1, j, r, c);
    dfs(i - 1, j + 1, r, c);
    dfs(i, j - 1, r, c);
    dfs(i, j + 1, r, c);
    dfs(i + 1, j - 1, r, c);
    dfs(i + 1, j, r, c);
    dfs(i + 1, j + 1, r, c);

}

void calc(int r, int c, int m)
{
    if (m == r * c - 1)
    {
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                if (i == 0 && j == 0)
                {
                    cout << 'c';
                }
                else
                {
                    cout << '*';
                }
            }
            cout << endl;
        }
        return;
    }

    memset(a, 0, sizeof(a));
    memset(used, 0, sizeof(used));
    int R = r;
    int C = c;

    while (m)
    {
        if (R >= C)
        {
            fillrow(--R, C, m);
        }
        else
        {
            fillcell(R, --C, m);
        }
    }
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (a[i][j] != 9)
            {
                int k = 0;
                k += getmine(i - 1, j - 1);
                k += getmine(i - 1, j);
                k += getmine(i - 1, j + 1);
                k += getmine(i, j - 1);
                k += getmine(i, j + 1);
                k += getmine(i + 1, j - 1);
                k += getmine(i + 1, j);
                k += getmine(i + 1, j + 1);
                a[i][j] = k;
            }
        }
    }

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (a[i][j] == 0)
            {
                dfs(i, j, r, c);
            }
        }
    }

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (a[i][j] != 9 && used[i][j] == 0)
            {
                cout << "Impossible" << endl;
                return;
            }
        }
    }
    int tp = 0;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (a[i][j] == 9)
            {
                cout << '*';
            }
            else
            {
                if (tp == 0 && a[i][j] == 0)
                {
                    cout << 'c';
                    tp = 1;
                }
                else
                {
                    cout << '.';
                }
            }
        }
        cout << endl;
    }

}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int r, c, m;
        cin >> r >> c >> m;
        cout << "Case #" << i + 1 << ":" << endl;
        calc(r, c, m);
    }
    return 0;
}
