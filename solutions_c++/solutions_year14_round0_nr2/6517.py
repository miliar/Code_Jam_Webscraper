#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("input.in");
    ofstream out("output.out");
    int T;
    long double C, F, X, bT, cT, nT;
    in >> T;
    int num = 0;
    out.precision(7);
    while (T--)
    {
        cT = 0;
        num++;
        in >> C >> F >> X;
        double rate = 2;
        bT = X/rate;
        nT = C/rate + X/(rate+F);
        while (bT > nT)
        {
            cT += C/rate;
            bT = nT;
            rate += F;
            bT = cT + X/rate;
            nT = cT + C/rate + X/(rate+F);
        }
        out << fixed << "Case #" << num << ": " << bT << endl;
    }
    return 0;
}
