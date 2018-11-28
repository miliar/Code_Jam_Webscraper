#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

ifstream lire("input.in", ios::in);
ofstream ecrire("output.txt", ios::out);

int main()
{
    int T;
    lire >> T;
    ecrire.precision(15);
    for (int k = 1; k <= T; k++)
    {
        double C, F, X, P = 2.0, t = 0.0;
        lire >> C >> F >> X;
        while (C / P + X / (P + F) < X / P)
        {
            t += C / P;
            P += F;
        }
        ecrire << "Case #" << k << ": " << t + X / P << endl;
    }
    return 0;
}
