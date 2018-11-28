#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    string ans;
    char board[4][4];
    bool xcol[4];
    bool ocol[4];
    bool xwin;
    bool owin;
    bool hasdot;
    cin >> T;
    cin.ignore();
    int TT = T;
    while (T--) {
        hasdot = false;
        ans = "Draw";
        fill(xcol, xcol + 4, true);
        fill(ocol, ocol + 4, true);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++)
                board[i][j] = getchar();
            cin.ignore();
        }
        cin.ignore();
        
        xwin = true;
        owin = true;
        for (int i = 0; i < 4; i++) {
            if (board[i][i] == 'X')
                owin = false;
            else if (board[i][i] == 'O')
                xwin = false;
            else if (board[i][i] == '.') {
                owin = false;
                xwin = false;
            }
            if (!owin && !xwin)
                break;
        }
        if (owin) {
            ans = "O won";
            cout << "Case #" << TT - T << ": " << ans << '\n';
            continue;
        }
        else if (xwin) {
            ans = "X won";
            cout << "Case #" << TT - T << ": " << ans << '\n';
            continue;
        }
        xwin = true;
        owin = true;
        for (int i = 0; i < 4; i++) {
            if (board[i][3 - i] == 'X')
                owin = false;
            else if (board[i][3 - i] == 'O')
                xwin = false;
            else if (board[i][3 - i] == '.') {
                owin = false;
                xwin = false;
            }
            if (!owin && !xwin)
                break;
        }
        if (owin) {
            ans = "O won";
            cout << "Case #" << TT - T << ": " << ans << '\n';
            continue;
        }
        else if (xwin) {
            ans = "X won";
            cout << "Case #" << TT - T << ": " << ans << '\n';
            continue;
        }

        for (int i = 0; i < 4; i++) {
            xwin = true;
            owin = true;
            for (int j = 0; j < 4; j++) {
                if (board[i][j] == 'X') {
                    owin = false;
                    ocol[j] = false;
                }
                else if (board[i][j] == 'O') {
                    xwin = false;
                    xcol[j] = false;
                }
                else if (board[i][j] == '.') {
                    hasdot = true;
                    owin = false;
                    ocol[j] = false;
                    xwin = false;
                    xcol[j] = false;
                }
            }
            if (xwin || owin)
                break;
        }
        if (hasdot)
            ans = "Game has not completed";
        if (xwin)
            ans = "X won";
        else if (owin)
            ans = "O won";
        else {
            for (int i = 0; i < 4; i++) {
                if (ocol[i]) {
                    ans = "O won";
                    break;
                }
                else if (xcol[i]) {
                    ans = "X won";
                    break;
                }
            }   
        }
        cout << "Case #" << TT - T << ": " << ans << '\n';
    }
    return 0;
}
