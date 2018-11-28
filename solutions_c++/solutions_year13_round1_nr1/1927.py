#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

double r, t;
int T;

int main() {
    fin >> T;
    for(int it=1; it <= T; it++) {
        fin >> r >> t;
        long num = (long) ( sqrt( (2*r-1)*(2*r-1) + 8*t ) - (2*r-1) )/4;
        fout << "Case #" << it << ": " << num << endl;
    }
}
