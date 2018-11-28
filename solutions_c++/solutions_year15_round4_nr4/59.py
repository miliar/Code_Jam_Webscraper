#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

const int N = 10;
int f[N][N];
int n, m;
int result = 0;
set<string> ff;

string best()
{
    string s;
    forn(r, m)
    {
        string c;
        forn(i, n)
            forn(j, m)
                c += char('0' + f[i][(r + j) % m]);
        if (s == "")
            s = c;
        else
            s = min(s, c);                    
    }
    return s;
}

int cnt(int i, int j)
{
            int k = 0;
            forn(d, 4)
            {
                int ni = i + dx[d];
                int nj = (j + dy[d] + m) % m;
                if (ni >= 0 && ni < n)
                    if (f[i][j] == f[ni][nj])
                        k++;
            }
            return k;
}

int cntz(int i, int j)
{
            int k = 0;
            forn(d, 4)
            {
                int ni = i + dx[d];
                int nj = (j + dy[d] + m) % m;
                if (ni >= 0 && ni < n)
                    if (0 == f[ni][nj])
                        k++;
            }
            return k;
}

bool check()
{
    forn(i, n)
        forn(j, m)
        {
            if (cnt(i, j) != f[i][j])
                return false;
        }
    return true;
}

void rec(int x, int y)
{
    if (y >= m)
        y = 0, x++;

    if (x >= n)
    {
        if (check())
        {
            result++;
            /*
            forn(i, n)
            {
                forn(j, m)
                    cout << f[i][j];
                cout << endl;
            }
            cout << endl;
            */
            ff.insert(best());
        }
        return;
    }

    for (int a = 1; a <= 3; a++)
    {
        f[x][y] = a;

        int c = cnt(x, y);
        int cz = cntz(x, y);

        if (c <= f[x][y] && f[x][y] <= c + cz)
        {
            bool ok = true;
            forn(d, 4)
            {
                int nx = x + dx[d];
                int ny = (y + dy[d] + m) % m;
                if (nx >= 0 && nx < n && f[nx][ny] != 0)
                {
                    int c = cnt(nx, ny);
                    int cz = cntz(nx, ny);
                    if (!(c <= f[nx][ny] && f[nx][ny] <= c + cz))
                        ok = false;
                }
            }
            if (ok)
                rec(x, y + 1);
        }

        f[x][y] = 0;
    }
}

int solve()
{
    ff.clear();
    forn(i, N)
        forn(j, N)
            f[i][j] = 0;
    result = 0;
    rec(0, 0);
    // cout << result << endl;
    return ff.size();
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(test, tt)
    {
        cin >> n >> m;
        solve();

        cout << "Case #" << (test + 1) << ": " << solve() << endl;
    }

    return 0;
}
