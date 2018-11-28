#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>
#include <assert.h>
#include <unistd.h>

using namespace std;

int main(int argc, char** argv)
{
    assert(argc==2 && "Input missing.");
    assert(!access(argv[1],F_OK) && "Input file not exist.");

    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t c(1); c != nbCases+1; ++c)
    {
        int P,Q;
        char d;
        is >> P >> d >> Q;

        int nb(1);
        int x(P);
        bool impossible(false);
        while (true) {
            x = 2*x;
            if (x >= Q) x -= Q;
            if (x == 0) { break; }
            if (nb > 40) { impossible = true; break; }
            ++nb;
        }

        nb = 1;
        x = P;
        while (true) {
            x = 2*x;
            if (x >= Q) break;
            ++nb;
        }

        if (impossible) cout << "Case #" << c << ": impossible" << endl;
        else cout << "Case #" << c << ": " << nb << endl;
    }
}

