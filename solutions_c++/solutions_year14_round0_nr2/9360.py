#include <fstream>
#include <iostream>
#include <conio.h>
#include <iomanip>

using namespace std;

double C, F, X;

double invTime(double pduration, double ptime, int stage) {
    double ncookie = 2 + stage * F, ctime = pduration + X / ncookie;

    if(ctime > ptime) {
        return ptime;
    } else {
        return invTime(pduration + C / ncookie, ctime, stage+1);
    }
}


int main() {
    int iterations;

    ifstream fin("abc3.txt");
    ofstream fout("out2.txt");

    fin >> iterations;
    for(int i = 0; i < iterations; i++) {
        fin >> C >> F >> X;

        fout << setprecision(20);
        fout << "Case #" << i + 1 << ": " << invTime(C/2, X / 2, 1) << endl;
    }

    getch();

    fout.close();
    fin.close();
    return 0;
}
