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
template< class T1, class T2 > inline istream &
operator>>( istream & fin, pair< T1, T2 > & pr )
{ fin >> pr.first >> pr.second; return fin; }
template< class T > inline istream &
operator>>( istream & fin, vector< T > & a ) {
if(! a.size()){ size_t n; fin >> n; a.resize( n ); }
for( auto & u: a) fin >> u; return fin; }
/* ------------------------------ */

inline size_t resolve( const vector< long double > & a )
{
    const int n = a.size() / 2;
    int val = 0;

    for( auto iter=begin(a); iter != begin(a) + n ; ++ iter )
    {
        const auto last = upper_bound( iter, end(a), *iter + M_PI + 1e-10L );
        val = max( val, (int)(last - iter ));
    }

    return max(0, n - val);
}

vector< size_t > xsolve( const vector< pair< int, int > > & a )
{
    const auto n = a.size();
    vector< size_t > out;
    out.reserve( n );

    vector< long double > t;
    t.reserve( n * 2  );

    for( size_t i = 0; i < n; ++ i )
    {
        t.clear();
        for( size_t j = 0; j < n; ++ j )
            if( j != i )
            {
                const long double dx = a[j].first - a[i].first;
                const long double dy = a[j].second - a[i].second;
                t.push_back(atan2( dx, dy ));
            }

        sort( begin(t), end(t) );
        for( size_t j = 0; j + 1 < n; ++ j )
            t.push_back( t[j] + 2.0L * M_PI );

        out.push_back( resolve( t ) );
    }

    return out;
}

int main( const int argc, char * argv [])
{
    fstream fin, fout;
    fin.open("input.in", fstream::in);
    fout.open("output.txt", fstream::out);

    cout << setprecision( 20 ) << M_PI << '\n';
    cout << setprecision( 20 ) << 1e-8L << '\n';

    long double dx = 2e6;
    long double dy = 0;

    cout << setprecision( 20 ) << atan2( dx, dy ) << '\n';
    cout << setprecision( 20 ) << atan2( dx, dy + 1 ) << '\n';
    cout << setprecision( 20 ) << atan2( dx, dy - 1 ) << '\n';

    const auto base = atan2( dx, dy );
    cout << setprecision( 20 ) << base - atan2( dx, dy + 1 ) << '\n';
    cout << setprecision( 20 ) << base - atan2( dx, dy - 1 ) << '\n';


    size_t t;
    fin >> t;

    for( size_t i = 0; i < t; ++ i )
    {
        vector< pair< int, int > > a;
        fin >> a;
        const auto val = xsolve( a );

        fout << "Case #" << i + 1 << ':' << '\n';
        copy(begin(val), end(val), ostream_iterator< size_t >(fout, "\n"));
    }

    fin.close();
    fout.close();
}
