# include <iostream>
# include <cstring>
# include <string>
# include <cstdio>
# include <vector>
# include <queue>
# include <map>
# include <algorithm>

using namespace std;

const int MAX_N = 128;

int n, m;

char c[MAX_N][MAX_N];

int aa[4] = {-1, 1, 0, 0};
int bb[4] = {0, 0, -1, 1};

char cc[4] = {'<', '>', 'v', '^'};

bool check (int i, int j)
{
    int p, q, cntc = 0, x, y;
    char pp = c[i][j];
    ///cout << i << " " << j << " " << c[i][j] << endl;
    for (q = 0; q < 4; q ++)
    {
            c[i][j] = cc[q];
            if (c[i][j] == '^')
                p = 0;
            if (c[i][j] == 'v')
                p = 1;
            if (c[i][j] == '<')
                p = 2;
            if (c[i][j] == '>')
                p = 3;
            x = i + aa[p];
            y = j + bb[p];
            ///cout << c[i][j] << " " << p << " " << x << " " << y << endl;
            while (x >= 0 && y >= 0 && x < n && y < m)
            {
                if (c[x][y] != '.')
                    break;
                x += aa[p];
                y += bb[p];
            }

            ///cout << c[i][j] << " " << p << " " << x << " " << y << endl;

            if (x >= 0 && y >= 0  && x < n && y < m)
                return false;
    }
    return true;
}

void solve ()
{
    int i, j, p, cnt = 0, x, y, lamp = 0;
    scanf ("%d%d", &n, &m);
    for (i = 0; i < n; i ++)
            scanf ("%s", &c[i]);

    for (i = 0; i < n; i ++)
    {
        for (j = 0; j < m; j ++)
        {
            if (c[i][j] == '.')
                continue;
            if (c[i][j] == '^')
                p = 0;
            if (c[i][j] == 'v')
                p = 1;
            if (c[i][j] == '<')
                p = 2;
            if (c[i][j] == '>')
                p = 3;
            x = i + aa[p];
            y = j + bb[p];
            while (x >= 0 && y >= 0  && x < n && y < m)
            {
                if (c[x][y] != '.')
                    break;
                x += aa[p];
                y += bb[p];
            }

            if (x >= 0 && y >= 0  && x < n && y < m)
                continue;
            if (check (i, j))
            {
                printf ("IMPOSSIBLE\n");
                lamp = 1;
                return ;
            }
            cnt ++;
        }
        if (lamp == 1)
            break;
    }
    printf ("%d\n", cnt);
}

int main ()
{
    int t, t1;
    scanf ("%d", &t);
    for (t1 = 1; t1 <= t; t1 ++)
    {
        printf ("Case #%d: ", t1);
        solve ();
    }
    return 0;
}
