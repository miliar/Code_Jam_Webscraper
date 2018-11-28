#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

bool IsRow(char mat[5][5], char sign, int i) {
    for (int k = 0; k < 4; ++k) {
        if (mat[i][k] != sign && mat[i][k] != 'T') {
            return false;
        }
    }
    return true;
}

bool IsCol(char mat[5][5], char sign, int i) {
    for (int k = 0; k < 4; ++k) {
        if (mat[k][i] != sign && mat[k][i] != 'T') {
            return false;
        }
    }
    return true;
}

bool IsMainDiag(char mat[5][5], char sign) {
    for (int i = 0; i < 4; ++i){
        if (mat[i][i] != sign && mat[i][i] != 'T') {
            return false;
        }
    }
    return true;
}

bool IsLeftDiag(char mat[5][5], char sign) {
    for (int i = 0; i < 4; ++i) {
        if (mat[i][3 - i] != sign && mat[i][3 - i] != 'T') {
            return false;
        }
    }
    return true;
}

bool IsDiag(char mat[5][5], char sign) {
    return IsMainDiag(mat, sign) || IsLeftDiag(mat, sign);
}

bool IsWon(char mat[5][5], char sign) {
    for (int i = 0; i < 4; ++i) {
        if (IsRow(mat, sign, i) || IsCol(mat, sign, i)) {
            return true;
        }
    }
    return IsDiag(mat, sign);
}

bool IsXWon(char mat[5][5]) {
    return IsWon(mat, 'X');
}

bool IsOWon(char mat[5][5]) {
    return IsWon(mat, 'O');
}

bool IsFull(char mat[5][5]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (mat[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("outal.txt", "w", stdout);

    int T;
    scanf("%d\n", &T);

    char mat[5][5];
    char line[100];

    int cs = 1;
    while (T--) {
        for (int i = 0; i < 4; ++i) {
            scanf("%s\n", mat[i]);
        }
        if (IsXWon(mat)) {
            printf("Case #%d: X won\n", cs++);
        } else if (IsOWon(mat)) {
            printf("Case #%d: O won\n", cs++);
        } else if (IsFull(mat)) {
            printf("Case #%d: Draw\n", cs++);
        } else {
            printf("Case #%d: Game has not completed\n", cs++);
        }
    }

    return 0;
}

