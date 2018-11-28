#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

#define MAX 210

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int R, C;
string fie[MAX];
map<char,int> ma;

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; ++i) cin >> fie[i];
    
    int res = 0;
    bool ok = true;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            if (fie[i][j] == '.') continue;
            
            int dir = ma[fie[i][j]];
            bool out = false;
            bool exist = false;
            for (int k = 0; k < 4; ++k) {
                int ni = i, nj = j;
                for (int ppp = 0; ; ++ppp) {
                    ni += dx[k];
                    nj += dy[k];
                    if (ni < 0 || ni >= R || nj < 0 || nj >= C) {
                        if (dir == k) out = true;
                        break;
                    }
                    if (fie[ni][nj] != '.') {
                        exist = true;
                        break;
                    }
                }
            }
            if (!exist) ok = false;
            if (out) ++res;
        }
    }
        
    if (ok) cout << res << endl;
    else puts("IMPOSSIBLE");
}

int main() {
    freopen( "/Users/macuser/Dropbox/Contest/A-large.in", "r", stdin );
    freopen( "/Users/macuser/Dropbox/Contest/A-large.out", "w", stdout );
    
    ma.clear();
    ma['v'] = 0;
    ma['>'] = 1;
    ma['^'] = 2;
    ma['<'] = 3;
    
    int TTT;
    scanf("%d", &TTT);
    for (int XXX = 0; XXX < TTT; ++XXX) {
        printf("Case #%d: ", XXX+1);
        solve();
    }
    
    return 0;
}



