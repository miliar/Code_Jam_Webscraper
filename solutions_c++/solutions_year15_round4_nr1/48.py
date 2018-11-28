#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int T, R, C, val[100][100];
bool chg[100][100];
string grid[100];

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> R >> C;
        for (int i = 0; i < R; ++i)
            cin >> grid[i];
        memset(val, 0, sizeof val);
        memset(chg, 0, sizeof chg);
        for (int i = 0; i < R; ++i)
        {
            for (int j = 0; j < C; ++j)
            if (grid[i][j] != '.')
            {
                if (grid[i][j] == '<')
                    chg[i][j] = true;
                ++val[i][j];
                break;
            }
            for (int j = C-1; j >= 0; --j)
            if (grid[i][j] != '.')
            {
                if (grid[i][j] == '>')
                    chg[i][j] = true;
                ++val[i][j];
                break;
            }
        }
        for (int j = 0; j < C; ++j)
        {
            for (int i = 0; i < R; ++i)
            if (grid[i][j] != '.')
            {
                if (grid[i][j] == '^')
                    chg[i][j] = true;
                ++val[i][j];
                break;
            }
            for (int i = R-1; i >= 0; --i)
            if (grid[i][j] != '.')
            {
                if (grid[i][j] == 'v')
                    chg[i][j] = true;
                ++val[i][j];
                break;
            }
        }
        int ans = 0;
        for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
        if (chg[i][j])
        {
            if (val[i][j] == 4)
                ans = MINF;
            else
                ++ans;
        }
        cout << "Case #" << z << ": ";
        if (ans < 0)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
}
