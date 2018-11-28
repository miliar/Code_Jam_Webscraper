#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <conio.h>

using namespace std;

int main(void) {
    int iterations, rowcnt,cmp, row[4], inter[4];


    ifstream fin("abc.txt");
    ofstream fout("out.txt");

    fin >> iterations;
    for(int a = 0, i; a < iterations; a++) {
i = -1;
        for(int b = 0; b < 2; b++) {
            fin >> rowcnt;

            for(int c = 1; c < rowcnt; c++)
                fin >> cmp >> cmp>>cmp>>cmp;


            if(b == 0) {
                for(int d = 0; d < 4; d++)
                    fin >> row[d];

            } else {
                for(int d = 0; d < 4; d++) {
                    fin >> cmp;

                    for(int n = 0; n < 4; n++) {
                        if(row[n] == cmp) {
                            inter[++i] = cmp;
                        }
                    }
                }
            }

            for(int c = 0; c < 4 - rowcnt; c++)
                fin >> cmp >> cmp>>cmp>>cmp;

        }


        fout << "case #" << a + 1 << ": ";

        if(i == 0)
            fout << inter[i];
        else
            fout << (i == -1  ? "Volunteer cheated!" : "Bad magician!");

        fout << endl;

    }

    getch();
    return 0;
}
