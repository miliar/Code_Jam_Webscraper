#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
using namespace std;

const char *infile = "B-large.in";
const char *outfile = "pb-large.out";

double getAns(double C, double F, double X) {
    double passed=0;
    double pro=2;
    while (C + pro*X/(pro+F) < X) {
        passed += C / pro;
        pro += F;
    }
    return passed + X / pro;
}

int main() {
    ifstream fin(infile);
    assert(fin);
    ofstream fout(outfile);
    assert(fout);
    fout.setf(ios::fixed);
    
    int test;
    fin >> test;
    for (int current=1; current<=test; current++) {
        double C, F, X;
        fin >> C >> F >> X;
        fout << "Case #" << current << ": " << setprecision(7) << getAns(C, F, X) << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
