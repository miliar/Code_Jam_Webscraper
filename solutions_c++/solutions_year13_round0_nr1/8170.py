#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>

#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    ifstream input ("A-small-attempt0.in");
    ofstream output ("tic.out");

    int T;
    char empty;

    input >> T;

    for (int i=0; i<T; i++){
        char table[4][4];
        memset (table, '.' ,16);
        bool space=false;
        for (int ii=0; ii<4; ii++){
            for (int jj=0; jj<4; jj++){
                input >> table[ii][jj];
                if (table[ii][jj]=='.'){
                    space=true;
                }
            }
        }

        if (((table[0][0]=='X') || (table[0][0]=='T')) &&
            ((table[0][1]=='X') || (table[0][1]=='T')) &&
            ((table[0][2]=='X') || (table[0][2]=='T')) &&
            ((table[0][3]=='X') || (table[0][3]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][0]=='O') || (table[0][0]=='T')) &&
            ((table[0][1]=='O') || (table[0][1]=='T')) &&
            ((table[0][2]=='O') || (table[0][2]=='T')) &&
            ((table[0][3]=='O') || (table[0][3]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[1][0]=='X') || (table[1][0]=='T')) &&
            ((table[1][1]=='X') || (table[1][1]=='T')) &&
            ((table[1][2]=='X') || (table[1][2]=='T')) &&
            ((table[1][3]=='X') || (table[1][3]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[1][0]=='O') || (table[1][0]=='T')) &&
            ((table[1][1]=='O') || (table[1][1]=='T')) &&
            ((table[1][2]=='O') || (table[1][2]=='T')) &&
            ((table[1][3]=='O') || (table[1][3]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[2][0]=='X') || (table[2][0]=='T')) &&
            ((table[2][1]=='X') || (table[2][1]=='T')) &&
            ((table[2][2]=='X') || (table[2][2]=='T')) &&
            ((table[2][3]=='X') || (table[2][3]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[2][0]=='O') || (table[2][0]=='T')) &&
            ((table[2][1]=='O') || (table[2][1]=='T')) &&
            ((table[2][2]=='O') || (table[2][2]=='T')) &&
            ((table[2][3]=='O') || (table[2][3]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[2][0]=='X') || (table[2][0]=='T')) &&
            ((table[2][1]=='X') || (table[2][1]=='T')) &&
            ((table[2][2]=='X') || (table[2][2]=='T')) &&
            ((table[2][3]=='X') || (table[2][3]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[3][0]=='O') || (table[3][0]=='T')) &&
            ((table[3][1]=='O') || (table[3][1]=='T')) &&
            ((table[3][2]=='O') || (table[3][2]=='T')) &&
            ((table[3][3]=='O') || (table[3][3]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[0][0]=='X') || (table[0][0]=='T')) &&
            ((table[1][0]=='X') || (table[1][0]=='T')) &&
            ((table[2][0]=='X') || (table[2][0]=='T')) &&
            ((table[3][0]=='X') || (table[3][0]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][0]=='O') || (table[0][0]=='T')) &&
            ((table[1][0]=='O') || (table[1][0]=='T')) &&
            ((table[2][0]=='O') || (table[2][0]=='T')) &&
            ((table[3][0]=='O') || (table[3][0]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[0][1]=='X') || (table[0][1]=='T')) &&
            ((table[1][1]=='X') || (table[1][1]=='T')) &&
            ((table[2][1]=='X') || (table[2][1]=='T')) &&
            ((table[3][1]=='X') || (table[3][1]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][1]=='O') || (table[0][1]=='T')) &&
            ((table[1][1]=='O') || (table[1][1]=='T')) &&
            ((table[2][1]=='O') || (table[2][1]=='T')) &&
            ((table[3][1]=='O') || (table[3][1]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[0][2]=='X') || (table[0][2]=='T')) &&
            ((table[1][2]=='X') || (table[1][2]=='T')) &&
            ((table[2][2]=='X') || (table[2][2]=='T')) &&
            ((table[3][2]=='X') || (table[3][2]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][2]=='O') || (table[0][2]=='T')) &&
            ((table[1][2]=='O') || (table[1][2]=='T')) &&
            ((table[2][2]=='O') || (table[2][2]=='T')) &&
            ((table[3][2]=='O') || (table[3][2]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[0][3]=='X') || (table[0][3]=='T')) &&
            ((table[1][3]=='X') || (table[1][3]=='T')) &&
            ((table[2][3]=='X') || (table[2][3]=='T')) &&
            ((table[3][3]=='X') || (table[3][3]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][3]=='O') || (table[0][3]=='T')) &&
            ((table[1][3]=='O') || (table[1][3]=='T')) &&
            ((table[2][3]=='O') || (table[2][3]=='T')) &&
            ((table[3][3]=='O') || (table[3][3]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[0][0]=='X') || (table[0][0]=='T')) &&
            ((table[1][1]=='X') || (table[1][1]=='T')) &&
            ((table[2][2]=='X') || (table[2][2]=='T')) &&
            ((table[3][3]=='X') || (table[3][3]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][0]=='O') || (table[0][0]=='T')) &&
            ((table[1][1]=='O') || (table[1][1]=='T')) &&
            ((table[2][2]=='O') || (table[2][2]=='T')) &&
            ((table[3][3]=='O') || (table[3][3]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (((table[0][3]=='X') || (table[0][3]=='T')) &&
            ((table[1][2]=='X') || (table[1][2]=='T')) &&
            ((table[2][1]=='X') || (table[2][1]=='T')) &&
            ((table[3][0]=='X') || (table[3][0]=='T'))){
                output << "Case #" << i+1 << ": X won" << "\n";
            }
        else if (((table[0][3]=='O') || (table[0][3]=='T')) &&
            ((table[1][2]=='O') || (table[1][2]=='T')) &&
            ((table[2][1]=='O') || (table[2][1]=='T')) &&
            ((table[3][0]=='O') || (table[3][0]=='T'))){
                output << "Case #" << i+1 << ": O won" << "\n";
            }
        else if (space==true){
            output << "Case #" << i+1 << ": Game has not completed" << "\n";
        }
        else{
            output << "Case #" << i+1 << ": Draw" << "\n";
        }
    }

    //output << T;

    return 0;
}
