#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    char lfeed[32];
    ifstream inf;
    ofstream outf;
    inf.open("A.in");
    outf.open("A.out");
    inf.getline(lfeed,32);
    int T = atoi(strtok(lfeed,"\n"));
    for (int cases = 0 ; cases < T ; cases ++)
    {
        
        
        
        char **table = new char*[4];
        for (int k = 0 ; k < 4 ; k ++) table[k] = new char[4];
        for (int k = 0 ; k < 4 ; k ++)
        {
            inf.getline(lfeed,32);
            for (int l = 0 ; l < 4 ; l ++) table[k][l] = lfeed[l];
        }
        int win = 0;
        for (int k = 0 ; k < 4 ; k ++)
        {
            if (((table[k][0] == 'O') || (table[k][0] == 'T'))&&((table[k][1] == 'O') || (table[k][1] == 'T'))&&((table[k][2] == 'O') || (table[k][2] == 'T'))&&((table[k][3] == 'O') || (table[k][3] == 'T'))) {win = 1; break;}
            if (((table[k][0] == 'X') || (table[k][0] == 'T'))&&((table[k][1] == 'X') || (table[k][1] == 'T'))&&((table[k][2] == 'X') || (table[k][2] == 'T'))&&((table[k][3] == 'X') || (table[k][3] == 'T'))) {win = 2; break;}
        }
        if (!win)
        {
        for (int l = 0 ; l < 4 ; l ++)
        {
            if (((table[0][l] == 'O') || (table[0][l] == 'T'))&&((table[1][l] == 'O') || (table[1][l] == 'T'))&&((table[2][l] == 'O') || (table[2][l] == 'T'))&&((table[3][l] == 'O') || (table[3][l] == 'T'))) {win = 1; break;}
            if (((table[0][l] == 'X') || (table[0][l] == 'T'))&&((table[1][l] == 'X') || (table[1][l] == 'T'))&&((table[2][l] == 'X') || (table[2][l] == 'T'))&&((table[3][l] == 'X') || (table[3][l] == 'T'))) {win = 2; break;}
        }
        }
        if (!win)
        {

            if (((table[0][0] == 'O') || (table[0][0] == 'T'))&&((table[1][1] == 'O') || (table[1][1] == 'T'))&&((table[2][2] == 'O') || (table[2][2] == 'T'))&&((table[3][3] == 'O') || (table[3][3] == 'T'))) {win = 1;}
            if (((table[0][0] == 'X') || (table[0][0] == 'T'))&&((table[1][1] == 'X') || (table[1][1] == 'T'))&&((table[2][2] == 'X') || (table[2][2] == 'T'))&&((table[3][3] == 'X') || (table[3][3] == 'T'))) {win = 2;}
            if (((table[3][0] == 'O') || (table[3][0] == 'T'))&&((table[2][1] == 'O') || (table[2][1] == 'T'))&&((table[1][2] == 'O') || (table[1][2] == 'T'))&&((table[0][3] == 'O') || (table[0][3] == 'T'))) {win = 1;}
            if (((table[3][0] == 'X') || (table[3][0] == 'T'))&&((table[2][1] == 'X') || (table[2][1] == 'T'))&&((table[1][2] == 'X') || (table[1][2] == 'T'))&&((table[0][3] == 'X') || (table[0][3] == 'T'))) {win = 2;}
        }        
        if (win == 1) {outf << "Case #" << cases+1 << ": O won" << endl;}
        else if (win == 2) {outf << "Case #" << cases+1 << ": X won" << endl;}
        if (win ==0){
        bool found = false;
        for (int k = 0 ; k < 4 ; k ++)
        {
            for (int l = 0 ; l < 4 ; l ++){ if (table[k][l] == '.'){found = true; break;}}
        }
        if (found) {outf << "Case #" << cases+1 << ": Game has not completed" << endl;}
        else {outf << "Case #" << cases+1 << ": Draw" << endl;}
        }
        

        
        
        for (int k = 0 ; k < 4 ; k ++) delete[] table[k];
        delete[] table;
        inf.getline(lfeed,32);
    }
    outf.close();
    return 0;
}
