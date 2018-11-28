#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;

string XWon = "X won";
string OWon = "O won";
string Draw = "Draw";
string GameRunning = "Game has not completed";

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tCase = 0, kase;

    scanf ("%d",&tCase);

    for (kase = 1; kase <= tCase; kase++){
        string grid[4];
        int i, j, dotCount = 0, XCount = 0, OCount = 0, gameResult = 0;
        for (i = 0; i < 4; i++) cin >> grid[i];
        printf ("Case #%d: ", kase);

        //Diagonal (0,0)
        for (i = 0; i < 4; i++) {
            if (grid[i][i] == 'X') XCount++;
            else if (grid[i][i] == 'O') OCount++;
            else if (grid[i][i] == 'T') { XCount++; OCount++; }
        }

        if (XCount == 4) { cout << XWon << endl; gameResult = 1; }
        else if (OCount == 4) { cout << OWon << endl; gameResult = 1; }

        //Diagonal (0,3)
        XCount = OCount = 0;
        for (i = 0; i < 4; i++) {
            if (grid[i][3-i] == 'X') XCount++;
            else if (grid[i][3-i] == 'O') OCount++;
            else if (grid[i][3-i] == 'T') { XCount++; OCount++; }
        }

        if (XCount == 4) { cout << XWon << endl; gameResult = 1; }
        else if (OCount == 4) { cout << OWon << endl; gameResult = 1; }

        if (!gameResult) for (i = 0; i < 4; i++){
            // Horizontal
            XCount = OCount = 0;
            for (j = 0; j < grid[i].size(); j++){
                if (grid[i][j] == 'X') XCount++;
                else if (grid[i][j] == 'O') OCount++;
                else if (grid[i][j] == 'T') { XCount++; OCount++; }
                else dotCount++;
            }

            if (XCount == 4) { cout << XWon << endl; gameResult = 1; }
            else if (OCount == 4) { cout << OWon << endl; gameResult = 1; }
            if (gameResult) break;

            // Vertical
            XCount = OCount = 0;
            for (j = 0; j < grid[i].size(); j++){
                if (grid[j][i] == 'X') XCount++;
                else if (grid[j][i] == 'O') OCount++;
                else if (grid[j][i] == 'T') { XCount++; OCount++; }
                else dotCount++;
            }

            if (XCount == 4) { cout << XWon << endl; gameResult = 1; }
            else if (OCount == 4) { cout << OWon << endl; gameResult = 1; }
            if (gameResult) break;
        }

        if (!gameResult && !dotCount) cout << Draw << endl;
        else if (!gameResult) cout << GameRunning << endl;
    }

    return 0;
}
