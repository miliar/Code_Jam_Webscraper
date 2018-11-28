#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int t, r, c;
char maze[110][110];
bool ok[110][110];
bool used[110][110];

int xx[5] = {0, -1, 0, 0, 1};
int yy[5] = {0, 0, 1, -1, 0};

bool dfs(int x, int y, int dir){

    if (x == 0 || x == r + 1 || y == 0 || y == c + 1)
        return 0;
    if (maze[x][y] != '.')
        return 1;
    return dfs(x + xx[dir], y + yy[dir], dir);
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca++){
        scanf("%d%d", &r, &c);

        for (int i = 1; i <= r; i++){
            scanf("%s", maze[i] + 1);
        }

        int ans = 0;
        bool nans = 0;
        for (int i = 1; i <= r; i++){
            for (int j = 1; j <= c; j++){
                if (maze[i][j] != '.'){
                    int dir;
                    switch (maze[i][j]) {
                        case '^' :
                            dir = 1;
                            break;
                        case '>' :
                            dir = 2;
                            break;
                        case '<' :
                            dir = 3;
                            break;
                        case 'v' :
                            dir = 4;
                    }
                    //printf("%d %d %d\n", i, j, dir) ;
                    if (dfs(i + xx[dir], j + yy[dir], dir))
                        continue;
                    //printf("end %d\n", i);
                    bool flag = 0;
                    for (int fld = 1; fld <= 4; fld++)
                        if (dfs(i + xx[fld], j + yy[fld], fld)){
                            ans++;
                            flag = 1;
                            break;
                        }

                    if (!flag)
                        nans = 1;
                }
            }
        }
        if (nans){
            printf("Case #%d: IMPOSSIBLE\n", ca);
        }else{
            printf("Case #%d: %d\n", ca, ans);
        }
    }
}
