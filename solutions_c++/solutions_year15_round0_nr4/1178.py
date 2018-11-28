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

template< class T > inline istream &
operator>>( istream & fin, vector< T > & a ) {
if(! a.size()){ size_t n; fin >> n; a.resize( n ); }
for( auto & u: a) fin >> u; return fin; }

/* ------------------------------ */

bool isrich(const int x, const int a, const int b)
{
    if(7 < x + 1) /* hole inside */
        return true;

    if((a + 1) * 2 < x + 2 ) /* long L */
        return true;

    if((a * b) % x != 0 ) /* non-divisible */
        return true;

    /* single fork */
    if( b + 3 < x + 1 || ( a < 3 && 5 < x + 1 ))
        return true;

    if( x == 4 && a == 2 )
        return true;

    return false;
}

int main( const int argc, char * argv [])
{
    fstream fin, fout;
    fin.open( "input.txt", fstream::in );
    fout.open( "output.txt", fstream::out );

    size_t k;
    fin >> k;

    for( size_t i = 0; i < k; ++ i )
    {
        int x, r, c;
        fin >> x >> r >> c;

        fout << "Case #" << i + 1 << ": "
             << (isrich(x, min(r, c), max(r, c)) ? "RICHARD" : "GABRIEL" )
             << '\n';
    }

    fin.close();
    fout.close();
}
