#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[128][128];
int row[128];
int column[128];

void solve () {

    static int testCase = 1;

    int n, m;
    scanf ("%d%d", &n, &m);

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            scanf ("%d", &a[i][j]);

    memset (row, -1, sizeof(row));
    memset (column, -1, sizeof(column));

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            row[i] = max (row[i], a[i][j]);
    }

    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; ++j)
            column[i] = max (column[i], a[j][i]);
    }

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (a[i][j] != row[i] && a[i][j] != column[j]) {
                printf ("Case #%d: NO\n", testCase++);
                return;
            }

    printf("Case #%d: YES\n", testCase);
    testCase ++;
}
int main () {

    int t;
    scanf ("%d", &t);
    for (; t; t--) solve();
return 0;
}
