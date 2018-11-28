#include <QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QDebug>
#include <iostream>
#include <string.h>
using namespace std;

QString tempStorage;
QFile inputFile;

int numPuzzles;
int caseNumber;
int board[4][4];
int results[10];
bool dotPresent;
bool debug;

int getCharValue (QString text) {
    if (QString().compare(text,"X") == 0) { return 1; }
    if (QString().compare(text,"O") == 0) { return -1;}
    if (QString().compare(text,".") == 0) { dotPresent=true; return 0; }
    if (QString().compare(text,"T") == 0) { return 10;}

    return 10;
}

int whoWon (int result) {
    // Return 1 if X Won / 0 if Y Won / 2 if nobody won
    if (result == 4 || result == 13) { return 1; }
    if (result == -4 || result == 7) { return 0; }
    return 2;
}

void addUpResults() {

    // Horizontal Results
    results[0] = board[0][0] + board[0][1] + board[0][2] + board[0][3];
    results[1] = board[1][0] + board[1][1] + board[1][2] + board[1][3];
    results[2] = board[2][0] + board[2][1] + board[2][2] + board[2][3];
    results[3] = board[3][0] + board[3][1] + board[3][2] + board[3][3];

    // Vertical Results
    results[4] = board[0][0] + board[1][0] + board[2][0] + board[3][0];
    results[5] = board[0][1] + board[1][1] + board[2][1] + board[3][1];
    results[6] = board[0][2] + board[1][2] + board[2][2] + board[3][2];
    results[7] = board[0][3] + board[1][3] + board[2][3] + board[3][3];

    // Diagonals
    results[8] = board[0][0] + board[1][1] + board[2][2] + board[3][3];
    results[9] = board[0][3] + board[1][2] + board[2][1] + board[3][0];

    // Debug Output
    if (debug == true) {
        for (int i=0; i<=9; i++) { QTextStream(stdout) << results[i] << ":"; }
        QTextStream(stdout) << "----";
    }
}

void calculateResults() {

    int winner = -1;
    for (int i=0; i<=9; i++) {
        if (whoWon(results[i]) == 0) { QTextStream(stdout) << "Case #" << caseNumber << ": O won"; return;}
        if (whoWon(results[i]) == 1) { QTextStream(stdout) << "Case #" << caseNumber << ": X won"; return;}
    }

    if (winner == -1 && dotPresent == true) {
        QTextStream(stdout) << "Case #" << caseNumber << ": Game has not completed"; return;
    } else {
        QTextStream(stdout) << "Case #" << caseNumber << ": Draw"; return;
    }
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    if (QString::compare(argv[1],"-d") == 0) { debug = true; } else { debug = false; }

    inputFile.open (stdin, QIODevice::ReadOnly);
    QTextStream qtin(&inputFile);

    // Get number of puzzles
    tempStorage = qtin.readLine();

    // Get number of puzzles
    numPuzzles = tempStorage.toInt();

    for (int i=1; i <= numPuzzles; i++) {
        caseNumber = i;

        for (int j=0; j<=3; j++) {
            tempStorage = qtin.readLine();
            board[j][0] = getCharValue(tempStorage.mid(0,1));
            board[j][1] = getCharValue(tempStorage.mid(1,1));
            board[j][2] = getCharValue(tempStorage.mid(2,1));
            board[j][3] = getCharValue(tempStorage.mid(3,1));
        }

        tempStorage = qtin.readLine();
        // Debug Printout
        if (debug == true) { for (int x=0; x<=3; x++) { QTextStream(stdout) << board[x][0] << ":" << board[x][1] <<  ":" << board[x][2] <<  ":" << board[x][3] << "\n"; } }

        // Calculate Results
        addUpResults();
        calculateResults();
        if (caseNumber != numPuzzles) { QTextStream(stdout) << "\n"; }
        dotPresent=false;
    }

    return 0;
}
