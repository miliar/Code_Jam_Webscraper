#include <iostream>
#include <string.h>  
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <ctime>

using namespace std;

int main() {
    ifstream fin("A1.in");
    fstream fout("A.out", ios::out);
    int T;
    int A[4][4], B[4][4];
    fin >> T;
    for (int zzz = 1; zzz <= T; zzz++) {
        int a, b, c = 0, d;
        fin >> a;
        for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) fin >> A[i][j];
        fin >> b;
        for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) fin >> B[i][j];
        --a, --b;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                if (A[a][j] == B[b][k]) {
                    d = A[a][j];
                    c++;
                }
        fout << "Case #" << zzz << ": ";
        if (c == 0)
            fout << "Volunteer cheated!";
        else if (c == 1)
            fout << d;
        else
            fout << "Bad magician!";
        fout << endl;
    }
    fout.close();
    return 0;
}
