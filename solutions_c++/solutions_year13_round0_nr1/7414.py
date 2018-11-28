#include<cstdio>

char a[5][5];

bool has_empty_cell() {
    for (int x = 0; x < 4; x++)
        for (int y = 0; y < 4; y++)
            if (a[x][y] == '.')
                return true;
    return false;
}

bool win(char c) {
    bool flag;
    for (int x = 0; x < 4; x++) {
        flag = true;
        for (int y = 0; y < 4; y++)
            if (a[x][y] != c and a[x][y] != 'T')
                flag = false;
        if (flag) return true;
    }
    for (int y = 0; y < 4; y++) {
        flag = true;
        for (int x = 0; x < 4; x++)
            if (a[x][y] != c and a[x][y] != 'T')
                flag = false;
        if (flag) return true;
    }
    flag = true;
    for (int x = 0; x < 4; x++)
        if (a[x][x] != c and a[x][x] != 'T')
            flag = false;
    if (flag) return true;
    flag = true;
    for (int x = 0; x < 4; x++)
        if (a[x][3 - x] != c and a[x][3 - x] != 'T')
            flag = false;
    if (flag) return true;
    return false;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        for (int x = 0; x < 4; x++)
            scanf("%s", a[x]);
        if (win('X'))
            puts("X won");
        else if (win('O'))
            puts("O won");
        else if (has_empty_cell())
            puts("Game has not completed");
        else
            puts("Draw");
    }
}
