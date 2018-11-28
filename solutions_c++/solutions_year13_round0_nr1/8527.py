#include <iostream>

using namespace std;

#define NUM_COLUMNS  4
#define NUM_ROWS     4
#define NUM_DIAGNALS 4 

void updateResults( char* checklist,
					int   index,
					bool* oWon,
					bool* xWon,
					bool* emptySpots ){

	if( checklist[index] == 'X' ){
		*xWon = true;
	} else if( checklist[index] == 'O' ){
		*oWon = true;
	} else if( checklist[index] == '.' ){
		*emptySpots = true;
	}

}
void processResult( char* columnCheck,
					char* rowCheck,
					char* diagCheck){
	bool emptySpots = false;
	bool oWon = false;
	bool xWon = false;

	for( int column = 0; column < NUM_COLUMNS; column++ ){
		updateResults( columnCheck,
			           column,
					   &oWon,
					   &xWon,
					   &emptySpots );
	}

	for( int row = 0; row < NUM_COLUMNS; row++ ){
		updateResults( rowCheck,
					   row,
					   &oWon,
					   &xWon,
					   &emptySpots );
	}

	for( int diag = 0; diag < NUM_DIAGNALS; diag++ ){
		updateResults( diagCheck,
					   diag,
					   &oWon,
					   &xWon,
					   &emptySpots );
	}

	//TODO: xWon and yWon? 
	if( xWon ){
		cout << "X won";
	} else if( oWon ){
		cout << "O won";
	} else if( emptySpots ){
		cout << "Game has not completed";
	} else {
		cout << "Draw";
	}
}

void updateChecks( char* checklist,
				   int   index,
				   char  currentChar ){

	if( index == 0 && currentChar == 'T' )
		return; // we leave it as 'n' to process for next time

	if( checklist[index] == 'n' ||
		currentChar == checklist[index] ){
					
		checklist[index] = currentChar;

	} else if( currentChar == '.' ){

		checklist[index] = 'e';

	} else if( currentChar != 'T' && checklist[index] != '.' ){ 
		//current Char == 'T', rowCheck[i] stays the same
		//if rowCheck[row] == '.', then rowCheck[i] stays the same
		checklist[index] = 'f';

	}

}
void processInput( char* inputBoard ){
	
	//n = not inputed yet, f = already invalid, e = empty '.'
	//TODO: turn these into enums instead
	char columnCheck[NUM_COLUMNS] = {'n', 'n', 'n', 'n'};
	char diagnalCheck[NUM_DIAGNALS] = {'n', 'n'};
	char rowCheck[NUM_ROWS] = {'n', 'n', 'n', 'n'};
	bool empty = false;
	char currentChar;
	int  diagColumnIndex = 0;

	for( int row = 0; row < NUM_ROWS; row++ ){
		
		for( int column = 0; column < NUM_COLUMNS; column++ ){
			//current Char = X, O, T or .
			currentChar = inputBoard[row*NUM_COLUMNS+column];

			//checking row: if current char = X, O, or T, we place it in, 
			//else we mark as invalid
			if( rowCheck[row] != 'f' &&
			  ( row != 0 || currentChar != 'T' ) ){
				 updateChecks( rowCheck, row, currentChar );
			}

			//checking column
			if( columnCheck[column] != 'f' && 
			  ( column != 0 || currentChar != 'T' ) ){
				updateChecks( columnCheck, column, currentChar );
			}

			//checking first diagnals
			if( diagnalCheck[0] != 'f' && diagColumnIndex == column &&
			   ( diagColumnIndex != 0 || currentChar != 'T' ) ){
				updateChecks( diagnalCheck, 0, currentChar );
			}

			//checking second diagnal
			if( diagnalCheck[1] != 'f' && 3-diagColumnIndex == column &&
			   ( diagColumnIndex != 0 || currentChar != 'T' ) ){
				updateChecks( diagnalCheck, 1, currentChar );
			}
		}
		diagColumnIndex++;
	}
	processResult(rowCheck, columnCheck, diagnalCheck);
}

int main( int argc, char** argv ){	
	
	int numCases = 0;
	char inputBoard[16];

	cin >> numCases;

	for( int input = 0; input < numCases; input++ ){

		for( int character = 0; character < 16; character++ ){
			cin >> inputBoard[character];
		}
		
		//cin >> tmpEmpty;
		cout << "Case #" << input+1 <<": ";
		processInput( inputBoard );

		if( input != numCases-1 )
			cout << endl; 
	}

	return 0;
}