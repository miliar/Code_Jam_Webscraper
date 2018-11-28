#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream fin("D-small-attempt0.in");

    int T=0;
    fin >> T;

    ofstream fout("outputD.txt");

    for (int i=1; i<=T; i++) {
        int X, R, C;
        fin >> X >> R >> C;

        if (X == 1) {
            fout << "Case #" << i << ": GABRIEL\n";
        } else if (X == 2) {
            if ((R*C) % 2 == 0) fout << "Case #" << i << ": GABRIEL\n";
            else fout << "Case #" << i << ": RICHARD\n";
        } else {
            if ((R*C) % X != 0) fout << "Case #" << i << ": RICHARD\n";
            else if ((R*C) < X) fout << "Case #" << i << ": RICHARD\n";
            else if (R < X && C < X) fout << "Case #" << i << ": RICHARD\n";
            else if (R == 1 || C == 1) fout << "Case #" << i << ": RICHARD\n";
            else {
                if (X == 4 && R*C == 8) fout << "Case #" << i << ": RICHARD\n";
                else fout << "Case #" << i << ": GABRIEL\n";
            }
        }
    }

    return 0;
}
