#include <iostream>
#include <fstream>
using namespace std;

void fillArray(ifstream& isr, char B[][4]) {
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            char c = isr.get();
            if(isr.good() && c != '\n')
                B[i][j] = c;
            else {
                char c = isr.get();
                if(isr.good() && c != '\n')
                    B[i][j] = c;
                else {
                    char c = isr.get();
                    if(isr.good())
                        B[i][j] = c;
                }
            }
        }
    }
}

char checkRow(int row, char B[][4]) {
    char c = B[row][0];
    for(int j=1; j<4; j++)
        if(B[row][j] != c && B[row][j] != 'T')
            return 0;

    return c;
}

char checkCol(int col, char B[][4]) {
    char c = B[0][col];
    for(int i=1; i<4; i++)
        if(B[i][col] != c && B[i][col] != 'T')
            return 0;

    return c;
}

char checkDiag(char B[][4]) {
    char c = B[0][0];
    for(int i=1; i<4; i++)
        if(B[i][i] != c && B[i][i] != 'T')
            return 0;

    return c;
}

char checkDiagRev(char B[][4]) {
    char c = B[0][3];
    for(int i=1; i<4; i++)
        if(B[i][3-i] != c && B[i][3-i] != 'T')
            return 0;

    return c;
}

void drawORnotCompleted(ofstream& osr, char B[][4], int caseNum) {
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            if(B[i][j] == '.') {
                osr << "Case #" << caseNum << ": Game has not completed" << endl;
                return;
            }
        }
    }
    osr << "Case #" << caseNum << ": Draw" << endl;
}


int main() {
    ifstream is("small.in");
    ofstream os("output.in");
    int caseNumber = 10;
    int currentCaseNumber = 1;
    char A[4][4];
    char winner = 0;

    while(is.good() && currentCaseNumber <= caseNumber) {
        fillArray(is, A);

        for(int i=0; i<4 && !winner; i++) {
            if(A[i][0] != '.') {
                winner = checkRow(i, A);
                if(winner)
                    os << "Case #" << currentCaseNumber << ": " << winner << " won" << endl;
            }
        }

        for(int j=0; j<4 && !winner; j++) {
            if(A[0][j] != '.') {
                winner = checkCol(j, A);
                if(winner)
                    os << "Case #" << currentCaseNumber << ": " << winner << " won" << endl;
            }
        }

        if(!winner) {
            if(A[0][0] != '.') {
                winner = checkDiag(A);
                if(winner)
                    os << "Case #" << currentCaseNumber << ": " << winner << " won" << endl;
            }
        }

        if(!winner) {
            if(A[0][3] != '.') {
                winner = checkDiagRev(A);
                if(winner)
                    os << "Case #" << currentCaseNumber << ": " << winner << " won" << endl;
            }
        }

        if(!winner)
            drawORnotCompleted(os, A, currentCaseNumber);

        winner = 0;
        currentCaseNumber++;
    }

    is.close();
}
