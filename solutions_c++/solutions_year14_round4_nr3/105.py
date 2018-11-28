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

#define x0 first0
#define y0 second0
#define x1 first1
#define y1 second1

const int N = 1005;

int f[N], d[N][N], v[N], x0[N], x1[N], y0[N], y1[N];

void work()
{
    int n, m, q;
    cin >> n >> m >> q;
    for (int i = 0; i < q; ++i)
        cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
    for (int i = 0; i < q; ++i)
    {
        for (int j = 0; j < q; ++j)
        {
            d[i][j] = 1;

            if (y1[i] < y0[j])
            {
                d[i][j] = max(d[i][j], y0[j] - y1[i]);
            }
            else if (y0[i] > y1[j])
            {
                d[i][j] = max(d[i][j], y0[i] - y1[j]);
            }

            if (x1[i] < x0[j])
            {
                d[i][j] = max(d[i][j], x0[j] - x1[i]);
            }
            else if (x0[i] > x1[j])
            {
                d[i][j] = max(d[i][j], x0[i] - x1[j]);
            }
            --d[i][j];
        }
        d[i][q] = d[q][i] = x0[i];
        d[i][q + 1] = d[q + 1][i] = n - x1[i] - 1;
    }
    d[q][q + 1] = d[q + 1][q] = n;
    q += 2;
    for (int i = 0; i < q; ++i)
    {
        f[i] = 1000000000;
        v[i] = 0;
    }
    f[q - 2] = 0;
    for (int i = 0; i < q; ++i)
    {
        int k = -1;
        for (int j = 0; j < q; ++j)
        {
            if (v[j]) continue;
            if (k == -1 || f[j] < f[k])
                k = j;
        }
        v[k] = 1;
        for (int j = 0; j < q; ++j)
            f[j] = min(f[j], f[k] + d[k][j]);
    }
    cout << f[q - 1] << endl;
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("c.in","r",stdin);
		freopen("c.out","w",stdout);
	#endif
	int task;
	cin >> task;
	for (int tt = 1; tt <= task; ++tt)
	{
	    cout << "Case #" << tt << ": ";
	    work();
	}
	return 0;
}
