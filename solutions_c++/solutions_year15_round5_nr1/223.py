#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <list>
#include <deque>
#include <algorithm>

using namespace std;

class Solution
{
    int Result;
    int N, D;
    int S0, As, Cs, Rs;
    int M0, Am, Cm, Rm;

    vector< int > M;
    vector< int > S;

    vector< char > IsUsed;

    vector< vector< int > > Empl;

public:
	void Work()
	{
        int i, b, e;

        M.reserve( N );
        S.reserve( N );
        M.push_back( M0 );
        S.push_back( S0 );
        for( i = 1; i < N; ++i )
        {
            S.push_back( ( int )( ( ( long long )S.back() * As + Cs ) % Rs ) );
            M.push_back( ( int )( ( ( long long )M.back() * Am + Cm ) % Rm ) );
        }

        Empl.resize( N );
        for( i = 1; i < N; ++i )
            Empl[ M[ i ] % i ].push_back( i );

        vector< int > index;
        index.reserve( N );
        for( i = 0; i < N; ++i )
            index.push_back( i );

        sort( index.begin(), index.end(), [this]( int i, int j ) { return S[ i ] < S[ j ]; } );

        b = e = 0;
        IsUsed.resize( N, 0 );
        Result = 1;

        while( b < N )
        {
            while( e < N && S[ index[ e ] ] - S[ index[ b ] ] <= D )
                IsUsed[ index[ e++ ] ] = true;
            if( IsUsed[ 0 ] )
            {
                int c = Count( 0 );
                if( Result < c )
                    Result = c;
            }
            IsUsed[ index[ b++ ] ] = false;
        }
	}

    int Count( int k )
    {
        int i;
        if( !IsUsed[ k ] )
            return 0;
        int result = 1;
        for( i = 0; i < ( int )Empl[ k ].size(); ++i )
            result += Count( Empl[ k ][ i ] );
        return result;
    }

	void Read()
	{
		scanf( "%d%d\n", &N, &D );
        scanf( "%d%d%d%d", &S0, &As, &Cs, &Rs );
        scanf( "%d%d%d%d", &M0, &Am, &Cm, &Rm );
	}

	void Write( int t )
	{
        printf( "Case #%d: ", t );
		printf( "%d\n", Result );
	}
};

vector< Solution > solution;

int main()
{
	int i, t;
	scanf( "%d", &t );
	solution.resize( t );
	for( i = 0; i < t; ++i )
		solution[ i ].Read();
#pragma omp parallel for schedule(dynamic, 1)
	for( i = 0; i < t; ++i )
		solution[ i ].Work();
	for( i = 0; i < t; ++i )
		solution[ i ].Write( i + 1 );
	return 0;
}
