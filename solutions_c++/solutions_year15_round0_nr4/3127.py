#include <iostream>
#include <fstream>
using namespace std;

ifstream input;
ofstream output;

int main() {
    input.open("D-small-attempt4.in");
    output.open("output.txt");
    int n;
    input >> n;
    for (int i=0; i<n; i++) {
        int X, R, C;
        input >> X >> R >> C;

        string winner;
        if (R*C < X || R*C%X != 0) {
            winner = "RICHARD";
        } else {
            if (X == 1) 
                winner = "GABRIEL";
            else if (X == 2) 
                winner = "GABRIEL";
            else if (X == 3) {
                if (R*C == 3)
                    winner = "RICHARD";
                else
                    winner = "GABRIEL";
            } else {
                if (R*C == 4)
                    winner = "RICHARD";
                else if (R*C == 8)
                    winner = "RICHARD";
                else
                    winner = "GABRIEL";
            }
        }

        output << "Case #" << i+1 << ": " << winner << "\n";

    }
    input.close();
    output.close();

    return 0;
}
