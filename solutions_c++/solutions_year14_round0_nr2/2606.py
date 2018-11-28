#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t c(1); c != nbCases+1; ++c)
    {
        double C,F,X;
        is >> C >> F >> X;

        double time(0.0);
        double curf(2.0);

        for(;;) {
            
            if ( X/curf < (X/(curf+F) + C/curf) ) {
                time += X / curf;
                break;
            } else {
                time += C / curf;
                curf += F;
            }
        }

        cout << "Case #" << c << ": " << fixed << setprecision(7) << time << endl;
    }
}

