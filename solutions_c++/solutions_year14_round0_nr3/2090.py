#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <deque>
#include <stack>
#include <string>
#include <ctime>
#include <list>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <queue>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

#define mp make_pair
#define pb push_back

#define _USE_MATH_DEFINES
#define pi M_PI

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <vector<int> > graph;

int dx[8] = {1, 1, 1, 0, -1, -1, -1, 0};
int dy[8] = {1, 0, -1, -1, -1, 0, 1, 1};
int n, m, c;

bool good(int x, int y)
{
    return x >= 0 && y >= 0 && x < n && y < m;
}

bool OK;

void check(vector <vector <int> > V)
{
    if (!OK)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (V[i][j] == 0)
                {
                    queue <pair <int, int> > Q;
                    vector <vector <bool> > B(n, vector <bool> (m, 0));
                    Q.push(mp(i, j));
                    B[i][j] = 1;
                    while (!Q.empty())
                    {
                        pair <int, int> p = Q.front();
                        Q.pop();
                        int tm = 0;
                        for (int q = 0; q < 8; q++)
                        {
                            int tx = p.first + dx[q];
                            int ty = p.second + dy[q];
                            if (good(tx, ty) && V[tx][ty])
                                tm++;
                        }
                        if (!tm)
                        {
                            for (int q = 0; q < 8; q++)
                            {
                                int tx = p.first + dx[q];
                                int ty = p.second + dy[q];
                                if (good(tx, ty) && !B[tx][ty])
                                {
                                    Q.push(mp(tx, ty));
                                    B[tx][ty] = 1;
                                }
                            }
                        }
                    }
                    bool ok = 1;
                    for (int ii = 0; ii < n; ii++)
                    {
                        for (int jj = 0; jj < m; jj++)
                        {
                            if (V[ii][jj] == 0 && B[ii][jj] == 0)
                                ok = 0;
                        }
                    }
                    if (ok)
                    {
                        OK = ok;
                        for (int ii = 0; ii < n; ii++)
                        {
                            for (int jj = 0; jj < m; jj++)
                            {
                                if (V[ii][jj])
                                    cout << '*';
                                else if (ii == i && jj == j)
                                    cout << 'c';
                                else
                                    cout << '.';
                            }
                            cout << endl;
                        }
                        return;
                    }
                }
            }
        }
    }
}

void gen(int x, int y, int k, vector <vector <int> > & V)
{
//    cerr << x << " " << y << endl;
    if (OK)
        return;
    if (!k)
    {
        check(V);
        return;
    }
    if (x == n)
        return;
    int tx = x, ty = y + 1;
    if (ty == m)
    {
        tx = x + 1;
        ty = 0;
    }
    V[x][y] = 0;
    gen(tx, ty, k, V);
    V[x][y] = 1;
    gen(tx, ty, k - 1, V);
    V[x][y] = 0;

}

int main()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int q = 0; q < T; q++)
    {
        cerr << "Test # " << q + 1 << endl;
        cout << "Case #" << q + 1 << ":\n";
        cin >> n >> m >> c;

        OK = 0;
        vector <vector <int> > V(n, vector <int> (m, 0));
        gen(0, 0, c, V);
        if (!OK)
            cout << "Impossible" << endl;

    }

    return 0;
}
