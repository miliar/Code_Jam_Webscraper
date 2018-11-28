#include <bits/stdc++.h>
using namespace std;

const int N = 105;

int marker[N], matrix[N][N], wall[5][N], cons[5][N][N];
map<char, int> _map;

void init() {
    fill(marker, marker + N, 0);
    for (int i = 0; i < N; i++) {
        fill(matrix[i], matrix[i] + N, 0);
    }

    for (int i = 0; i < 5; i++) {
        fill(wall[i], wall[i] + N, 0);
        for (int j = 0; j < N; j++) {
            fill(cons[i][j], cons[i][j] + N, 0);
        }
    }
}

void solve() {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char ch;
            scanf("\n%c", &ch);
            matrix[i][j] = _map[ch];
        }
    }

    #define in fill(marker, marker + N, 0);

    in
    for (int j = 0; j < m; j++) {
        int p = _map['<'];
        for (int i = 0; i < n; i++) {
            cons[p][i][j] = marker[i];
            marker[i] |= matrix[i][j] != -1;
        }
    }

    in

    for (int j = m - 1; j >= 0; j--) {
        int p = _map['>'];
        for (int i = 0; i < n; i++) {
            cons[p][i][j] = marker[i];
            marker[i] |= matrix[i][j] != -1;
        }
    }

    in

    for (int i = 0; i < n; i++) {
        int p = _map['^'];
        for (int j = 0; j < m; j++) {
            cons[p][i][j] = marker[j];
            marker[j] |= matrix[i][j] != -1;
        }
    }

    in

    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < m; j++) {
            int p = _map['v'];
            cons[p][i][j] = marker[j];
            marker[j] |= matrix[i][j] != -1;
        }
    }

    #define fl (cons[0][i][j] | cons[1][i][j] | cons[2][i][j] | cons[3][i][j])

    in
    for (int j = 0; j < m; j++) {
        int p = _map['<'];
        for (int i = 0; i < n; i++) {
            if (matrix[i][j] == -1 || marker[i])
                continue;

            if (matrix[i][j] == p)
                wall[p][i] = 1;
            marker[i] = 1;
        }
    }

    in

    for (int j = m - 1; j >= 0; j--) {
        int p = _map['>'];
        for (int i = 0; i < n; i++) {
            if (matrix[i][j] == -1 || marker[i])
                continue;

            
            if (matrix[i][j] == p)
                wall[p][i] = 1;
            marker[i] = 1;
        }
    }

    in

    for (int i = 0; i < n; i++) {
        int p = _map['^'];
        for (int j = 0; j < m; j++) {

            if (matrix[i][j] == -1 || marker[j])
                continue;

            if (matrix[i][j] == p)
                wall[p][j] = 1;
            marker[j] = 1;
        }
    }

    in

    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < m; j++) {
            int p = _map['v'];
             
            if (matrix[i][j] == -1 || marker[j])
                continue;

            if (matrix[i][j] == p)
                wall[p][j] = 1;
            marker[j] = 1;
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans += wall[_map['<']][i] + wall[_map['>']][i];
    
        for (int j = 0; j < m; j++) {
            bool flag = fl;
            if (wall[_map['<']][i] && !flag) {
                printf("IMPOSSIBLE\n");
                return;
            }

            if (wall[_map['>']][i] && !flag) {
                printf("IMPOSSIBLE\n");
                return;
            }
        }
    }

    for (int j = 0; j < m; j++) {
        ans += wall[_map['^']][j] + wall[_map['v']][j];
    
        for (int i = 0; i < n; i++) {
            bool flag = fl; 
            if (wall[_map['^']][j] && !flag) {
                printf("IMPOSSIBLE\n");
                return;
            }

            if (wall[_map['v']][j] && !flag) {
                printf("IMPOSSIBLE\n");
                return;
            }
        }
    }
    
    cout << ans << "\n";
}

int main() {

    char arr[] = {'.', '<', '>', '^', 'v'};
    for (int i = 0; i < 5; i++)
        _map[arr[i]] = i - 1;

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        init();
        printf("Case #%d: ", i + 1);
        solve();
    }
}
