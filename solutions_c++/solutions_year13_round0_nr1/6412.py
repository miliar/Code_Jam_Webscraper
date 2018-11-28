#include <iostream>
#include <string>

using namespace std;

int T, countdot, ri;
char board[4][4];
string result[4] = {
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};

bool hasWon(const char player) {
    int j, k, countx, county;
    int countde = 0, countdn = 0;

    for (j = 0; j < 4; ++j) {
        county = 0;
        for (k = 0; k < 4; ++k) {
            if (0 == k)
                countx = 0;

            if (player == board[j][k] ||
                    'T' == board[j][k]) {
                ++countx;
                if (j == k)
                    ++countde;
                if (j + k == 3)
                    ++countdn;
            }
            if (player == board[k][j] ||
                    'T' == board[k][j])
                ++county;

            if (4 == countx || 4 == county ||
                    4 == countde || 4 == countdn)
                return true;
        }
    }

    return false;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outputl.out", "w", stdout);

    cin >> T;
    for (int i = 1; i <= T; ++i) {
        //
        countdot = 0;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k) {
                cin >> board[j][k];
                if ('.' == board[j][k])
                    ++countdot;
            }

        //
        if (hasWon('X'))
            ri = 0;
        else if (hasWon('O'))
            ri = 1;
        else if (0 == countdot)
            ri = 2;
        else
            ri = 3;

        //
        cout << "Case #" << i << ": "
             << result[ri] << endl;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

