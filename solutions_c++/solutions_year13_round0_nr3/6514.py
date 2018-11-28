#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>

using namespace std;

//const char *NAME_OF_INPUT = "input.txt";
const char *NAME_OF_INPUT = "C-small-attempt0.in";
//const char *NAME_OF_INPUT = "A-large.in";
ifstream fileStream;
int numberOfTestCases;
int A, B;
enum { RESULT_O, RESULT_X, RESULT_DRAW, RESULT_NOT };

int process( void );
bool isFair( double value );

int main ( void ){
	fileStream.open( NAME_OF_INPUT );
	
	fileStream >> numberOfTestCases;

	for( int i = 0; i < numberOfTestCases; i++ ){
		fileStream >> A >> B;

		int result = process();

		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	return 0;
}

int process( void ){
	double i, j;
	int count = 0;

	for( i = A; i <= B; i++ ){
		double rest = sqrt( i );
		rest = rest - ( int )rest;
		if( rest == 0 )
			if( isFair( i ) )
				if( isFair( sqrt( i ) ) ){
					count++;
					//cout << i << ' ' << sqrt(i) << endl;
				}
	}

	return count;
}

bool isFair( double value ){
	char stringValue[17];
	sprintf( stringValue, "%.0lf", value );
	int length = strlen( stringValue );
	int i;
	int a;

	for( i = 0; i < length; i++ ){
		a = length - i - 1;
		if( stringValue[i] != stringValue[a] ) return false;
		if( i >= a ) return true;
	} 
}
