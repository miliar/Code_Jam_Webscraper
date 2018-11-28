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

string f[1000];

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
string D = "v>^<";

bool good(int n, int m, int a, int b, int d)
{
    while (true)
    {
        a += dx[d];
        b += dy[d];
        if (!(a >= 0 && a < n && b >= 0 && b < m))
            return false;
        if (f[a][b] != '.')
            return true;
    }

    return false;
}

bool good(int n, int m, int a, int b)
{
    return good(n, m, a, b, D.find(f[a][b]));
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(test, tt)
    {
        int n, m;
        cin >> n >> m;
        forn(i, n)
            cin >> f[i];

        int result = 0;
        forn(i, n)
            forn(j, m)
                if (f[i][j] != '.')
                {
                    if (!good(n, m, i, j))
                    {
                        bool ok = false;
                        forn(d, 4)
                            if (good(n, m, i, j, d))
                            {
                                ok = true;
                                result++;
                                break;
                            }
                        if (!ok)
                        {
                            result = INT_MAX;
                            goto end;
                        }
                    }                                        
                }
end:
        if (result > INT_MAX / 2)
            cout << "Case #" << (test + 1) << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << (test + 1) << ": " << (result == INT_MAX ? -1 : result) << endl;
    }

    return 0;
}
