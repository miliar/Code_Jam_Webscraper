#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>

using namespace std;

#define INPUT "b.in"
#define OUTPUT "b.out"

#define EPS 0.000001

void read() {
    ifstream fin(INPUT);
    ofstream fout(OUTPUT);

    int tests; fin >> tests;
    
    for (int test = 1; test <= tests; test++) {
        double c; fin >> c;
        double f; fin >> f;
        double x; fin >> x;

        double v = 2.0;

        double res;

        if (x <= c) {
            res = x / v;
        } else {
            double tTotal = 0.0;
            
            while (true) {
                double tFarm = c / v + x / (v + f);
                double tSimp = x / v;

                if (tFarm < tSimp) {
                    tTotal += c / v;
                    v += f;
                } else {
                    break;
                }
            }

            res = tTotal + x / v;
        }

        fout << "Case #" << test << ": ";
        fout << fixed << setprecision(7) << res << "\n";
    }

    fin.close();
    fout.close();
}

int main() {
    read();    
    return 0;
}
