#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

int r, c;
char grid[200][200];

int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};
int dir[256];

bool inRange(int cr, int cc) {
    if (cr < 0)
        return false;
    if (cc < 0)
        return false;
    if (cr >= r)
        return false;
    if (cc >= c)
        return false;
    return true;
}

bool checkDir(int cr, int cc, int d) {
    int i;
    for (i = 1; inRange(cr+i*dr[d], cc+i*dc[d]); i++)
        if (grid[cr+dr[d]*i][cc + dc[d]*i] != '.')
            return true;
    return false;
}

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    dir['^'] = 0;
    dir['>'] = 1;
    dir['v'] = 2;
    dir['<'] = 3;
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        scanf("%d%d", &r, &c);
        int i;
        for (i = 0; i < r; i++)
            scanf("%s", grid[i]);
        
        int ans = 0;
        int j, k;
        bool possible = true;
        for (i = 0; i < r; i++) {
            for (j = 0; j < c; j++) {
                if (grid[i][j] == '.')
                    continue;
                
                if (checkDir(i, j, dir[grid[i][j]]))
                    continue;
                ans++;
                for (k = 0; k < 4; k++)
                    if (checkDir(i, j, k))
                        break;
                if (k == 4)
                    possible = false;
            }
        }
        
        if (possible)
            printf("%d\n", ans);
        else
            printf("IMPOSSIBLE\n");
    }
}
        