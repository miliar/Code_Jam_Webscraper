#include <cstdio>
#include <cstring>

const int N = 4;

const int MAX_MSG_LEN = 35;

char *res = NULL;

enum GameState {
    XWon,
    OWon,
    Draw,
    NotComplete
};

void printResult(int caseNum, GameState state)
{
    char msg[MAX_MSG_LEN];
    sprintf(msg, "Case #%d: ", caseNum);
    switch (state) {
    case XWon:
        strcat(msg, "X won\n");
        break;
    case OWon:
        strcat(msg, "O won\n");
        break;
    case Draw:
        strcat(msg, "Draw\n");
        break;
    case NotComplete:
        strcat(msg, "Game has not completed\n");
        break;
    }
    strcat(res, msg);
}

GameState checkRows(char field[][N])
{
    bool isDot = false;
    for (int i = 0; i < N; ++i) {
        int s = (field[i][0] == 'T') ? 1 : 0;
        if (field[i][s] == '.') {
            isDot = true;
            continue;
        }
        int j = s + 1;
        while (j < N && (field[i][s] == field[i][j] || field[i][j] == 'T')) {
            ++j;
        }
        if (j == N) {
            return (field[i][s] == 'X') ? XWon : OWon;
        }
    }
    return isDot ? NotComplete : Draw;
}

GameState checkCols(char field[][N])
{
    bool isDot = false;
    for (int i = 0; i < N; ++i) {
        int s = (field[0][i] == 'T') ? 1 : 0;
        if (field[s][i] == '.') {
            isDot = true;
            continue;
        }
        int j = s + 1;
        while (j < N && (field[s][i] == field[j][i] || field[j][i] == 'T')) {
            ++j;
        }
        if (j == N) {
            return (field[s][i] == 'X') ? XWon : OWon;
        }
    }
    return isDot ? NotComplete : Draw;
}

GameState checkDiagonals(char field[][N])
{
    bool isDot = false;
    // Main diagonal
    int s = (field[0][0] == 'T') ? 1 : 0;
    if (field[s][s] == '.') {
        isDot = true;
    }
    else {
        while (s < (N - 1) && (field[s][s] == field[s+1][s+1] || field[s+1][s+1] == 'T')) {
            ++s;
        }
        if (s == N-1) {
            return (field[s][s] == 'X') ? XWon : OWon;
        }
    }
    // Adverse diagonal
    s = (field[N-1][0] == 'T') ? N-2 : N-1;
    if (field[s][N-s-1] == '.') {
        isDot = true;
    }
    else {
        while (s > 0 && (field[s][N-s-1] == field[s-1][N-s] || field[s-1][N-s] == 'T')) {
            --s;
        }
        if (s == 0) {
            return (field[s][N-s-1] == 'X') ? XWon : OWon;
        }
    }
    return isDot ? NotComplete : Draw;
}

int main()
{
    int n;
    char c;
    scanf("%d", &n);
    int len = n * MAX_MSG_LEN + 1;
    res = new char[len];
    memset(res, 0, len);
    for(int i = 1; i <= n; ++i) {
        scanf("%c", &c);
        char field[N][N];
        for (int k = 0; k < N; ++k) {
            for (int l = 0; l < N; ++l) {
                scanf("%c", &field[k][l]);
            }
            scanf("%c", &c);
        }
        GameState stateRows = checkRows(field);
        GameState stateCols = checkCols(field);
        GameState stateDiags = checkDiagonals(field);
        if (stateRows == XWon || stateCols == XWon || stateDiags == XWon) {
            printResult(i, XWon);
        }
        else if (stateRows == OWon || stateCols == OWon || stateDiags == OWon) {
            printResult(i, OWon);
        }
        else if (stateRows == NotComplete || stateCols == NotComplete || stateDiags == NotComplete) {
            printResult(i, NotComplete);
        }
        else {
            printResult(i, Draw);
        }
    }
    printf("%s", res);
    delete[] res;
    return 0;
}