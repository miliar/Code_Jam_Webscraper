/*
 * g++ -g -std=c++11 -DBUG -D_GLIBCXX_DEBUG -Wall -Wfatal-errors -o code-jam{,.cpp}
 * g++ -O3 -std=c++11 -Wall -Wfatal-errors -o code-jam{,.cpp}
 */
#include <bits/stdc++.h>
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

/* how many customers will sit down by tic + epsilon minute */
inline int64_t count_sits( const int64_t tic,
        const vector< int64_t > & barber )
{
    int64_t val = 0;

    for( const auto & b: barber )
        val += tic / b + 1LL;

    return val;
}

size_t xsolve(const int64_t n,
        const vector< int64_t > & b )
{
    int64_t ub = 1;
    while( count_sits( ub, b ) < n )
        ub *= 2LL;

    int64_t lb = -1LL;
    while( lb + 1 < ub )
    {
        const auto tic = (lb + ub) >> 1;
        if( count_sits( tic, b ) < n )
            lb = tic;
        else
            ub = tic;
    }

    const auto tic = ub;
    DEBUG( tic );

    if( tic == 0 )
        return n;

    auto offset = n - count_sits( tic - 1LL , b );

    for( size_t i = 0; i < b.size(); ++ i )
    {
        if( tic % b[ i ] == 0 )
            -- offset;

        if( ! offset )
            return i + 1;
    }
}

int main( const int argc, char * argv [])
{
    fstream fin, fout;
    fin.open("input.in", fstream::in);
    fout.open("output.txt", fstream::out);

    size_t t;
    fin >> t;

    for( size_t i = 0; i < t; ++ i )
    {
        int64_t b, n;
        fin >> b >> n;
        vector<  int64_t > m(b);
        fin >> m;

        fout << "Case #" << i + 1 << ": " << xsolve( n, m ) << '\n';
    }

    fin.close();
    fout.close();
}
