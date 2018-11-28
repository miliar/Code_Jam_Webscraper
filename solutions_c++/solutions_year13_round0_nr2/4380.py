#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int solve() {
    int n, m;
    cin >> n >> m;
    int ar[100][100], res[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            cin >> ar[i][j];
            res[i][j] = 100;
        }
    for (int i = 0; i < n; i++) {
        int mi = 0;
        for (int j = 0; j < m; j++)
            mi = max(ar[i][j], mi);
        for (int j = 0; j < m; j++)
            res[i][j] = min(mi, res[i][j]);
    }

    for (int j = 0; j < m; j++) {
        int mi = 0;
        for (int i = 0; i < n; i++)
            mi = max(ar[i][j], mi);
        for (int i = 0; i < n; i++)
            res[i][j] = min(mi, res[i][j]);
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (ar[i][j] != res[i][j])
                return 0;
    return 1;

}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        int p = solve();
        if (p == 1)
            cout << "YES\n";
        else if (p == 0)
            cout << "NO\n";
    }
    return 0;
}
