#include <cstdio>
#include <algorithm>
using namespace std;

int tc;
int r, c, a, b, g[40];
int mirror[20][20];
int chk[40];
int x, y, dir; // 0 1 2 3 : À§ ¿À ¾Æ ¿Þ
int newdir[2][4] = {{1, 0, 3, 2}, {3, 2, 1, 0}};
int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

int main(){
    freopen("Cs.in", "r", stdin);
    freopen("Cs.out", "w", stdout);
    scanf("%d", &tc);
    for(int ttc = 1; ttc <= tc; ttc++){
        scanf("%d%d", &r, &c);
        for(int i = 1; i <= r + c; i++){
            scanf("%d%d", &a, &b);
            g[a] = b; g[b] = a;
        }
        bool ansflag = false;
        for(int i = 0; i < (1 << (r * c)); i++){
            bool flag = true;
            for(int j = 0; j < r * c; j++){
                if(i & (1 << j)) mirror[j / c + 1][j % c + 1] = 0; // slash /
                else mirror[j / c + 1][j % c + 1] = 1; // backslash
            }
            for(int j = 1; j <= 2 * (r + c); j++) chk[j] = 0;
            for(int j = 1; j <= 2 * (r + c); j++){
                if(chk[j]) continue;
                if(j <= c) x = 1, y = j, dir = 2;
                else if(j <= (r + c)) x = j - c, y = c, dir = 3;
                else if(j <= (r + c) + c) x = r, y = c - (j - (r + c)) + 1, dir = 0;
                else x = 2 * (r + c) - j + 1, y = 1, dir = 1;
                //printf("//%d:\n", j);
                while(x >= 1 && x <= r && y >= 1 && y <= c){
                    //printf("%d %d %d\n", x, y, dir);
                    dir = newdir[mirror[x][y]][dir];
                    x += dx[dir]; y += dy[dir];
                }
                int dest;
                if(x == 0) dest = y;
                else if(x == r + 1) dest = (c - y) + (r + c) + 1;
                else if(y == 0) dest = 2 * (r + c) - x + 1;
                else if(y == c + 1) dest = x + c;
                if(dest != g[j]) {flag = false; break;}
            }
            if(flag == true){
                ansflag = true;
                printf("Case #%d:\n", ttc);
                for(int x = 1; x <= r; x++){
                    for(int y = 1; y <= c; y++){
                        putchar(mirror[x][y] ? '\\' : '/');
                    }puts("");
                }
                break;
            }
        }
        if(!ansflag){
            printf("Case #%d:\n", ttc);
            puts("IMPOSSIBLE");
        }
    }
}
