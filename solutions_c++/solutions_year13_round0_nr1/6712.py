#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>

#define ll long long

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

enum Cell {
    EMPTY,
    X,
    O,
    T,
};

Cell position [4][4];

int Tc;

bool check(Cell figure) {
    bool result = false;
    for (int i=0; i < 4; i++) {
        bool ok = true;
        for (int j=0; j < 4; j++) {
            if ((position [i][j] == T) || (position [i][j] == figure)) {
            } else {
                ok = false;
            }
        }
        if (ok) {
            return true;
        }
    }

    for (int j=0; j < 4; j++) {
        bool ok = true;
        for (int i=0; i < 4; i++) {
            if ((position [i][j] == T) || (position [i][j] == figure)) {
            } else {
                ok = false;
            }
        }

        if (ok) {
            return true;
        }
    }

    result = true;
    for (int i=0; i < 4; i++) {
        if(!((position [i][i] == T) || (position [i][i] == figure))) {
            result = false;
        }
    }
    if (result) return true;

    result = true;
    for (int i=0; i < 4; i++) {
        if (!((position [i][3-i] == T) || (position [i][3-i] == figure))) result = false;
    }

    return result;
}

int main () {
    in >> Tc;
    for (int t=0; t < Tc; t++) {
        int empty = 0;
        for (int i=0; i < 4; i++) {
            for (int j=0; j < 4; j++) {
                char ch;
                in >> ch;
                Cell c;
                if (ch == '.') {
                    c = EMPTY;
                } else if (ch == 'X') {
                    c = X;
                } else if (ch == 'O') {
                    c = O;
                } else {
                    c = T;
                }


                position[i][j] = c;
                if (position[i][j] == EMPTY) empty++;
            }
        }

        bool f1 = check(X);
        if (f1) {
            out << "Case #" << t+1 << ": " << "X won" << endl;
            continue;
        }

        bool f2 = check(O);
        if (f2) {
            out << "Case #" << t+1 << ": " << "O won" << endl;
            continue;
        }

        if (empty == 0) {
            out << "Case #" << t+1 <<": " << "Draw" << endl;
        } else {
            out << "Case #" << t+1 << ": " << "Game has not completed" << endl;
        }
    }
}
