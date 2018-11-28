#include <fstream>
#include <string>
#include <iostream>

using namespace std;

string grid[4];
char ret;
int brX, brO, brT, brD;
ifstream fin;
ofstream fout;

void init() {
    brX = 0;
    brO = 0;
    brT = 0;
    brD = 0;
}

/*
void ispis() {
    for (int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j)
            cout << grid[i][j];
        cout << endl;
    }
    cout << endl;
}
*/

void provjera() {
    if (brX == 4 || brX == 3 && brT == 1)
        ret = 'X';
    else if (brO == 4 || brO == 3 && brT == 1)
        ret = 'O';
    else
        ret = ' ';
}

void horizontalCheck() {
    for (int i=0; i<4; ++i) {
        init();
        for (int j=0; j<4; ++j) {
            if (grid[i][j] == 'X') brX++;
            else if (grid[i][j] == 'O') brO++;
            else if (grid[i][j] == 'T') brT++;
        }
        //cout << brX << brO << brT << endl;
        provjera();
        if (ret != ' ')
            return;
    }
}

void diagonalCheck() {
    init();
    for (int i=0; i<4; ++i) {
        if (grid[i][i] == 'X') brX++;
        else if (grid[i][i] == 'O') brO++;
        else if (grid[i][i] == 'T') brT++;
    }
    provjera();
    if (ret != ' ')
        return;
    init();
    for (int i=0; i<4; ++i) {
        if (grid[3-i][i] == 'X') brX++;
        else if (grid[3-i][i] == 'O') brO++;
        else if (grid[3-i][i] == 'T') brT++;
    }
    provjera();
    if (ret != ' ')
        return;
}

void verticalCheck() {
    for (int i=0; i<4; ++i) {
        init();
        for (int j=0; j<4; ++j) {
            if (grid[j][i] == 'X') brX++;
            else if (grid[j][i] == 'O') brO++;
            else if (grid[j][i] == 'T') brT++;
        }
        provjera();
        if (ret != ' ')
            return;
    }
}

void tocka() {
    for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
            if (grid[i][j] == '.') {
                ret = '.';
                return;
            }
}

string solve() {
    //fin >> grid[0];
    for (int i=0; i<4; ++i) {
        fin >> grid[i];
    }

    //ispis();
    ret = ' ';
    horizontalCheck();

    if (ret == 'X')
        return "X won";
    else if (ret == 'O')
        return "O won";

    diagonalCheck();

    if (ret == 'X')
        return "X won";
    else if (ret == 'O')
        return "O won";

    verticalCheck();

    if (ret == 'X')
        return "X won";
    else if (ret == 'O')
        return "O won";
    tocka();
    if (ret == '.')
        return "Game has not completed";
    else
        return "Draw";
}

int main() {
    int test;
    fin.open("tictac.in");
    fout.open("tictac.out");

    fin >> test;

    for (int i=0; i<test; ++i) {
        fout << "Case #" << i+1 << ": " << solve() << endl;
    }

    return 0;
}
