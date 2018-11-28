#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

int main()
{
    std::ifstream in("in");
    std::ofstream out("out");

    int T;
    in >> T;

    short x, r, c;
    for(int caseNum = 1; caseNum <= T; ++caseNum)
    {
        out << "Case #" << caseNum << ": ";

        in >> x >> r >> c;

        if(c*r % x != 0)
        {
            out << "RICHARD\n";
            continue;
        }

        if(x == 4)
        {
            if((c >= 3 && r >= 4) || (c >= 4 && r >= 3))
            {
                out << "GABRIEL\n";
                continue;
            }
            else
            {
                out << "RICHARD\n";
                continue;
            }
        }

        if(x == 3)
        {
            if((c >= 3 && r >= 2) || (c >= 2 && r >= 3))
            {
                out << "GABRIEL\n";
                continue;
            }
            else
            {
                out << "RICHARD\n";
                continue;
            }
        }

        out << "GABRIEL\n";
    }

    return 0;
}
