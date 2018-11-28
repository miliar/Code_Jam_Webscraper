#include <stdio.h>

int T;
char map[6][6];

bool win(char c) {
    int i, j;
    int a, b;
    for (i = 0; i < 4; i++) {
        a = 0;
        b = 0;
        for (j = 0; j < 4; j++) {
            if (map[i][j] == c) a++;
            if (map[i][j] == 'T') b++;
        }
        if (a == 4 || a == 3 && b == 1) return true;
    }
    for (i = 0; i < 4; i++) {
        a = 0;
        b = 0;
        for (j = 0; j < 4; j++) {
            if (map[j][i] == c) a++;
            if (map[j][i] == 'T') b++;
        }
        if (a == 4 || a == 3 && b == 1) return true;
    }
    a = 0;
    b = 0;
    for (i = 0; i < 4; i++) {
        if (map[i][i] == c) a++;
        if (map[i][i] == 'T')b++;
    }
    if (a == 4 || a == 3 && b == 1) return true;
    a = 0;
    b = 0;
    for (i = 0; i < 4; i++) {
        if (map[i][3-i] == c) a++;
        if (map[i][3-i] == 'T')b++;
    }
    if (a == 4 || a == 3 && b == 1) return true;
}

int main() {
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int i, j;
    scanf("%d", &T);
    for (int case_t = 1; case_t <= T; case_t++) {
        for (i = 0; i < 4; i++)
            scanf("%s", map[i]);
        printf("Case #%d: ",case_t);
        if(win('X')) printf("X won\n");
        else if(win('O')) printf("O won\n");
        else{
            bool d = true;
            for(i = 0;i < 4;i++){
                for(j = 0;j < 4;j++)
                    if(map[i][j] == '.')
                        d = false;
            }
            if(d)printf("Draw\n");
            else printf("Game has not completed\n");
               
        }
    }
    return 0;
}