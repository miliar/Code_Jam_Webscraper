#include <fstream>
#include <iostream>
#include <string>
using namespace std;

enum STATE {
    INITIAL,
    XWIN,
    OWIN,
    DRAW,
    INCOMP
};

string stateStr(STATE s) {
    switch (s) {
        case XWIN:
            return "X won";
            
        case OWIN:
            return "O won";
            
        case DRAW:
            return "Draw";
            
        case INCOMP:
            return "Game has not completed";

        default:
            return "idk";
    };
}

struct BoardMachine {
    STATE s;
    BoardMachine() : s(INITIAL) {}

    STATE state(void) const {
        return s;
    }

    // Takes in the state for a set (row/col/diag) and updates the board state
    void transition(STATE setState) {
        switch (s) {
            // Draws and initial states can transition to anything
            case DRAW:
            case INITIAL:
                s = setState;
                break;

            // Incomplete games can be come complete games only
            case INCOMP:
                switch (setState) {
                    case OWIN:
                    case XWIN:
                        s = setState;
                        break;
                }
                break;
                
            // Once a game is determined to be complete, it stays that way
            case OWIN:
            case XWIN:
                break;
        }
    }
};

// Meant to be run on a sequence of 4 characters representing a row/column/diagonal
struct StateMachine {
    STATE s;
    StateMachine() : s(INITIAL) {}

    STATE state(void) const {
        return s;
    }
    
    STATE transition(char c) {
        switch (s) {
            case INITIAL:
                switch (c) {
                    case '.':
                        s = INCOMP;
                        break;
                        
                    case 'X':
                        s = XWIN;
                        break;
                        
                    case 'O':
                        s = OWIN;
                        break;
                }
                break;
                
            case XWIN:
                switch (c) {
                    case '.':
                        s = INCOMP;
                        break;
                        
                    case 'O':
                        s = DRAW;
                        break;
                }
                break;
                
            case OWIN:
                switch (c) {
                    case '.':
                        s = INCOMP;
                        break;
                        
                    case 'X':
                        s = DRAW;
                        break;
                }
                break;
            case DRAW:
                switch (c) {
                    case '.':
                        s = INCOMP;
                        break;
                }
                break;
                
            case INCOMP:
                break;
        }
    }
};

int main(void) {
    string baseName;
    cin >> baseName;
    
    char board[4][4];
    fstream fin(baseName + ".in", fstream::in);
    fstream fout(baseName + ".out", fstream::out);

    int T;
    fin >> T;

    for (int case_num = 1; case_num <= T; ++case_num) {
        fout << "Case #" << case_num << ": ";
        
        BoardMachine bs;
        bool done = false;

        // Read in the board
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                fin >> board[i][j];
            }
            fin.ignore();
        }
        
        for (int i = 0; !done && i < 4; ++i) {
            // State machine for processing this row
            StateMachine s;
            for (int j = 0; j < 4; ++j) {
                s.transition(board[i][j]);
            }
            bs.transition(s.state());
            if (bs.state() == XWIN || bs.state() == OWIN) {
                done = true;
                fout << stateStr(bs.state()) << endl;
            }
        }

        // Run over columns
        for (int i = 0; !done && i < 4; ++i) {
            StateMachine s;
            for (int j = 0; j < 4; ++j) {
                s.transition(board[j][i]);
            }
            bs.transition(s.state());
            if (bs.state() == XWIN || bs.state() == OWIN) {
                done = true;
                fout << stateStr(bs.state()) << endl;
            }
        }

        if (!done) {
            // Run over diagonals, left = (0..4, 0..4) right = (0..4, 4..0)
            StateMachine sl, sr;
            for (int i = 0; !done && i < 4; ++i) {
                sl.transition(board[i][i]);
                sr.transition(board[i][3 - i]);
            }
            bs.transition(sl.state());
            bs.transition(sr.state());
            fout << stateStr(bs.state()) << endl;
        }
    }

    return 0;
}
