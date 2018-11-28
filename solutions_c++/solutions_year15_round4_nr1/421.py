#include <bits/stdc++.h>

using namespace std;

int R, C;
string A[100];

int B[100][100][4];

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; i++)
        cin >> A[i];
    
    {
        vector<int> v(100, -1);
        for (int r = 0; r < R; r++)
            for (int c = 0; c < C; c++) {
                B[r][c][0] = v[c];
                if (A[r][c] != '.')
                    v[c] = r;
            }
    }
    
    {
        vector<int> v(100, -1);
        for (int r = R-1; r >= 0; r--)
            for (int c = 0; c < C; c++) {
                B[r][c][2] = v[c];
                if (A[r][c] != '.')
                    v[c] = r;
            }
    }
    
    {
        vector<int> v(100, -1);
        for (int c = 0; c < C; c++)
            for (int r = 0; r < R; r++) {
                B[r][c][1] = v[r];
                if (A[r][c] != '.')
                    v[r] = c;
            }
    }
    
    {
        vector<int> v(100, -1);
        for (int c = C-1; c >= 0; c--)
            for (int r = 0; r < R; r++) {
                B[r][c][3] = v[r];
                if (A[r][c] != '.')
                    v[r] = c;
            }
    }
    
    int ans = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            switch (A[r][c]) {
                case '<':
                    if (B[r][c][1] == -1) {
                        ans++;
                        if (B[r][c][0] == -1 && B[r][c][2] == -1 && B[r][c][3] == -1) {
                            cout << "IMPOSSIBLE";
                            return;
                        }
                    }
                    break;
                case '^':
                    if (B[r][c][0] == -1) {
                        ans++;
                        if (B[r][c][1] == -1 && B[r][c][2] == -1 && B[r][c][3] == -1) {
                            cout << "IMPOSSIBLE";
                            return;
                        }
                    }
                    break;
                case '>':
                    if (B[r][c][3] == -1) {
                        ans++;
                        if (B[r][c][0] == -1 && B[r][c][2] == -1 && B[r][c][1] == -1) {
                            cout << "IMPOSSIBLE";
                            return;
                        }
                    }
                    break;
                case 'v':
                    if (B[r][c][2] == -1) {
                        ans++;
                        if (B[r][c][0] == -1 && B[r][c][1] == -1 && B[r][c][3] == -1) {
                            cout << "IMPOSSIBLE";
                            return;
                        }
                    }
                    break;
            }
        }
    }
    
    cout << ans;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
    return 0;
}
