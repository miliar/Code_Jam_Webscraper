//A
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("input.in");
    ofstream out("output.out");
    int T, P, Q, counter;
    char slash;
    int generace;
    in >> T;
    counter = 0;
    while (T--)
    {
        counter++;
        in >> P;
        in >> slash;
        in >> Q;
        generace = 0;
        while (Q%2 == 0)
        {
            if (P < Q)
                generace++;
            Q /= 2;
        }
        if (Q == 1 || P == Q)
            out << "Case #" << counter << ": " << generace << endl;
        else
            out << "Case #" << counter << ": " << "impossible" << endl;
    }
    return 0;
}
