//Common code for Google code jam

#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <array>
#include <vector>
#include <utility>

#define fori(n) for (uint i = 0; i < n; ++i)
#define forj(n) for (uint j = 0; j < n; ++j)
#define sc static_cast
#define range(con) begin(con), end(con)

using uint = uint32_t;
using uint64 = uint64_t;
using int64 = int64_t;
using namespace std;

///////////////////////////////////////////

enum class status { unknown, xwon, owon};

int main () {
    array<array<char, 4>,4> board;
    uint ncases, nx, no, np;
    status winner;
    cin >> ncases; ++ncases;

    for (uint caseNumber = 1; caseNumber < ncases; ++caseNumber) {
        fori(4)
            forj(4)
                cin >> board[i][j];

        np = 0; //~number of "." found on board
        winner = status::unknown;
        
        //check lines
        fori(4) {
            nx = 0; no = 0;
            forj(4) {
                if ( board[i][j] == 'X' ) ++nx;
                else if ( board[i][j] == 'O' ) ++no;
                else if ( board[i][j] == 'T' ) { ++no; ++nx; }
                else { ++np; }
            }
            if (nx == 4) { winner = status::xwon; goto announceWinner;}
            if (no == 4) { winner = status::owon; goto announceWinner;}
        }

        //check columns
        forj(4) {
            nx = 0; no = 0;
            fori(4) {
                if ( board[i][j] == 'X' ) ++nx;
                else if ( board[i][j] == 'O' ) ++no;
                else if ( board[i][j] == 'T' ) { ++no; ++nx; }
                else { ++np; }
            }
            if (nx == 4) { winner = status::xwon; goto announceWinner;}
            if (no == 4) { winner = status::owon; goto announceWinner;}
        }

        //check left->right diagonal
        nx = 0; no = 0;
        for (uint i = 0, j = 0; i < 4; ++i, ++j) {
            if ( board[i][j] == 'X' ) ++nx;
            else if ( board[i][j] == 'O' ) ++no;
            else if ( board[i][j] == 'T' ) { ++no; ++nx; }
            else { ++np; }
        }
        if (nx == 4) { winner = status::xwon; goto announceWinner;}
        if (no == 4) { winner = status::owon; goto announceWinner;}    

        //check left<-right diagonal
        nx = 0; no = 0;
        for (uint i = 0, j = 3; i < 4; ++i, --j) {
            if ( board[i][j] == 'X' ) ++nx;
            else if ( board[i][j] == 'O' ) ++no;
            else if ( board[i][j] == 'T' ) { ++no; ++nx; }
            else { ++np; }
        }
        if (nx == 4) { winner = status::xwon;}
        if (no == 4) { winner = status::owon;}
       
       announceWinner:
        cout << "Case #" << caseNumber << ": ";
        if (winner == status::xwon) cout << "X won\n";
        else if (winner == status::owon) cout << "O won\n";
        else if (np > 0) cout << "Game has not completed\n";
        else cout << "Draw\n";
    }
}