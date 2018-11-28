#include <fstream>
#include <ostream>
#include <string>
#include <vector>
using namespace std;

bool checkIfAsleep( int[] );
void increaseDigitCount( int[], int );
void setDigitArrayToZero( int[] );
void printResults( bool, int, int );

int main()
{
	
	int T = 0;
	int N = 0;

	ifstream inFile( "A-large.in", ios::in );

	if ( !inFile )
	{
		exit( 1 );
	}

	vector<int> testCases;

	// run through test cases
	for ( int i = 0; inFile >> N; i++ )
	{
		if ( i == 0 )
		{
			T = N;
		}
		else
		{
			testCases.push_back( N );
		}
		
	}

	int digits[ 10 ] = { 0 };

	// check testcases
	for ( int i = 0; i < T; i++ )
	{
		string number = to_string(testCases[ i ]);
		int finalNumber = testCases[ i ];
		bool isAsleep = false;
		int multiplier = 2;

		// run through count game
		while ( isAsleep == false && multiplier <= 100 )
		{
			// increase digits
			for ( int j = 0; j < number.size(); j++ )
			{
				const int temp = static_cast< int >( number[ j ] ) - 48;

				increaseDigitCount( digits, temp );

				isAsleep = checkIfAsleep( digits );

				if ( isAsleep == true )
					break;		
			}

			if ( isAsleep == false )
			{
				finalNumber = testCases[ i ] * multiplier;
				number = to_string( finalNumber );
				multiplier++; // increment multiplier
			}
			
		}

		
		printResults( isAsleep, i + 1, finalNumber );



		setDigitArrayToZero( digits ); // reset digits

	}
	
	return 0;
}
bool checkIfAsleep( int a[] )
{
	for ( int i = 0; i < 10; i++ )
	{
		if ( a[ i ] == 0 )
			return false;
	}

	return true;
}
void increaseDigitCount( int a[], int x)
{	
	if ( x >= 0 && x <= 9 )
	{
		a[ x ]++;
	}

	
}
void setDigitArrayToZero( int a[] )
{
	for ( int i = 0; i < 10; i++ )
	{
		a[ i ] = 0;
	}
}
void printResults( bool test, int count, int n )
{
	ofstream outFile( "answers.txt", ios::app );

	if ( !outFile )
	{
		exit( 1 );
	}

	if ( test == true )
	{
		outFile << "Case #" << count << ": " << n << endl;
	}
	else
		outFile << "Case #" << count << ": " << "INSOMNIA" << endl;
}