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
    ifstream fin("B2.in");
    fstream fout("B.out", ios::out);
    int T;
    fin >> T;
    for (int zzz = 1; zzz <= T; zzz++) {
        fout << "Case #" << zzz << ": ";
        double C, F, X;
        fin >> C >> F >> X;
        double R = 2, t = 0;
        while (true) {
            if (X * F - C * (R + F) < 0) {
                t += X / R;
                break;
            } else {
                t += C / R;
                R += F;
            }
        }
        fout << setprecision(7) << t << endl;
    }
    fout.close();
    return 0;
}
