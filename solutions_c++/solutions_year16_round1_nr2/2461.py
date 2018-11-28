#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <vector>
#include <stack>
#include <set>
#include <algorithm>


std::vector< int > solve( int n, std::vector< std::vector< int > > vReport )
{
	std::vector< int > rows;
	rows.resize( n );
	std::fill( rows.begin(), rows.end(), -1 );

	std::vector< std::vector< int > > testCase;
	testCase.resize( n );
	for ( int i = 0; i < n; i++ )
		testCase[ i ].resize( n );

	struct Level_t
	{
		std::vector< int > usedRows;
		std::set< int > leftRows;
	};

	for ( int start = 0; start < (int)vReport.size(); start++ )
	{
		Level_t level;
		level.usedRows.push_back( start );
		for ( int ir = 0; ir < (int)vReport.size(); ir++ )
			if ( ir != start )
				level.leftRows.insert( ir );

		std::stack< Level_t > stack;
		stack.push( level );

		while ( !stack.empty() )
		{
			Level_t tl = stack.top();
			stack.pop();
			for ( int row = 0; row < n; row++ )
				std::fill( testCase[ row ].begin(), testCase[ row ].end(), -1 );
			bool ok = true;
			for ( int row = 0; row < (int)tl.usedRows.size(); row++ )
			{
				for ( int i = 0; i < n; i++ )
					testCase[ row ][ i ] = vReport[ tl.usedRows[ row ] ][ i ];

				if ( row > 0 )
					for ( int i = 0; i < n; i++ )
						if ( testCase[ row ][ i ] <= testCase[ row - 1 ][ i ] )
						{
							ok = false;
							break;
						}
			}
			if ( !ok ) continue;

			if ( (int)tl.usedRows.size() == n )
			{
				std::set< int > leftColumns;
				for ( int i = 0; i < n; i++ )
					leftColumns.insert( i );

				bool bFoundSolution = true;
				for ( auto it = tl.leftRows.begin(); it != tl.leftRows.end(); it++ )
				{
					auto itlc = leftColumns.begin();
					while ( true )
					{
						if ( itlc == leftColumns.end() )
						{
							bFoundSolution = false;
							break;
						}
//						assert( itlc != leftColumns.end() );
						bool found = true;
						int col = *itlc;
						for ( int row = 0; row < n; row++ )
						{
							if ( testCase[ row ][ col ] != vReport[ *it ][ row ] )
							{
								found = false;
								break;
							}
						}
						if ( found ) break;

						itlc++;
					}
					if ( !bFoundSolution ) break;

					leftColumns.erase( itlc );
				}

				if ( bFoundSolution )
				{
					assert( leftColumns.size() == 1 );

					std::vector< int > result;
					result.resize( n );
					for ( int i = 0; i < n; i++ )
						result[ i ] = testCase[ i ][ *leftColumns.begin() ];
					return result;
				}
			}
			else if ( (int)tl.usedRows.size() < n )
			{
				for ( auto it = tl.leftRows.begin(); it != tl.leftRows.end(); it++ )
				{
					Level_t nl = tl;
					nl.leftRows.erase( *it );
					nl.usedRows.push_back( *it );
					stack.push( nl );
				}
			}
		}
	}

	assert( false && "no solution :(" );

	return std::vector< int >();
}

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "B-small-attempt1.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		int n;
		fscanf( fin, "%d\n", &n );

		std::vector< std::vector< int > > vReport;
		vReport.resize( n * 2 - 1 );
		for ( int i = 0; i < n * 2 - 1; i++ )
		{
			vReport[ i ].resize( n );
			for ( int j = 0; j < n; j++ )
				fscanf( fin, "%d", &vReport[ i ][ j ] );
		}

		fprintf( fout, "Case #%d:", iCase );
		std::vector< int > result = solve( n, vReport );
		for ( int i = 0; i < n; i++ )
			fprintf( fout, " %d", result[ i ] );
		fprintf( fout, "\n" );
	}

	fclose( fin );
	fclose( fout );
/*
	for ( int test = 0; test < 50; test++ )
	{
		int n = rand() * 8 / RAND_MAX + 2;

		std::vector< std::vector< int > > testCase( n );
		for ( int i = 0; i < n; i++ )
			testCase[ i ].resize( n );

		for ( int row = 0; row < n; row++ )
			for ( int col = 0; col < n; col++ )
			{
				int base = 1;
				if ( row > 0 ) base = std::max< int >( base, testCase[ row - 1 ][ col ] );
				if ( col > 0 ) base = std::max< int >( base, testCase[ row ][ col - 1 ] );
				int r = rand() * 10 / RAND_MAX + 1;
				testCase[ row ][ col ] = base + r;
			}

		std::vector< std::vector< int > > vReport;
		vReport.resize( 2 * n );
		for ( int r = 0; r < n; r++ )
		{
			vReport[ r ].resize( n );
			for ( int i = 0; i < n; i++ )
				vReport[ r ][ i ] = testCase[ r ][ i ];
		}
		for ( int c = 0; c < n; c++ )
		{
			vReport[ c + n ].resize( n );
			for ( int i = 0; i < n; i++ )
				vReport[ c + n ][ i ] = testCase[ i ][ c ];
		}

		int skip = rand() * ( 2 * n ) / RAND_MAX;
		std::vector< int > tr = vReport[ skip ];
		vReport.erase( vReport.begin() + skip );

		std::vector< int > result = solve( n, vReport );
		assert( result == tr );
	}*/
}
