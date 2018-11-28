#include <iostream>
#include <cmath>

using namespace std;

int T, N;
char tbl[4][5];
char ch, winner;
bool dot, won;

bool check_row()
{
    int count;
    for (int i = 0; i < 4; ++i) {
        count = 0;
        winner = tbl[i][0];
        for (int j = 0; j < 4; ++j){
            ch = tbl[i][j];
            if (ch == '.')
                dot = true;
            else if (ch == 'T')
                ++count;
            else if (winner == 'T') {
                winner = ch;
                ++count;
            }
            else if (winner != ch)
                continue;
            else
                ++count;
        }
        if (count == 4)
            return true;
    }
    return false;
}

bool check_column()
{
    int count;
    for (int i = 0; i < 4; ++i) {
        count = 0;
        winner = tbl[0][i];
        for (int j = 0; j < 4; ++j){
            ch = tbl[j][i];
            if (ch == '.')
                dot = true;
            else if (ch == 'T')
                ++count;
            else if (winner == 'T') {
                winner = ch;
                ++count;
            }
            else if (winner != ch)
                continue;
            else
                ++count;
        }
        if (count == 4)
            return true;
    }
    return false;
}

bool check_cross1()
{
    int count = 0;
    winner = tbl[0][0];
    for (int i = 0; i < 4; ++i) {
        ch = tbl[i][i];
        if (ch == '.')
            dot = true;
        else if (ch == 'T')
            ++count;
        else if (winner == 'T') {
            winner = ch;
            ++count;
        }
        else if (winner != ch)
            continue;
        else
            ++count;
    }
    if (count == 4)
        return true;
    return false;
}

bool check_cross2()
{
    int count = 0;
    winner = tbl[0][3];
    for (int i = 0; i < 4; ++i) {
        ch = tbl[i][3-i];
        if (ch == '.')
            dot = true;
        else if (ch == 'T')
            ++count;
        else if (winner == 'T') {
            winner = ch;
            ++count;
        }
        else if (winner != ch)
            continue;
        else
            ++count;
    }
    if (count == 4)
        return true;
    return false;
}

int main()
{
    scanf("%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        for (int j = 0; j < 4; ++j)
        scanf("%s\n", tbl[j]);

        dot = false;
        if (check_row() || check_column() || check_cross1() || check_cross2())
            won = true;
        else
            won = false;

        printf("Case #%d: ", i);
        if(won && winner != '.' && winner != 'T')
            printf("%c won\n", winner);
        else if (dot)
            printf("Game has not completed\n");
        else
            printf("Draw\n");

    }
    return 0;
}

