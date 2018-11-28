#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

struct Case {
    double C; 
    double F;
    double X;
    double ans;
};

void solve(Case* c) {
    double currentRate = 2;
    double tempTime = 0;
    double X = c->X;
    double C = c->C;
    double F = c->F;
    while ( (X/currentRate ) > (C/currentRate + X/(currentRate+F)) ) {
        tempTime += C/currentRate;
        currentRate += F;
    }
    c->ans = tempTime + X/currentRate;
}

int main(int argc, char** argv) {
    int numTests;
    ifstream in(argv[1]);
    ofstream out("output.out");
    in >> numTests;
    Case* cases = new Case[numTests];
    for(int i = 0; i < numTests; i++) {
        double C, F, X;
        in >> C;
        in >> F;
        in >> X;
        cases[i].C = C;
        cases[i].F = F;
        cases[i].X = X;
    }

    out << fixed << setprecision(7);

    #pragma omp parallel for
    for(int i = 0; i < numTests; i++) {
        solve(&cases[i]);
    }

    for (int i = 0; i < numTests; i++)
        out << "Case #" << (i+1) << ": " << cases[i].ans << '\n';

    out.close();

    delete[] cases;

    return 0;
}
