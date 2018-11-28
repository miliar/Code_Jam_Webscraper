#include <bits/stdtr1c++.h>

using namespace std;

const int MAXN = 105;
char a[MAXN][MAXN];

int main() {
    ios::sync_with_stdio(0);
    
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        int r, c; cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> a[i][j];
                //cerr << a[i][j];
            }
            //cerr << endl;
        }
        
        int cnt = 0;
        for (int i = 0; i < r; i++) {
            cnt += a[i][0] == '<';
            cnt += a[i][c-1] == '>';
        }
        
        for (int j = 0; j < c; j++) {
            cnt += a[0][j] == '^';
            cnt += a[r-1][j] == 'v';
        }
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (a[i][j] == '.') continue;
                int nbad = 0;
                // from left
                int C = 0;
                for (int k = 0; k < j; k++) {
                    if (a[i][k] != '.') C++;
                }
                nbad += C == 0;
                C = 0;
                // from right
                for (int k = j+1; k < c; k++) {
                    if (a[i][k] != '.') C++;
                }
                nbad += C == 0;
                C = 0;
                // from top
                for (int k = 0; k < i; k++) {
                    if (a[k][j] != '.') C++;
                }
                nbad += C == 0;
                C = 0;
                // from bot
                for (int k = i+1; k < r; k++) {
                    if (a[k][j] != '.') C++;
                }
                nbad += C == 0;
                C = 0;
                
                if (nbad == 4) {
                    cnt = -1;
                    goto done;
                } else if (nbad >= 1) {
                    int dx, dy;
                    if (a[i][j] == '<') {
                        if (j == 0) continue;
                        dx = 0, dy = -1;
                    } else if (a[i][j] == '>') {
                        if (j == c-1) continue;
                        dx = 0, dy = 1;
                    } else if (a[i][j] == '^') {
                        if (i == 0) continue;
                        dx = -1, dy = 0;
                    } else if (a[i][j] == 'v') {
                        if (i == r-1) continue;
                        dx = 1; dy = 0;
                    }
                    
                    int ci = i+dx, cj = j+dy;
                    //cerr << "manual checking " << i << " " << j << " " << dx << " " << dy << endl;
                    while (ci < r && ci >= 0 && cj < c && cj >= 0) {
                        if (a[ci][cj] != '.') C++;
                        ci += dx; cj += dy;
                        //cerr << a[ci][cj];
                    }
                    //cerr << endl;
                    //cerr << C << endl;
                    cnt += (C == 0);
                }
            }
        }
        
        done:
        cout << "Case #" << ca << ": ";
        if (cnt == -1) cout << "IMPOSSIBLE" << endl;
        else cout << cnt << endl;
    }
	return 0;
}