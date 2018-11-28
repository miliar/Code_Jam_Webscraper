#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

//const char *NAME_OF_INPUT = "input.txt";
const char *NAME_OF_INPUT = "A-small-attempt1.in";
ifstream fileStream;
int numberOfTestCases;
char board[4][5];
enum { RESULT_O, RESULT_X, RESULT_DRAW, RESULT_NOT };

int process( void );
bool isAvailable( int row, int column );

int main ( void ){
	fileStream.open( NAME_OF_INPUT );
	
	fileStream >> numberOfTestCases;

	for( int i = 0; i < numberOfTestCases; i++ ){
		for( int j = 0; j < 4; j++ ){
			fileStream >> board[j];
		}	

		int result = process();
		cout << "Case #" << i + 1 << ": ";
		if( result == RESULT_O ) cout << "O won";
		else if( result == RESULT_X ) cout << "X won";
		else if( result == RESULT_DRAW ) cout << "Draw";
		else if( result == RESULT_NOT ) cout << "Game has not completed";
		cout << endl;
	}

	return 0;
}

int process( void ){
	int o[4][4], x[4][4];
	int i, j;
	bool flag = false;
	int row, column;

	for( i = 0; i < 4; i++ )
		for( j = 0; j < 4; j++ ){
			if( board[i][j] == '.' ) flag = true;
			o[i][j] = 0;
			x[i][j] = 0;

			// from left
			row = i, column = j - 1;
			if( isAvailable( row, column ) ){
				if( board[row][column] == 'O' || board[row][column] == 'T' ) o[i][j] += o[row][column] + 1;
				if( board[row][column] == 'X' || board[row][column] == 'T' ) x[i][j] += x[row][column] + 1;
			}
			// from up
			row = i - 1, column = j;
			if( isAvailable( row, column ) ){
				if( board[row][column] == 'O' || board[row][column] == 'T' ) o[i][j] += ( o[row][column] / 10 + 1 ) * 10;
				if( board[row][column] == 'X' || board[row][column] == 'T' ) x[i][j] += ( x[row][column] / 10 + 1 ) * 10;
			}
			// from leftUp
			row = i - 1, column = j - 1;
			if( i == j )
				if( isAvailable( row, column ) ){
					if( board[row][column] == 'O' || board[row][column] == 'T' ) o[i][j] += ( o[row][column] / 100 + 1 ) * 100;
					if( board[row][column] == 'X' || board[row][column] == 'T' ) x[i][j] += ( x[row][column] / 100 + 1 ) * 100;
				}
			// from rightUp
			row = i - 1, column = j + 1;
			if( 3 - i == j )
				if( isAvailable( row, column ) ){
					if( board[row][column] == 'O' || board[row][column] == 'T' ) o[i][j] += ( o[row][column] / 1000 + 1 ) * 1000;
					if( board[row][column] == 'X' || board[row][column] == 'T' ) x[i][j] += ( x[row][column] / 1000 + 1 ) * 1000;
				}
		}

	/*
	cout << " -- O -- " << endl;
	for( i = 0; i < 4; i++ ){
		for( j = 0; j < 4; j++ ){
			cout << o[i][j] << ' ';
		}
		cout << endl;
	}

	cout << " -- X -- " << endl;
	for( i = 0; i < 4; i++ ){
		for( j = 0; j < 4; j++ ){
			cout << x[i][j] << ' ';
		}
		cout << endl;
	}
	*/

	if( o[0][3] % 10 == 3 && ( board[0][3] == 'O' || board[0][3] == 'T' ) ) return RESULT_O;
	if( o[1][3] % 10 == 3 && ( board[1][3] == 'O' || board[1][3] == 'T' ) ) return RESULT_O;
	if( o[2][3] % 10 == 3 && ( board[2][3] == 'O' || board[2][3] == 'T' ) ) return RESULT_O;
	if( o[3][3] % 10 == 3 && ( board[3][3] == 'O' || board[3][3] == 'T' ) ) return RESULT_O;
	if( ( o[3][0] / 10 ) % 10 == 3 && ( board[3][0] == 'O' || board[3][0] == 'T' ) ) return RESULT_O;
	if( ( o[3][1] / 10 ) % 10 == 3 && ( board[3][1] == 'O' || board[3][1] == 'T' ) ) return RESULT_O;
	if( ( o[3][2] / 10 ) % 10 == 3 && ( board[3][2] == 'O' || board[3][2] == 'T' ) ) return RESULT_O;
	if( ( o[3][3] / 10 ) % 10 == 3 && ( board[3][3] == 'O' || board[3][3] == 'T' ) ) return RESULT_O;
	if( ( o[3][3] / 100 ) % 10 == 3 && ( board[3][3] == 'O' || board[3][3] == 'T' ) ) return RESULT_O;
	if( ( o[3][0] / 1000 ) % 10 == 3 && ( board[3][0] == 'O' || board[3][0] == 'T' ) ) return RESULT_O;
	if( x[0][3] % 10 == 3 && ( board[0][3] == 'X' || board[0][3] == 'T' ) ) return RESULT_X;
	if( x[1][3] % 10 == 3 && ( board[1][3] == 'X' || board[1][3] == 'T' ) ) return RESULT_X;
	if( x[2][3] % 10 == 3 && ( board[2][3] == 'X' || board[2][3] == 'T' ) ) return RESULT_X;
	if( x[3][3] % 10 == 3 && ( board[3][3] == 'X' || board[3][3] == 'T' ) ) return RESULT_X;
	if( ( x[3][0] / 10 ) % 10 == 3 && ( board[3][0] == 'X' || board[3][0] == 'T' ) ) return RESULT_X;
	if( ( x[3][1] / 10 ) % 10 == 3 && ( board[3][1] == 'X' || board[3][1] == 'T' ) ) return RESULT_X;
	if( ( x[3][2] / 10 ) % 10 == 3 && ( board[3][2] == 'X' || board[3][2] == 'T' ) ) return RESULT_X;
	if( ( x[3][3] / 10 ) % 10 == 3 && ( board[3][3] == 'X' || board[3][3] == 'T' ) ) return RESULT_X;
	if( ( x[3][3] / 100 ) % 10 == 3 && ( board[3][3] == 'X' || board[3][3] == 'T' ) ) return RESULT_X;
	if( ( x[3][0] / 1000 ) % 10 == 3 && ( board[3][0] == 'X' || board[3][0] == 'T' ) ) return RESULT_X;

	if( flag == true ) return RESULT_NOT;
	else return RESULT_DRAW;
}

bool isAvailable( int row, int column ){
	if( row >= 0 && row < 4 && column >= 0 && column < 4 ) return true;
	else return false;
}
