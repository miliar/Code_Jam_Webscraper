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

int main( const int argc, char * argv [])
{
    fstream fin, fout;
    fin.open("input.in", fstream::in);
    fout.open("output.txt", fstream::out);

    size_t t;
    fin >> t;

    for( size_t i = 0; i < t; ++ i )
    {
        vector< int > a;
        fin >> a;

        const auto n = a.size();
        vector< int > b( n );

        adjacent_difference(begin(a), end(a), begin(b));
        int fst = 0;
        for( auto i = begin(b) + 1; i != end(b); ++ i )
            fst += max( -*i, 0 );

        const auto r = max(0, - * min_element(begin(b) + 1, end(b)));

        int snd = 0;
        for( auto i = begin(a); i + 1 != end(a); ++ i )
            snd += r < *i + 1 ? r : *i;


        fout << "Case #" << i + 1 << ": " << fst << ' ' << snd << '\n';
    }

    fin.close();
    fout.close();
}
