#include <iostream>
#include <stdio.h>

using namespace std;

int vert[100], gor[100];
int a[100][100];

bool solution(int n, int m) {
    bool ans = true;
    for(int i = 0; i < n; i++) {
        vert[i] = 0;
        for(int j = 0; j < m; j++)
            cin >> a[i][j];
    }
    for(int i = 0; i < m; i++)
        gor[i] = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            vert[i] = max(vert[i], a[i][j]);
            gor[j] = max(gor[j], a[i][j]);
        }
    }
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            ans = ans && (a[i][j] == vert[i] || a[i][j] == gor[j]);
    return ans;
}

int main()
{
    int t, n, m;
    freopen("input.in", "r", stdin);
    freopen("output.in", "w", stdout);
    cin >> t;
    for(int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        cin >> n >> m;
        if(solution(n, m))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
