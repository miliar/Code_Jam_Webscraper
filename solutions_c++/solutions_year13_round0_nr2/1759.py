#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 110;

int n, m, T;
int grass[MAXN][MAXN];
bool ok = true;

int main() {
    scanf ("%d", &T);

    for (int cas = 1; cas <= T; cas++) {
        scanf ("%d %d", &n, &m);
        ok = true;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf ("%d", &grass[i][j]);

        for (int i = 0; ok && i < n; i++)
            for (int j = 0; ok && j < m; j++) {
                bool fl = true;
                for (int k = 0; k < m; k++)
                    if (grass[i][j] < grass[i][k])
                        fl = false;
                if (fl)
                    continue;
                fl = true;
                for (int k = 0; k < n; k++)
                    if (grass[i][j] < grass[k][j])
                        fl = false;
                if (fl)
                    continue;
                ok = false;
            }

        cout << "Case #" << cas << ": ";
        if (ok)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
