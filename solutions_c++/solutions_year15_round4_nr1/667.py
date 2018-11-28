#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    
    cin.tie(0);
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    
    int TC, R, C;
    string line;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
                
        cin >> R >> C;
        getline(cin, line);
        char grid[R+2][C+2];
        for (int i = 0; i < C+2; i++) grid[0][i] = grid[R+1][i] = '.';
        for (int i = 0; i < R+2; i++) grid[i][0] = grid[i][C+1] = '.';
        for (int i = 0; i < R; i++) {
            getline(cin, line);
            for (int j = 0; j < C; j++) {
                grid[i+1][j+1] = line[j];
            }
        }
                
        bool upkill[R+2][C+2];
        for (int i = 0; i < C+2; i++) upkill[0][i] = true;
        for (int i = 1; i < R+2; i++) {
            for (int j = 0; j < C+2; j++) {
                upkill[i][j] = upkill[i-1][j] && grid[i][j] == '.';
            }
        }
        
        bool downkill[R+2][C+2];
        for (int i = 0; i < C+2; i++) downkill[R+1][i] = true;
        for (int i = R; i >= 0; i--) {
            for (int j = 0; j < C+2; j++) {
                downkill[i][j] = downkill[i+1][j] && grid[i][j] == '.';
            }
        }
        
        bool leftkill[R+2][C+2];
        for (int i = 0; i < R+2; i++) leftkill[i][0] = true;
        for (int i = 0; i < R+2; i++) {
            for (int j = 1; j < C+2; j++) {
                leftkill[i][j] = leftkill[i][j-1] && grid[i][j] == '.';
            }
        }
        
        bool rightkill[R+2][C+2];
        for (int i = 0; i < R+2; i++) rightkill[i][C+1] = true;
        for (int i = 0; i < R+2; i++) {
            for (int j = C; j >= 0; j--) {
                rightkill[i][j] = rightkill[i][j+1] && grid[i][j] == '.';
            }
        }
        
        int ans = 0;
        bool impossible = false;
        for (int i = 1; i <= R; i++) {
            for (int j = 1; j <= C; j++) {
                if (grid[i][j] == '.') continue;
                if (upkill[i-1][j] && downkill[i+1][j] && leftkill[i][j-1] && rightkill[i][j+1]) {
                    impossible = true;
                }
                if (grid[i][j] == '^' && upkill[i-1][j]) ans++;
                if (grid[i][j] == 'v' && downkill[i+1][j]) ans++;
                if (grid[i][j] == '<' && leftkill[i][j-1]) ans++;
                if (grid[i][j] == '>' && rightkill[i][j+1]) ans++;
            }
        }
        
        cout << "Case #" << tc << ": ";
        if (impossible) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
        
        
        
        /*cin >> R >> C;
        getline(cin, line);
        char grid[R+2][C+2];
        for (int i = 0; i < C+2; i++) grid[0][i] = grid[R+1][i] = 0;
        for (int i = 0; i < R+2; i++) grid[i][0] = grid[i][C+1] = 0;
        for (int i = 0; i < R; i++) {
            getline(cin, line);
            for (int j = 0; j < C; j++) {
                grid[i+1][j+1] = line[j];
            }
        }
        
        for (int i = 1; i <= R; i++) {
            for (int j = 1; i <= C; j++) {
                if
            }
        }*/
        
        
    }

    return 0;
}
