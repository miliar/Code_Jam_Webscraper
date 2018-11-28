#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <utility>
#include <set>


using namespace std;
typedef long long ll;

int T, emptyCount;
char board[16][16], winner;


bool rowColWinner() {
    int xR = 0, oR = 0, xC = 0, oC = 0, tR = 0, tC = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            xR += board[i][j] == 'X';
            oR += board[i][j] == 'O';
            tR += board[i][j] == 'T';
            emptyCount += board[i][j] == '.';
            xC += board[j][i] == 'X';
            oC += board[j][i] == 'O';
            emptyCount += board[j][i] == '.';
            tC += board[j][i] == 'T';
        }
        if (xR + tR > 3 || (xC + tC > 3)) {
            winner = 'X';
            return true;
        }
        else if  (oR + tR > 3  || oC + tC > 3) {
            winner = 'O';
            return true;
        }
        xR = oR = xC = oC = tR = tC = 0;
    }
    return false;
}
bool diagWinner() {
    int xL = 0, oL = 0, tL = 0, xR = 0, oR = 0, tR = 0;
    for (int i = 0; i < 4; ++i) {
        xL += board[i][i] == 'X';
        oL += board[i][i] == 'O';
        tL += board[i][i] == 'T';
        xR += board[i][3 - i] == 'X';
        oR += board[i][3 - i] == 'O';
        tR += board[i][3 - i] == 'T';
        emptyCount += board[i][i] == '.';
        emptyCount += board[i][3 - i] == '.';

        if (xL + tL > 3 || xR + tR > 3) {
            winner = 'X';
            return true;
        }
        else if (oL + tL > 3 || oR + tR > 3) {
            winner = 'O';
            return true;
        }
    }
    return false;
}


void printAnswer(int tc, bool haswinner) {
    cout << "Case #" << tc <<": ";
    if (haswinner) {
        cout << winner << " won" << '\n';
    }
    else {
        if (emptyCount == 0) {
            cout << "Draw" << '\n';
        }
        else {
            cout << "Game has not completed" << '\n';
        }
    }

}
int main() {
    ios_base::sync_with_stdio(false);
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        emptyCount = 0, end = false;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> board[i][j];

        if (rowColWinner() || diagWinner()) {
            printAnswer(tc, true);
        }
        else {
            printAnswer(tc, false);
        }
    }
}
