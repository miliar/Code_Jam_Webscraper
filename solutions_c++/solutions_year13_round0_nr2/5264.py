#include <iostream>
#include <string>
#include <fstream>

using namespace std;

typedef enum {
	up,
	down,
	right,
	left
} direction;

int board[120][120];

bool checkIfPossible( int i, int j, int n, int m, direction dir );
bool checkRight( int i, int j, int end );
bool checkLeft( int i, int j, int start );
bool checkUp( int i, int j, int start );
bool checkDown( int i, int j, int end );

void displayInput( int n, int m );

int main( int argc, char* argv[] )
{
	ifstream inputFile( "input.txt" );
	ofstream outputFile( "output.txt" );

	int numTest;
	inputFile >> numTest;

	int n, m;
	bool possible;

	for ( int k = 1; k <= numTest; k++ )
	{
		possible = true;
		inputFile >> n >> m;

		for ( int i = 0; i < n; i++ )
			for ( int j = 0; j < m; j++ )
				inputFile >> board[i][j];

		//displayInput( n, m );

		for ( int i = 0; i < n && possible; i++ )
		{
			for ( int j = 0; j < m && possible; j++ )
			{
				if ( !checkIfPossible( i, j, n, m, direction::right ) || !checkIfPossible( i, j, n, m, direction::left ) )
					if ( !checkIfPossible( i, j, n, m, direction::up ) || !checkIfPossible( i, j, n, m, direction::down ) )
						possible = false;
			}
		}

		if ( possible )
			outputFile << "Case #" << k << ": YES" << endl;
		else
			outputFile << "Case #" << k << ": NO" << endl;
	}

	inputFile.close();
	outputFile.close();

	system( "PAUSE" );
	return 0;
}

bool checkIfPossible( int i, int j, int n, int m, direction dir )
{
	bool temp;

	switch ( dir )
	{
	case direction::up:
		temp = checkUp( i, j, 0 );
		break;
	case direction::down:
		temp = checkDown( i, j, n-1 );
		break;
	case direction::right:
		temp = checkRight( i, j, m-1 );
		break;
	case direction::left:
		temp = checkLeft( i, j, 0 );
		break;
	default:
		break;
	}

	return temp;
}

bool checkUp( int i, int j, int start )
{
	int target = board[i][j];

	if ( i == start )
		return true;

	while ( --i >= start )
	{
		if ( target < board[i][j] )
			return false;
	}

	return true;
}

bool checkDown( int i, int j, int end )
{
	int target = board[i][j];

	if ( i == end )
		return true;

	while ( ++i <= end )
	{
		if ( target < board[i][j] )
			return false;
	}

	return true;
}

bool checkLeft( int i, int j, int start )
{
	int target = board[i][j];

	if ( j == start )
		return true;

	while ( --j >= start )
	{
		if ( target < board[i][j] )
			return false;
	}

	return true;
}

bool checkRight( int i, int j, int end )
{
	int target = board[i][j];

	if ( j == end )
		return true;

	while ( ++j <= end )
	{
		if ( target < board[i][j] )
			return false;
	}

	return true;
}

void displayInput( int n, int m )
{
	for ( int i = 0; i < n; i++ )
	{
		for ( int j = 0; j < m; j ++ )
			cout << board[i][j];
		cout << endl;
	}
	cout << endl;
}