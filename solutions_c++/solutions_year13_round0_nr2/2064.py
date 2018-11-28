#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;
const int MAXN = 110;

typedef struct grass
{
    int high;
    int x, y;
} grass;

int compare(grass k1, grass k2)
{
    return (k1.high < k2.high);
}

bool check(int lawn[][MAXN], int n, int m)
{
    grass a[MAXN * MAXN];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
        {
            a[i * m + j].high = lawn[i][j];
            a[i * m + j].x = i;
            a[i * m + j].y = j;
        }
    sort(a, a + n * m, compare);

    bool rowCut[MAXN * MAXN] = {false};
    bool colCut[MAXN * MAXN] = {false};
    for (int k = 0; k < n * m; ++k)
        if (!rowCut[a[k].x] && !colCut[a[k].y])
        {
            int x = a[k].x, y = a[k].y;
            //cout << x << " " << y << endl;
            int cut = 1;
            for (int j = 0; j < m; ++j)
                if (!rowCut[x] && !colCut[j])
                    if (lawn[x][j] != a[k].high)
                        cut = 0;
            if (cut)
            {
                rowCut[x] = true;
                //cout << "Cut row " << x << endl;
                continue;
            }

            cut = 1;
            for (int i = 0; i < n; ++i)
                if (!rowCut[i] && !colCut[y])
                    if (lawn[i][y] != a[k].high)
                        cut = 0;
            if (cut)
            {
                colCut[y] = true;
                //cout << "Cut column " << y << endl;
                continue;
            }

            return false;
        }
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("lawnmower.out", "w", stdout);
    int nTest;
    cin >> nTest;

    int lawn[MAXN][MAXN];
    for (int test = 1; test <= nTest; ++test)
    {
        int n = 0, m = 0;
        cin >> n >> m;

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> lawn[i][j];

        cout << "Case #" << test << ": " << ((check(lawn, n, m)) ? "YES" : "NO") << endl;
    }
    return 0;
}
