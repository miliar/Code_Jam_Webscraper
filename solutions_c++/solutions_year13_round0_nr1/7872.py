#include <iostream>
#include <string.h>
using namespace std;
const int size = 4;
char Map[size][size];
bool used[size][size];
void get_map ()
{
    for (int i = 0; i < size; ++i)
    {
        for (int j = 0; j < size; ++j)
        {
            cin >> Map[i][j];
        }
    }
}

int dfs (int x, int y, int v, int dx, int dy, int deep)
{
    if (deep == size) return true;
    if (x + dx < size && x + dx > -1 && y + dy < size && y + dy > -1 && (Map[x + dx][y + dy] == v || Map[x + dx][y + dy] == 'T'))
    {
        return dfs (x + dx, y + dy, v, dx, dy, deep + 1);
    }
    return false;
}

bool check_win (char v)
{
    bool res = false;
    if (Map[0][0] == v || Map[0][0] == 'T') res = res || dfs (0, 0, v, 1, 0, 1) || dfs (0, 0, v, 1, 1, 1) || dfs (0, 0, v, 0, 1, 1);
    if ((Map[1][0] == v || Map[1][0] == 'T') && !res) res = res || dfs (1, 0, v, 0, 1, 1);
    if ((Map[2][0] == v || Map[2][0] == 'T')&& !res) res = res || dfs (2, 0, v, 0, 1, 1);
    if ((Map[3][0] == v || Map[3][0] == 'T')&& !res) res = res || dfs (3, 0, v, 0, 1, 1) || dfs (3, 0, v, -1, 1, 1);
    if ((Map[0][1] == v || Map[0][1] == 'T') && !res) res = res || dfs (0, 1, v, 1, 0, 1);
    if ((Map[0][2] == v || Map[0][2] == 'T')&& !res) res = res || dfs (0, 2, v, 1, 0, 1);
    if ((Map[0][3] == v  || Map[0][3] == 'T')&& !res) res = res || dfs (0, 3, v, 1, 0, 1);
    return res;
}
bool check_full ()
{
    for (int i = 0; i < size; ++i)
    {
        for (int j = 0; j < size; ++j)
        {
            if (Map[i][j] == '.') return false;
        }
    }
    return true;
}
void resolve ()
{
    if (check_win('X'))
    {
        cout << "X won" << endl;
    }
    else if (check_win('O'))
    {
        cout << "O won" << endl;
    }
    else if (check_full())
    {
        cout << "Draw" << endl;
    }
    else
    {
        cout << "Game has not completed" << endl;
    }
}
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        get_map();
        cout << "Case #" << i + 1 << ": ";
        resolve();
    }
    return 0;
}
