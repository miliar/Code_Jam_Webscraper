#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int n, m;
int a[111][111];
int h[111];
int v[111];

bool solve(){
    for (int i = 0; i < 111; i++) h[i] = v[i] = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) v[j] = max(v[j], a[i][j]), h[i] = max(h[i], a[i][j]);
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (a[i][j] < h[i] && a[i][j] < v[j]) return 0;
        }
    return 1;
}

int main()
{      
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        scanf ("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf ("%d", &a[i][j]);
        cout << "Case #" << tt << ": ";
        cout << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}

