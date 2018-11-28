#include <cstdlib>
#include <limits>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <iterator>
#ifdef BUG
    #include "debug.hpp"
#else
    #define DEBUG(var)
#endif
using namespace std;
/* ------------------------------ */

int main( const int argc, char * argv [])
{
    fstream fin, fout;
    fin.open( "input.txt", fstream::in );
    fout.open( "output.txt", fstream::out );

    size_t k;
    fin >> k;

    for( size_t i = 0; i < k; ++ i )
    {
        size_t n;
        string row;
        fin >> n >> row;

        size_t acc = 0;
        size_t val = 0;

        for( size_t j = 0; j < row.length(); acc += row[j++] - '0' )
            if( acc < j && row[j] != '0' )
            {
                const size_t inc = j - acc;
                val += inc;
                acc += inc;
            }

        fout << "Case #" << i + 1 << ": " << val << '\n';
    }

    fin.close();
    fout.close();
}
