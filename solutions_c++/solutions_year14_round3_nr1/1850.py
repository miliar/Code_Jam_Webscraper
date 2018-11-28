

#include <cstdlib>
#include <cstdio>
#include <cassert>

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;


int main(int argc, char ** argv)
{
    std::string line;
    // read the tests count
    int T = 0;
    cin >> T;
    getline(cin, line);
    // run the test cases
    int t = 0;
    while (t < T)
    {
        ++t;
        // load the values
        int P = 0, Q = 0;
        int * ptrVal = &P;
        getline(cin, line);
        for (std::string::const_iterator ic = line.begin(); ic != line.end(); ++ic)
        {
            if (*ic == '/')
                ptrVal = &Q;
            else
                *ptrVal = *ptrVal * 10 + (*ic - '0');
        }
        // solve
        int X = 0, G = 0;
        bool impossible = false;
        while (Q > 1)
        {
            ++G;
            if ((Q & 0x1) || (G > 40))
            {
                // impossible
                X = 0;
                break;
            }
            Q >>= 1;
            if (!X && P >= Q)
            {
                // found the generation
                X = G;
            }
        }
        cout << "Case #" << t << ": ";
        if (X)
            cout << X;
        else
            cout << "impossible";
        cout << endl;
    }
    return EXIT_SUCCESS;
}
