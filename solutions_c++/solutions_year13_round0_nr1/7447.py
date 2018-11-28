#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool checkWin(int sum);
void determineWinner(int id, string& out);

int main() {
    ifstream in("Alarge.in");
    ofstream out("output.out");

    if (in.fail()) {
        cout << "ifile error\n";
        exit(10);
    }
    if (out.fail()) {
        cout << "ofile error\n";
        exit(20);
    }

    int cases=0, id=0, rowSum[4]={0}, colSum[4]={0}, diagSum[2]={0}, gameSum=0;
    int row=0, col=0, diag=0, rowsRead=0;
    char space, board[4][4]={0};
    string winner;
    bool hasT=false;
    in >> cases;

    for (int i=1; i<=cases; i++) {        
        // cout << "Case #: " << i << endl;

        // Read a case
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                in >> board[row][col];
                // cout << board[row][col];
            }
            in.get();

            // cout << endl;
        }

        // Evaluate a case
        for (row=0; row<4; row++) {
            for (col=0; col<4; col++) {
                space = board[row][col];

                switch (space) {
                case 'X': id=1; break;
                case 'O': id=5; break;
                case 'T': id=50; hasT=true; break;
                default: id=0; break;
                }

                gameSum+=id;
                rowSum[row]+=id;
                colSum[col]+=id;
                if (row == col) {
                    diagSum[0]+=id;
                } else if (row + col == 3) {
                    diagSum[1]+=id;
                }
            }

            // Check row for win
            if (checkWin(rowSum[row])) {
                determineWinner(rowSum[row], winner);
                row = 5;
            }
        }
        
        if (row < 5) {
            // Check columns for win
            for (col=0; col<4; col++) {
                if (checkWin(colSum[col])) {
                    determineWinner(colSum[col], winner);
                    col = 5;
                }
            }

            if (col < 5) {
                // Check diagonals for win
                for (diag=0; diag<2; diag++) {
                    if (checkWin(diagSum[diag])) {
                        determineWinner(diagSum[diag], winner);
                        diag = 5;
                    }
                }

                if (diag < 5) {
                    // Output Draw or Game not complete
                    if ((gameSum < 48 && !hasT) || (gameSum < 93 && hasT)) {
                        winner = "Game has not completed";
                    } else {
                        winner = "Draw";
                    }
                }
            }
        }        
        out << "Case #" << i << ": " << winner << endl;        

        // Reset all values for new case
        for (int k=0; k<4; k++) {
            rowSum[k]=colSum[k]=0;
        }
        diagSum[0]=diagSum[1]=0;
        row=col=diag=gameSum=0;
        hasT=false;
    }

    in.close();
    out.close();
    
    return 0;
}

bool checkWin(int sum) {
    return sum % 4 == 0 && (sum / 4 == 1 || sum / 4 == 5) || sum == 53 || sum == 65;
}

void determineWinner(int id, string& out) {    
    id /= 4;
    switch (id) {
    case 1: 
    case 13: out = "X won"; break;
    case 5: 
    case 16: out = "O won"; break;
    default: out = "No one wins"; break;
    }
}