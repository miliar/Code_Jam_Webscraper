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
    static const int MAXWORD = 16;
    static const int INF = 100000000;
    static const int MAX_N_WORD = ( 1000 * 2 + 200 * 10 ) * 2 + 2 + 123;
    int Result;
    int N;

    map< string, int > WordId;
    vector< vector< int > > Sentence;

    vector< vector< int > > M;
    bool IsUsed[ MAX_N_WORD ];
    int Prev[ MAX_N_WORD ];
    int Queue[ MAX_N_WORD ];

public:
    void FillSentence( const vector< int > &sentence )
    {
        int i, j;
        for( i = 0; i < ( int )sentence.size(); ++i )
        {
            for( j = 0; j < ( int )sentence.size(); ++j )
            {
                M[ sentence[ i ] * 2 + 1 ][ sentence[ j ] * 2 ] = INF;
            }
        }
    }

	void Work()
	{
        int i;
        Result = 0;

        int n = ( int )WordId.size();

        M.resize( n * 2 + 2, vector< int >( n * 2 + 2, 0 ) );

        for( i = 0; i < n; ++i )
            M[ i * 2 ][ i * 2 + 1 ] = 1;

        for( i = 0; i < N; ++i )
        {
            FillSentence( Sentence[ i ] );
        }

        for( i = 0; i < ( int )Sentence[ 0 ].size(); ++i )
        {
            M[ n * 2 + 1 ][ Sentence[ 0 ][ i ] * 2 ] = INF;
        }

        for( i = 0; i < ( int )Sentence[ 1 ].size(); ++i )
        {
            M[ Sentence[ 1 ][ i ] * 2 + 1 ][ n * 2 ] = INF;
        }

        while( true )
        {
            memset( IsUsed, 0, sizeof( IsUsed ) );
            memset( Prev, -1, sizeof( Prev ) );
    
            int head = 0, tail = 0;

            Queue[ tail++ ] = 2 * n + 1;
            IsUsed[ 2 * n + 1 ] = true;

            while( head != tail )
            {
                int curr = Queue[ head++ ];

                for( i = 0; i < 2 * n + 2; ++i )
                {
                    if( !IsUsed[ i ] && M[ curr ][ i ] > 0 )
                    {
                        Queue[ tail++ ] = i;
                        IsUsed[ i ] = true;
                        Prev[ i ] = curr;
                    }
                }
            }

            if( !IsUsed[ n * 2 ] )
                break;

            ++Result;

            for( i = 2 * n; Prev[ i ] != -1; i = Prev[ i ] )
            {
                M[ Prev[ i ] ][ i ] -= 1;
                M[ i ][ Prev[ i ] ] += 1;
            }
        }
	}

	void Read()
	{
        int i;
		scanf( "%d\n", &N );
        Sentence.resize( N );
        for( i = 0; i < N; ++i )
        {
            GetLine( Sentence[i] );
        }
	}

    void GetLine( vector< int > &sentence )
    {
        char word[ MAXWORD + 1 ];
        while( true )
        {
            while( true )
            {
                int c = getchar();
                if( c == '\n' )
                    return;
                if( isspace( c ) )
                    continue;
                ungetc( c, stdin );
                break;
            }

            scanf( "%s", word );
            map< string, int >::iterator word_id_it = WordId.find( word );
            if( word_id_it == WordId.end() )
                word_id_it = WordId.insert( make_pair( string( word ), ( int )WordId.size() ) ).first;
            int word_id = word_id_it->second;
            sentence.push_back( word_id );
        }
    }

	void Write( int t )
	{
        printf( "Case #%d: ", t );
        if( Result == -1 )
            puts( "IMPOSSIBLE" );
        else
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
