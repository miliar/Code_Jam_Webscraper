#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

char c[150][150];
int l[150][150], r[150][150], u[150][150], d[150][150];
int n, m;

void solve()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> c[i][j];
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < m; j++)
            if (c[i][j] != '.'){
                int x = i, y = j-1;
                while (y >= 0 && c[x][y] == '.') y--;
                l[i][j] = y;
                x = i-1, y = j;
                while (x >= 0 && c[x][y] == '.') x--;
                u[i][j] = x;
                x = i, y = j+1;
                while (y < m && c[x][y] == '.') y++;
                if (y == m) y = -1;
                r[i][j] = y;
                x = i+1, y = j;
                while (x < n && c[x][y] == '.')x++;
                if (x == n) x = -1;
                d[i][j] = x;

                if (l[i][j] == -1 && r[i][j] == -1 && u[i][j] == -1 && d[i][j] == -1){
                    cout << "IMPOSSIBLE\n";
                    return;
                }
            }
    int res = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++){
            if (c[i][j] != '.') {
                if (c[i][j] == '<' && l[i][j] == -1) res++;
                if (c[i][j] == '^' && u[i][j] == -1) res++;
                if (c[i][j] == '>' && r[i][j] == -1) res++;
                if (c[i][j] == 'v' && d[i][j] == -1) res++;
            }
        }
    cout << res << endl;
}

int main()
{      
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
