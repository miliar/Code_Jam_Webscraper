#include <cstdio>
#include <algorithm>
using namespace std;

char str[110][110];
int loop[105][105];
int r, c;
int getDirection(char x) {
    if (x=='^') return 1;
    if (x=='v') return 2;
    if (x=='<') return 3;
    if (x=='>') return 4;
    return 0;
}

int checkImp(int x, int y) {
    int imp = 1;

    for(int i=0 ; i<r ; i++) {
        if (i==x) continue;
        if (str[i][y] != '.') {imp = 0; break;}
    }
    for(int i=0 ; i<c ; i++) {
        if (i==y) continue;
        if (str[x][i] != '.') {imp = 0; break;}
    }

    return imp;
}
int main() {
    int tt;
    scanf("%d", &tt);
    for(int t=0 ; t<tt ; t++) {
        scanf("%d%d", &r, &c);
        for(int i=0 ; i<r ;i++) {
            scanf("%s", str[i]);
        }

        int imp = 1;
        for(int i=0 ; i<r ; i++) {
            for(int j=0 ; j<c ; j++) {
                if (str[i][j] != '.' && checkImp(i, j) == 1) {
                    imp = 0; break;
                }
            }
            if (imp == 0) break;
        }
        if (imp == 0) {
            printf("Case #%d: IMPOSSIBLE\n", t+1);
            continue;
        }


        for(int i=0 ; i<r ; i++) for(int j=0 ; j<c ; j++) loop[i][j] = 0;

        int ans = 0;
        for(int i=0 ; i<r ; i++) {
            for(int j=0 ; j<c ; j++) {
                if (loop[i][j] > 0 || str[i][j] == '.') continue;
                int x=i, y=j;
                int direction = getDirection(str[x][y]);
                while(x >= 0 && x < r && y>=0 && y < c && loop[x][y] == 0) {
                    if (str[x][y] != '.') loop[x][y] = 1;

                    if (str[x][y] == 'v') x++;
                    else if (str[x][y] == '>') y++;
                    else if (str[x][y] == '<') y--;
                    else if (str[x][y] == '^') x--;
                    else {
                        if (direction == 1) x--;
                        else if (direction == 2) x++;
                        else if (direction == 3) y--;
                        else if (direction == 4) y++;
                    }
                    if (x >= 0 && x < r && y>=0 && y < c && getDirection(str[x][y]) != 0) {
                        direction = getDirection(str[x][y]);
                    }
                }

                if (x >= 0 && x < r && y>=0 && y < c) {}
                else ans++;
            }
        }

        printf("Case #%d: %d\n", t+1, ans);
    }
}
