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
    static const int MAX = 102;
    int Result;
    int R, C;
    char Grid[ MAX ][ MAX + 1 ];
public:
	void Work()
	{
        int i, j;

        Result = 0;

        for( i = 0; i < R; ++i )
        {
            for( j = 0; j < C; ++j )
            {
                if( Grid[i][j] == '.' )
                    continue;
                bool safe = false;
                bool stable = false;
                if( Check( i, j, 0, 1 ) ) 
                {
                    safe = true;
                    if( Grid[i][j] == '>' )
                        stable = true;
                }
                if( Check( i, j, 0, -1 ) ) 
                {
                    safe = true;
                    if( Grid[i][j] == '<' )
                        stable = true;
                }
                if( Check( i, j, 1, 0 ) ) 
                {
                    safe = true;
                    if( Grid[i][j] == 'v' )
                        stable = true;
                }
                if( Check( i, j, -1, 0 ) ) 
                {
                    safe = true;
                    if( Grid[i][j] == '^' )
                        stable = true;
                }
                if( !safe ) 
                {
                    Result = -1;
                    return;
                }
                if( !stable )
                    ++Result;
            }
        }
	}

    bool Check( int i, int j, int di, int dj )
    {
        while( true )
        {
            i += di;
            j += dj;
            if( !( 0 <= i && i < R && 0 <= j && j < C ) )
                break;
            if( Grid[i][j] != '.' )
                return true;
        }
        return false;
    }
	
	void Read()
	{
        int i;
		scanf( "%d%d", &R, &C );
        for( i = 0; i < R; ++i )
        {
            scanf( "%s", &Grid[i] );
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
