#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
using namespace std;

#define REP(i,n) for( int i = 0; i<n; i++)
#define rep(n) REP(end,n)

const int SIZE=4;

int hantei(char a, char b, char c, char d) {
    if ( (a == 'O' || a == 'T')
         && (b == 'O' || b == 'T')
         && (c == 'O' || c == 'T')
         && (d == 'O' || d == 'T') ) {
        return 3;
    }
    else if ( (a == 'X' || a == 'T')
              && (b == 'X' || b == 'T')
              && (c == 'X' || c == 'T')
              && (d == 'X' || d == 'T') ){
        return 2;
    }
    return 0;
}

int main() {
    int ncases;
    cin>>ncases;
    REP(k,ncases) {
        int res = 1, tmp; //0:Game has not completed, 1:Draw, 2:X, 3:O
        char board[SIZE][SIZE];
        REP(i,SIZE) REP(j,SIZE) {
            char tmp;
            cin>>tmp;
            if ( tmp == '.' ) {
                res = 0;
            }
            board[i][j] = tmp;
        }

        // tate
        REP(i,SIZE) {
            if (tmp = hantei(board[i][0],board[i][1],board[i][2],board[i][3])) res = tmp;
        }

        // yoko
        REP(i,SIZE) {
            if (tmp = hantei(board[0][i],board[1][i],board[2][i],board[3][i])) res = tmp;
        }

        // naname
        if (tmp = hantei(board[0][0],board[1][1],board[2][2],board[3][3])) res = tmp; 
        if (tmp = hantei(board[0][3],board[1][2],board[2][1],board[3][0])) res = tmp;

        //0:Game has not completed, 1:Draw, 2:X, 3:O
        cout << "Case #" << k+1 << ": ";
        switch (res) {
        case 0:
            cout << "Game has not completed" << endl;
            break;
        case 1:
            cout << "Draw" << endl;
            break;
        case 2:
            cout << "X won" << endl;
            break;
        case 3:
            cout << "O won" << endl;
            break;
        }
    }
    return 0;
}
