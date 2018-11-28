#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 200;

int a[MAX][MAX], m, n;
bool avail[MAX][MAX];

bool Check()
{
    memset(avail, true, sizeof avail);
    while (true)
    {
        int minA = 101;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (avail[i][j]) minA = min(minA, a[i][j]);

        bool stop = false;
        for (int i = 0; i < m && !stop; ++i)
        {
            int ok = -1;
            for (int j = 0; j < n; ++j)
                if (avail[i][j])
                    ok = (ok < 0 ? (a[i][j] == minA) : ok & (a[i][j] == minA));
            if (ok == 1)
            {
                for (int j = 0; j < n; ++j) avail[i][j] = false;
                stop = true;
            }
        }
        for (int j = 0; j < n && !stop; ++j)
        {
            int ok = -1;
            for (int i = 0; i < m; ++i)
                if (avail[i][j])
                    ok = (ok < 0 ? (a[i][j] == minA) : ok & (a[i][j] == minA));
            if (ok == 1)
            {
                for (int i = 0; i < m; ++i) avail[i][j] = false;
                stop = true;
            }
        }

        if (!stop) return (minA > 100);
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; ++t)
    {
        scanf("%d%d", &m, &n);
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                scanf("%d", &a[i][j]);

        printf("Case #%d: %s", t, Check() ? "YES" : "NO");
        if (t < nTests) printf("\n");
    }
}