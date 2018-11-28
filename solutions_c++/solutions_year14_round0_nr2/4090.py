#include <iostream>
#include <fstream>
#include <iomanip>
#include <map>
using namespace std;

double run_once(double C, double F, double X) {
    double rate = 2;
    double total = 0;
    while (true) {
        double ttw = X / rate;
        double ttb = C / rate + X / (rate + F);
        if (ttw <= ttb) return total + ttw;
        total += C / rate;
        rate += F;
    }
}

int main() {
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int N; fin >> N;
    double C, F, X;
    for (int i=0; i<N; i++) {
        fin >> C >> F >> X;
        fout << "Case #" << i+1 << ": ";
        fout << fixed << setprecision(7) << run_once(C, F, X);
        fout << endl;
    }
    return 0;
}
