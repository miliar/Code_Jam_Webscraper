#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <cmath>
using namespace std;
typedef vector<int> VI;
#define REP( i, m, n ) for ( int i = (int)( m ); i < (int)( n ); ++i )

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int input;
    cin >> input;

    vector<vector<char>> probset;

    REP(i, 0, input) {
        vector<char> board;
        
        for (int j = 0; j < 16; j += 4) {
            char a, b, c ,d;
            cin >> a >> b >> c >> d;
            board.push_back(a);
            board.push_back(b);
            board.push_back(c);
            board.push_back(d);
        }
        
        probset.push_back(board);
    }

    REP(k, 0, input) {
    
        bool X = false;
        bool O = false;
        bool dot = false;

        { // column
            REP(i, 0, 4) {
                int cX = 0;
                int cO = 0;
                bool cdot = false;
                
                vector<char> board = probset[k];

                for(int j = i; j < 16; j += 4) {
                    if (board[j] == 'X' || board[j] == 'T') {
                        ++cX;
                    } else if (board[j] == '.') {
                        cdot = true;
                        break;
                    } else { break; }
                }

                for(int j = i; j < 16; j += 4) {
                    if (cX == 4)    break;

                    if (board[j] == 'O' || board[j] == 'T') {
                        ++cO;
                    } else if (board[j] == '.') {
                        cdot = true;
                        break;
                    } else { break; }
                }
                
                if (cX == 4) { X = true; }
                if (cO == 4) { O = true; }
                dot = cdot;
            }
        } // column
    
        { // row
            int rX = 0;
            int rO = 0;
            bool rdot = false;
            
            vector<char> board = probset[k];
            
            for (int i = 0; i < 16; i+=4) {
                if (X || O)    break;
                
                rX = rO = 0;

                REP(j, i, j+4) {
                    if (board[j] == 'X' || board[j] == 'T') {
                        ++rX;
                    } else if (board[j] == '.') {
                        rdot = true;
                        break;
                    } else { break; }
                }
                if (rX == 4) { X = true; }

                REP(j, i, j+4) {
                    if (board[j] == 'O' || board[j] == 'T') {
                        ++rO;
                    } else if (board[j] == '.') {
                        rdot = true;
                        break;
                    } else { break; }
                }
                if (rO == 4) { O = true; }
            }
            
            dot = rdot;
        } // row

        { // diagonal
            int dX = 0;
            int dO = 0;
            bool ddot = false;
            
            vector<char> board = probset[k];

            for (int i = 0; i < 16; i+=5) {
                if (board[i] == 'X' || board[i] == 'T') {
                    ++dX;
                } else if (board[i] == '.') {
                    ddot = true;
                    break;
                } else { break; }
            }

            for (int i = 0; i < 16; i+=5) {
                if (board[i] == 'O' || board[i] == 'T') {
                    ++dO;
                } else if (board[i] == '.') {
                    ddot = true;
                    break;
                } else { break; }
            }
            if (dX == 4) { X = true; }
            if (dO == 4) { O = true; }
            
            dX = dO = 0;
            
            for (int i = 3; i < 13; i+=3) {
                if (board[i] == 'X' || board[i] == 'T') {
                    ++dX;
                } else if (board[i] == '.') {
                    ddot = true;
                    break;
                } else { break; }
            }

            for (int i = 3; i < 13; i+=3) {
                if (board[i] == 'O' || board[i] == 'T') {
                    ++dO;
                } else if (board[i] == '.') {
                    ddot = true;
                    break;
                } else { break; }
            }
            if (dX == 4) { X = true; }
            if (dO == 4) { O = true; }
            dot = ddot;

        } // diagonal
        
        if (X) {
            cout << "Case #" << k+1 << ": X won" << endl;
        } else if (O) {
            cout << "Case #" << k+1 << ": O won" << endl;
        } else if (dot) {
            cout << "Case #" << k+1 << ": Game has not completed" << endl;
        } else {
            cout << "Case #" << k+1 << ": Draw" << endl;
        }
    }
}
