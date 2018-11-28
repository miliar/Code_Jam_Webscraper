/*
 * g++ -g -std=c++11 -dbug -d_glibcxx_debug -wall -wfatal-errors -o code-jam{,.cpp}
 * g++ -O3 -std=c++11 -Wall -Wfatal-errors -o code-jam{,.cpp}
 */
#include <cstdlib>
#include <limits>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <map>
#include <unordered_map>
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

bool isijk( const vector< int > & a,
            const vector< int > & b,
            const vector< vector< int > > & rule )
{
    const auto n = a.size();
    int left = 0;

    for( size_t i = 0; i < n; ++ i )
    {
        left = rule[ left ][ a[ i ] ];

        if( left == 1 )
        {
            int mid = 0;

            for( size_t j = i + 1; j + 1 < n; ++ j )
            {
                mid = rule[ mid ][ a[ j ] ];

                if( mid == 2 && b[ j + 1 ] == 3 )
                {
                    DEBUG( make_pair( i + 1, j - i ));
                    return true;
                }
            }
        }
    }

    return false;
}


int main( const int argc, char * argv [])
{
    fstream fin, fout;
    fin.open( "input.txt", fstream::in );
    fout.open( "output.txt", fstream::out );

    vector< vector< string > > table = {{"1",  "i",  "j",  "k"},
                                        {"i", "-1",  "k", "-j"},
                                        {"j", "-k", "-1",  "i"},
                                        {"k",  "j", "-i", "-1"}};

    const unordered_map< string, int > m = {
        { "1", 0}, { "i", 1}, { "j", 2}, { "k", 3},
        {"-1", 4}, {"-i", 5}, {"-j", 6}, {"-k", 7}};

    vector< vector< int > > rule( 8, vector< int >( 8 ));
    for( int i = 0; i < 8; ++ i )
        for( int j = 0; j < 8; ++ j )
            if(( i < 4 && j < 4 ))
                rule[ i ][ j ] = m.at( table[ i ][ j ]);
            else if ( 3 < i && 3 < j )
                rule[ i ][ j ] = m.at( table[ i - 4 ][ j - 4 ]);
            else if( 3 < i )
            {
                const auto w  = m.at( table[ i - 4 ][ j ] );
                rule[ i ][ j ] = w < 4 ? w + 4 : w - 4;
            }
            else
            {
                const auto w  = m.at( table[ i ][ j - 4 ] );
                rule[ i ][ j ] = w < 4 ? w + 4 : w - 4;
            }

    DEBUG( rule );

    size_t k;
    fin >> k;

    vector< int > a, b;

    for( size_t t = 0; t < k; ++ t )
    {
        a.clear();
        b.clear();

        size_t x, l;
        string str;
        fin >> l >> x >> str;

        if( 12 < x )
            x = (x - 12) % 4 + 12;

        a.reserve( x * l );

        for( const auto & w: str )
            a.push_back( w == 'i' ? 1 : w == 'j' ? 2 : 3 );

        for( size_t i = l; i < x * l; ++ i )
            a.push_back( a[i - l] );

        b.resize( x * l );
        b.back() = a.back();

        for( size_t i = x * l - 2; i < (size_t) (x * l); -- i )
            b[ i ] = rule[ a[ i ]][ b[ i + 1 ]];

        fout << "Case #" << t + 1 << ": "
             << (isijk(a, b, rule) ? "YES" : "NO") << '\n';

        if( t % 10 == 0 )
            cout << t << '\n';
    }

    fin.close();
    fout.close();
}
