#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <cassert>
#include <queue>
#include <sstream>
#include <set>
#include <functional>
#include <cfloat>
#include <unordered_map>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef complex<double> cd;
#define mp make_pair                                                  

const ll MN = 21000;
const ll mod = 1e9 + 7;


bool check(int x, int y, vector<string>& b, int dx, int dy)
{
    x += dx;
    y += dy;
    while (x >= 0 && x < b.size() && y >= 0 && y < b[0].size())
    {
        if (b[x][y] != '.')
            return true;
        x += dx;
        y += dy;
    }
    return false;
}

void solve()
{
    int r, c;
    cin >> r >> c;
    vector<string> b(r);
    for (int i = 0; i < r; ++i)
        cin >> b[i];
    int ans = 0;
    for (int i = 0; i < r; ++i)
    {
        for (int j = 0; j < c; ++j)
        {
            bool ok = false;
            if (b[i][j] == '.')
                continue;
            if (b[i][j] == '^')
                ok = check(i, j, b, -1, 0);
            if (b[i][j] == 'v')
                ok = check(i, j, b, 1, 0);
            if (b[i][j] == '<')
                ok = check(i, j, b, 0, -1);
            if (b[i][j] == '>')
                ok = check(i, j, b, 0, 1);
            if (!ok)
                ++ans;
            if (!check(i, j, b, -1, 0) &&
                !check(i, j, b, 1, 0) &&
                !check(i, j, b, 0, -1) &&
                !check(i, j, b, 0, 1))
            {
                cout << "IMPOSSIBLE";
                return;
            }
        }
    }
    cout << ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}