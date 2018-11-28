#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>

using namespace std;

ifstream inFile;
ofstream outFile;

typedef struct
{
	char ch;
	int n;
} RLChar;

vector< RLChar > toRLStr( string s )
{
	int index = 0;
	vector< RLChar > rlstr;
	while ( index < s.size() )
	{
		char baseChar = s[ index ];
		int baseIndex = index;
		
		while ( index < s.size() && s[ index ] == baseChar ) ++index;
		
		RLChar rlc;
		rlc.ch = baseChar;
		rlc.n = index - baseIndex + 1;
		rlstr.push_back( rlc );
	}
	
	return rlstr;
};

// Tests to see if the two RLStrings are similar by the rules of the game
bool gameCompare( vector< RLChar > a, vector< RLChar > b )
{
	if ( a.size() != b.size() ) return false;

	for ( int i = 0; i < a.size(); ++i )
	{
		if ( a[ i ].ch != b[ i ].ch ) return false;
	}
	
	return true;
};

int round( double x )
{
	int y = ( int ) x;
	x = x - y;
	if ( x >= 0.5 )
	{
		return y+1;
	}
	else
	{
		return y;
	}
};

// if the fully-reduced strings are not equivalent, Fegla wins
int main( int argc, char **argv )
{
	inFile.open( "gcj_a.in" );
	outFile.open( "gcj_a.out" );
	
	int T;
	inFile >> T;
	
	for ( int t = 0; t < T; ++t )
	{
		int N;
		bool feglaWon = false;
		
		inFile >> N;
		vector< vector< RLChar > > strs;
		
		for ( int i = 0; i < N; ++i )
		{
			string s;
			inFile >> s;
			strs.push_back( toRLStr( s ) ); 
		}
		
		for ( int i = 1; i < N; ++i )
		{
			if ( !gameCompare( strs[ i-1 ], strs[ i ] ) )
			{
				// fegla wins
				feglaWon = true;
				break;
			}
		}
		
		if ( feglaWon )
		{
			outFile << "Case #" << t+1 << ": Fegla Won" << endl;
		}
		else
		{
			int totalMoves = 0;
			
			for ( int e = 0; e < strs[ 0 ].size(); ++e )
			{
				int x = 0;
				for ( int i = 0; i < strs.size(); ++i )
				{
					x += strs[ i ][ e ].n;
				}
				
				x = round( ((double)x) / ((double)strs.size()));
				
				for ( int i = 0; i < strs.size(); ++i )
				{
					totalMoves += abs( x - strs[ i ][ e ].n );
				}
			}
			outFile << "Case #" << t+1 << ": " << totalMoves << endl;
		}
	}
	
	inFile.close();
	outFile.close();
	
	return 0;
};