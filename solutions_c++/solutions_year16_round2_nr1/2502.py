#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <map>
#include <algorithm>

using namespace std;

int charToInt( char InputCharacter );

//Code jam 1B problem A
int main( int argc, char * argv[] )
{
	//Find out how many test cases there are
	unsigned int nInputs = 0;
	cin >> nInputs;
	//cout << nInputs << " tests" << endl;

	//Loop over all inputs
	for ( unsigned int inputIndex = 0; inputIndex < nInputs; ++inputIndex )
	{
		//Read input
		string inputLine = "";
		cin >> inputLine;
		//cout << "input: " << inputLine << endl;

		//Count characters
		vector< int > characterCounts( 26, 0 );
		for ( char inputCharacter : inputLine )
		{
			characterCounts[ charToInt( inputCharacter ) ]++;
		}

		//Look for unique characters
		vector< int > outputDigits;

		//ZERO
		unsigned int const zNumber = characterCounts[ charToInt( 'Z' ) ];
		for ( unsigned int zIndex = 0; zIndex < zNumber; ++zIndex )
		{
			characterCounts[ charToInt( 'Z' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			characterCounts[ charToInt( 'R' ) ]--;
			characterCounts[ charToInt( 'O' ) ]--;
			outputDigits.push_back( 0 );
		}

		//ONE - later

		//TWO
		unsigned int const wNumber = characterCounts[ charToInt( 'W' ) ];
		for ( unsigned int wIndex = 0; wIndex < wNumber; ++wIndex )
		{
			characterCounts[ charToInt( 'T' ) ]--;
			characterCounts[ charToInt( 'W' ) ]--;
			characterCounts[ charToInt( 'O' ) ]--;
			outputDigits.push_back( 2 );
		}

		//THREE - later

		//FOUR
		unsigned int const uNumber = characterCounts[ charToInt( 'U' ) ];
		for ( unsigned int uIndex = 0; uIndex < uNumber; ++uIndex )
		{
			characterCounts[ charToInt( 'F' ) ]--;
			characterCounts[ charToInt( 'O' ) ]--;
			characterCounts[ charToInt( 'U' ) ]--;
			characterCounts[ charToInt( 'R' ) ]--;
			outputDigits.push_back( 4 );
		}

		//FIVE (now that FOUR is gone)
		unsigned int const fNumber = characterCounts[ charToInt( 'F' ) ];
		for ( unsigned int fIndex = 0; fIndex < fNumber; ++fIndex )
		{
			characterCounts[ charToInt( 'F' ) ]--;
			characterCounts[ charToInt( 'I' ) ]--;
			characterCounts[ charToInt( 'V' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			outputDigits.push_back( 5 );
		}

		//SIX
		unsigned int const xNumber = characterCounts[ charToInt( 'X' ) ];
		for ( unsigned int xIndex = 0; xIndex < xNumber; ++xIndex )
		{
			characterCounts[ charToInt( 'S' ) ]--;
			characterCounts[ charToInt( 'I' ) ]--;
			characterCounts[ charToInt( 'X' ) ]--;
			outputDigits.push_back( 6 );
		}

		//SEVEN (now that SIX is gone)
		unsigned int const sNumber = characterCounts[ charToInt( 'S' ) ];
		for ( unsigned int sIndex = 0; sIndex < sNumber; ++sIndex )
		{
			characterCounts[ charToInt( 'S' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			characterCounts[ charToInt( 'V' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			characterCounts[ charToInt( 'N' ) ]--;
			outputDigits.push_back( 7 );
		}

		//EIGHT
		unsigned int const gNumber = characterCounts[ charToInt( 'G' ) ];
		for ( unsigned int gIndex = 0; gIndex < gNumber; ++gIndex )
		{
			characterCounts[ charToInt( 'E' ) ]--;
			characterCounts[ charToInt( 'I' ) ]--;
			characterCounts[ charToInt( 'G' ) ]--;
			characterCounts[ charToInt( 'H' ) ]--;
			characterCounts[ charToInt( 'T' ) ]--;
			outputDigits.push_back( 8 );
		}

		//THREE (now that EIGHT is gone)
		unsigned int const hNumber = characterCounts[ charToInt( 'H' ) ];
		for ( unsigned int hIndex = 0; hIndex < hNumber; ++hIndex )
		{
			characterCounts[ charToInt( 'T' ) ]--;
			characterCounts[ charToInt( 'H' ) ]--;
			characterCounts[ charToInt( 'R' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			outputDigits.push_back( 3 );
		}

		//ONE (now that ZERO, TWO and FOUR are gone)
		unsigned int const oNumber = characterCounts[ charToInt( 'O' ) ];
		for ( unsigned int oIndex = 0; oIndex < oNumber; ++oIndex )
		{
			characterCounts[ charToInt( 'O' ) ]--;
			characterCounts[ charToInt( 'N' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			outputDigits.push_back( 1 );
		}

		//NINE (should be only thing left)
		unsigned int const iNumber = characterCounts[ charToInt( 'I' ) ];
		for ( unsigned int iIndex = 0; iIndex < iNumber; ++iIndex )
		{
			characterCounts[ charToInt( 'N' ) ]--;
			characterCounts[ charToInt( 'I' ) ]--;
			characterCounts[ charToInt( 'N' ) ]--;
			characterCounts[ charToInt( 'E' ) ]--;
			outputDigits.push_back( 9 );
		}

		//Error check
		for ( unsigned int count : characterCounts )
		{
			if ( count != 0 )
			{
				cerr << "Mistake: " << endl;
				for ( unsigned int count : characterCounts )
				{
					cerr << count << endl;
				}
				return 1;
			}
		}

		sort( outputDigits.begin(), outputDigits.end() );

		//Make output
		cout << "Case #" << inputIndex + 1 << ": ";
		for ( unsigned int digit : outputDigits )
		{
			cout << digit;
		}
		cout << endl;
	}

	return 0;
}

int charToInt( char InputCharacter )
{
	return ( ( int )InputCharacter ) - 65;
}
