#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rep(a,b) fr(a,0,b)
#define fst first
#define snd second
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef pair<int,int> pii;

map<char,int> mdir = {{'^', 0}, {'>', 1}, {'v', 2}, {'<', 3}};

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

char grid[111][111];

int main() {
    //ios_base::sync_with_stdio(false);
    int tc;
    scanf("%d", &tc);
    for (int caso = 1; caso <= tc; ++caso) {
        int R,C;
        scanf("%d %d", &R, &C);
        rep(i,R) scanf("%s", grid[i]);
        int rsp = 0;
        rep(i,R) rep(j,C) if (grid[i][j] != '.') {
            int x = i; int y = j;
            bool need = true;
            bool can = false;
            rep(k,4) {
                int tx = x + dx[k];
                int ty = y + dy[k];
                bool safe = false;
                while (tx >= 0 && tx < R && ty >= 0 && ty < C) {
                    if (grid[tx][ty] != '.') {
                        safe = true;
                        break;
                    }
                    tx = tx + dx[k];
                    ty = ty + dy[k];
                }
                if (safe) {
                    can = true;
                    if (k == mdir[grid[i][j]]) need = false;
                }
            }
            if (can == false) {
                rsp = -1;
                break;
            }
            rsp += need;
        }
        if (rsp == -1) {
            printf("Case #%d: IMPOSSIBLE\n", caso);
        } else {
            printf("Case #%d: %d\n", caso, rsp);
        }
    }
    return 0;
}
