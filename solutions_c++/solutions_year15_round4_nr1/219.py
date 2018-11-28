#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-8;

const int N = 205;

const int dx[] = {-1,0,0,1};
const int dy[] = {0,1,-1,0};

int a[N][N], out[N][N];

bool go(int i, int j, int k)
{
    while (1)
    {
        i += dx[k];
        j += dy[k];
        if (out[i][j]) return false;
        if (a[i][j] != 4) return true;
    }
}

void work()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i <= n + 1; ++i)
        for (int j = 0; j <= m + 1; ++j)
            out[i][j] = 1;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
        {
            out[i][j] = 0;
            char x;
            cin >> x;
            if (x == '^') a[i][j] = 0;
            else if (x == '>') a[i][j] = 1;
            else if (x == '<') a[i][j] = 2;
            else if (x == 'v') a[i][j] = 3;
            else if (x == '.') a[i][j] = 4;
            else assert(false);
        }
    int ans = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (a[i][j] != 4 && !go(i, j, a[i][j]))
            {
                ++ans;
                bool bad = true;
                for (int k = 0; k < 4; ++k)
                    if (go(i, j, k))
                        bad = false;
                if (bad)
                    ans = -100000000;
            }
    if (ans < 0)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << ans << endl;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//    ios_base::sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        work();
    }
}
