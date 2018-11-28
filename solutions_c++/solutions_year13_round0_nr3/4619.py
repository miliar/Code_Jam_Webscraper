#include <iostream>
#include <string>
#include <fstream>
#include <math.h>

using namespace std;

typedef unsigned long long ull;

bool isPalindrome( int val );

int main( int argc, char* argv[] )
{
	ifstream inputFile( "input.txt" );
	ofstream outputFile( "output.txt" );

	int numTest;
	inputFile >> numTest;

	ull left, right;

	for ( int k = 1; k <= numTest; k++ )
	{
		int num = 0;

		inputFile >> left >> right;

		double rootLeft = sqrt( left );
		double rootRight = sqrt( right );

		int first, last;

		if ( floor( rootLeft ) == rootLeft )
			first = (int) rootLeft;
		else
			first = (int) ceil( rootLeft );

		if ( floor( rootRight ) == rootRight )
			last = (int) rootRight;
		else
			last = (int) floor( rootRight );

		for ( int i = first; i <= last; i++ )
		{
			if ( isPalindrome( i ) )
				if ( isPalindrome( i*i ) )
				{
					cout << "number is: " << i << endl;
					cout << "square is: " << i*i << endl;
					num++;
				}
		}

		outputFile << "Case #" << k << ": " << num << endl;
		cout << "Case #" << k << ": " << num << endl << endl;
	}

	inputFile.close();
	outputFile.close();

	system( "PAUSE" );
	return 0;
}

bool isPalindrome( int val )
{
	char* buf = (char* ) malloc( sizeof(char) * 110 );

	if ( !buf )
	{
		cout << "malloc failed" << endl;
		return false;
	}

	sprintf( buf, "%d", val );

	int start = 0, end = 0;

	while ( buf[end] != '\0' )
		end++;

	end--;

	while ( start <= end )
	{
		if ( buf[start++] != buf[end--] )
			return false;
	}

	return true;
}

