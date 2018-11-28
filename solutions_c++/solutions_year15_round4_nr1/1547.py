#include <iostream>
#include <cstdio>
using namespace std;

void cans(int test, int ans)
{
    cout << "Case #" << test << ": " << ans << endl;
}

int r, c;
bool inrc(int y, int x)
{
    return (x < c && x >= 0 && y < r && y >= 0);
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        bool imp = false;
        int ans = 0;
        char g[105][105];
        bool visited[105][105] = {false};
        cin >> r >> c;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                cin >> g[i][j];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
            {
               //cout <<i << " " <<
          //      cout << endl << endl;
                if (!visited[i][j] && g[i][j] != '.')
                {

                    int x = j;
                    int y = i;
                    int cnt = 0;
                    do
                    {
                        cnt++;
                        visited[y][x] = true;
                        int vx, vy;
                        if (g[y][x] == '^')
                            vx = 0, vy = -1;
                        if (g[y][x] == 'v')
                            vx = 0, vy = 1;
                        if (g[y][x] == '<')
                            vx = -1, vy = 0;
                        if (g[y][x] == '>')
                            vx = 1, vy = 0;
                        do
                        {
                            x += vx; y += vy;
                        } while (inrc(y,x) && g[y][x] == '.');
                    //    cout << x << " " << y << endl;
                    } while (inrc(y, x) && !visited[y][x]);
                    if (!inrc(y,x))
                    {
                        //cout << i << " " << j << endl;
                        ans++;
                        if (cnt == 1)
                        {
                            bool flag = false;
                            for (int ii = i + 1; ii < r; ii++)
                                if (g[ii][j] != '.') flag = true;
                            for (int ii = i - 1; ii >= 0; ii--)
                                if (g[ii][j] != '.') flag = true;
                            for (int jj = j + 1; jj < c; jj++)
                                if (g[i][jj] != '.') flag = true;
                            for (int jj = j - 1; jj >= 0; jj--)
                                if (g[i][jj] != '.') flag = true;

                            if (!flag) imp = true;
                        }
                    }
                }
            }

        if (imp) cout << "Case #" << tt << ": Impossible" << endl;
        else cans(tt, ans);

    }

}
