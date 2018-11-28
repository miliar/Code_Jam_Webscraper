#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Game states
static const enum GameStates 
	{
		Xwon,
		Owon,
		Draw,
		NotComplete
	};

GameStates CheckGameState( vector<char> board);

void main() 
{
	// Opening input file
	string filename = "input.txt";
	string inputfile = "C:\\Users\\Lionel\\Documents\\Visual Studio 2012\\Projects\\CodeJam2013\\Debug\\input.txt";
	ifstream file( inputfile );

	string outputfile = "C:\\Users\\Lionel\\Documents\\Visual Studio 2012\\Projects\\CodeJam2013\\Debug\\output.txt";
	ofstream outfile( outputfile );

	// Checking if input file exists
	if( !file )
	{
		cerr << "can't open input file\"" << endl;
		exit( EXIT_FAILURE );
	}

	// Reading in file contents
	vector<char> board;
	vector< vector<char> > boards;
	char c = { NULL };
	char prev_c = { NULL };
	int totalCases = { 0 };
	file >> totalCases;

	// Get all the boards from the input file
		while ( file.get(c) )
		{
			if ( c != '\n' )
			{
				// put piece on board
				board.push_back(c);
			}
			else if ( c == prev_c )
			{
				// put complete board into collection and clear current board, getting ready for new board
				boards.push_back( board );
				board.clear();
			}
			
			prev_c = c;
		}

	for ( int i = 0; i < boards.size(); ++i)
	{
		switch ( CheckGameState( boards[i] ) )
		{
		case Xwon:
			outfile << "Case #" << i+1 << ": X won" << endl;
			break;

		case Owon:
			outfile << "Case #" << i+1 << ": O won" << endl;
			break;

		case Draw:
			outfile << "Case #" << i+1 << ": Draw" << endl;
			break;

		case NotComplete:
			outfile << "Case #" << i+1 << ": Game has not completed" << endl;
			break;
		}
	}
}

GameStates CheckGameState( vector<char> board )
{
	// Intial Game state
	GameStates gamestate = { Draw };
	const int ROWS = { 4 };
	const int COLS = { 4 };
	const char wildcard = 'T';
	const char emptyPos = '.';
	const char playerX = 'X';
	const char playerO = 'O';

	// Go through board
	vector<bool> colstate( ROWS, true );
	bool rowstate = { true };
	bool diag1state = { true };
	bool diag2state = { true };

	for ( int i = 0; i < ROWS; ++i)
	{
		for ( int j = 0; j < COLS; ++j)
		{
			char currentPos = board[j + i*ROWS];

			char nextPosRight = { currentPos };
			if ( j < COLS-1 ) 	{ nextPosRight = board[ (j+1) + i*ROWS ]; } 

			char nextPosDown = { currentPos };
			if ( i < ROWS-1 ) { nextPosDown = board[ j + (i+1)*ROWS ]; }

			char nextPosDownRight = { currentPos };
			if ( i < ROWS-1 && j < COLS-1 && i == j ) { nextPosDownRight = board[ (j+1) + (i+1)*ROWS ]; }

			char nextPosDownLeft = { currentPos };
			if ( i < ROWS-1 &&  (i+j) == ROWS-1 ) { nextPosDownLeft = board[ (j-1) + (i+1)*ROWS ]; }
			
			// check if empty position
			if ( currentPos == emptyPos )
			{
				// no-one wins the row or col
				gamestate = NotComplete;	// can not draw if there are still empty spaces
				rowstate = false;
				colstate[j] = false;
				//break;
			}

			// check col for winner
			if ( currentPos != nextPosDown  &&
				 nextPosDown != wildcard &&
				 currentPos != wildcard )
			{
				// no-one wins the col
				colstate[j] = false;
			}

			// check diagonal 1 for winner
			if ( currentPos != nextPosDownRight  &&
				 nextPosDownRight != wildcard &&
				 currentPos != wildcard )
			{
				// no-one wins diagonal 1
				diag1state = false;
			}

			// check diagonal 2 for winner
			if ( currentPos != nextPosDownLeft  &&
				 nextPosDownLeft != wildcard &&
				 currentPos != wildcard )
			{
				// no-one wins diagonal 2
				diag2state = false;
			}

			// check row for winner
			if ( currentPos != nextPosRight  &&
				 nextPosRight != wildcard &&
				 currentPos != wildcard )
			{
				// no-one wins the row
				rowstate = false;
				//break;
			}

		}

		// did someone win the row?
		if ( rowstate )
		{
			// we have a winner
			switch ( board[i*ROWS] )
			{
			case playerX :
				gamestate = Xwon;
				break;

			case playerO :
				gamestate = Owon;
				break;
			}

			return gamestate;
		}
	}

	// did someone win a column?
	for ( int i = 0; i < colstate.size(); ++i )
	{
		if ( colstate[i] )
		{
			// we have a winner
			switch ( board[i] )
			{
			case playerX :
				gamestate = Xwon;
				break;

			case playerO :
				gamestate = Owon;
				break;
			}

			return gamestate;
		}
	}

	// did someone win diagonal 1
	if ( diag1state )
	{
		// we have a winner
		switch ( board[0] )
		{
		case playerX :
			gamestate = Xwon;
			break;

		case playerO :
			gamestate = Owon;
			return gamestate;
		}
	}

	// did someone win diagonal 2
	if ( diag2state )
	{
		// we have a winner
		switch ( board[ROWS-1] )
		{
		case playerX :
			gamestate = Xwon;
			break;

		case playerO :
			gamestate = Owon;
			return gamestate;
		}
	}

	return gamestate;
}