#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

bool check(char board[4][4], char opp, bool& complete) {
    bool won;
    int i=0, j=0;

    for (i=0; i<4; i++) {
        won = true;
        for (j=0; j<4; j++) {
            if (board[i][j] == opp || board[i][j] == '.') won = false;
            if (board[i][j] == '.') complete = false;
        }
        if (won) return true;
    }
    
    for (i=0; i<4; i++) {
        won = true;
        for (j=0; j<4; j++) {
            if (board[j][i] == opp || board[j][i] == '.') won = false;
            if (board[i][j] == '.') complete = false;
        }
        if (won) return true;
    }
    
    won = true;
    for (i=0; i<4; i++) {
        if (board[i][i] == opp || board[i][i] == '.') won = false;
    }
    if (won) return true;
    
    won = true;
    for (i=0; i<4; i++) {
        if (board[3-i][i] == opp || board[3-i][i] == '.') won = false;
    }
    if (won) return true;
    
    return false;
}

int main() {
    int tests, ctr, i, j;
    char board[4][4];
    cin >> tests;
    for (ctr=0; ctr<tests; ctr++) {
        for (i=0; i<4; i++) {
            string s;
            cin >> s;
            for (j=0; j<4; j++) board[i][j] = s[j];    
        }
        
        bool complete=true, xwon=false, owon=false;
        
        
        
        // CHECK for X Won condition
        xwon = check(board, 'O', complete);
        
        // CHECK for O Won condition
        owon = check(board, 'X', complete);
        
        cout << "Case #" << ctr+1 << ": ";
        if (xwon) cout << "X won\n";
        else if (owon) cout << "O won\n";
        else if (complete) cout << "Draw\n";
        else cout << "Game has not completed\n";
        
        /*cout << "BOARD:\n";
        for (i=0; i<4; i++) {
            for (j=0; j<4; j++)
                cout << board[i][j];
            cout << endl;
        }*/
    }
    
    return 0;   
}
