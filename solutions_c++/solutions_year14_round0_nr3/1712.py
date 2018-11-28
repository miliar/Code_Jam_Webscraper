#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <ctime>
#include <sstream>
#include <fstream>
#include <bitset>
#include <iomanip>
#include <cassert>

using namespace std;

typedef long long int64;

#define mp make_pair
#define PII pair<int, int>
#define pb push_back
#define sz(X) ((int)((X).size()))

#define x first
#define y second

const double eps = 1e-8;
const int p[] = {0,0,0,-1,-1,-1,1,1,1};
const int q[] = {0,-1,1,-1,0,1,-1,0,1};

const int N = 55;

int v[N][N], vv[N][N], num[N][N], n, m, M;
int ans;

void dfs(int state, int i, int j)
{
    if (v[i][j] == 0) return;
    v[i][j] = 0;
    ++ans;
    int tmp = 0;
    for (int k = 1; k < 9; ++k)
    {
        int x = i + p[k];
        int y = j + q[k];
        if (!vv[x][y]) continue;
        if (state & (1 << num[x][y])) ++tmp;
    }
    if (tmp) return;
    for (int k = 1; k < 9; ++k)
    {
        int x = i + p[k];
        int y = j + q[k];
        if (!vv[x][y]) continue;
        dfs(state, x, y);
    }
}

bool check(int state, int p, int q)
{
    for (int i = 0; i <= n + 1; ++i)
        for (int j = 0; j <= m + 1; ++j)
            v[i][j] = 0, vv[i][j] = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
        {
            v[i][j] = 1;
            vv[i][j] = 1;
            if (state & (1 << num[i][j]))
                v[i][j] = 0;
        }
    ans = M;
    dfs(state, p, q);
    return ans == n * m;
}

void work()
{
    cin >> n >> m >> M;
    int ed = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            num[i][j] = ed++;
    for (int state = 0; state < (1 << (n * m)); ++state)
    {
        int cnt = 0;
        for (int i = 0; i < n * m; ++i)
            if (state & (1 << i)) ++cnt;
        if (cnt != M) continue;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                if ((state & (1 << num[i][j])) == 0)
                    if (check(state, i, j))
                    {
                        for (int p = 1; p <= n; ++p)
                        {
                            for (int q = 1; q <= m; ++q)
                            {
                                if (state & (1 << num[p][q]))
                                    cout << '*';
                                else if (p == i && q == j)
                                    cout << 'c';
                                else
                                    cout << '.';
                            }
                            cout << endl;
                        }
                        return;
                    }
    }
    cout << "Impossible" << endl;
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("c.in","r",stdin);
		freopen("c.out","w",stdout);
	#endif
	int task;
	cin >> task;
	for (int i = 1; i <= task; ++i)
	{
	    cerr << i << endl;
	    cout << "Case #" << i << ":" << endl;
	    work();
	}
	return 0;
}
