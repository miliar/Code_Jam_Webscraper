#include <iostream>
#include <fstream>

using namespace std;

#define TESTIN		"C-small-attempt2.in"
#define TESTOUT		"C-small-attempt2.out"

bool isPalindrome( long long x )
{
	// Start typing your C/C++ solution below
	// DO NOT write int main() function
	if( x < 0 )
	{
		return false;
	}
	long long div = 1;
	while( x / div >= 10 )
	{
		div *= 10;
	}
	while( x != 0 )
	{
		int left = x / div;
		int right = x % 10 ;
		if( left != right )
		{
			return false;
		}
		x = ( x % div ) / 10;
		div /= 100;
	}
	return true;
}

long long mySqrt( long long x)
{
	// if not , return -1
	long long value = 1;
	while( value * value < x )
	{
		value ++ ;
	}
	if( value * value == x )
	{
		return value;
	}
	return -1;
}

bool isFair( long long x )
{
	long long sqrtValue = 1;
// 	if( x >= 10 )
// 	{
// 		if( ( x % 10 == 1 ) || ( x % 10 == 5 ) || ( x % 10 == 6 ) ) 
// 		{
// 			return false;
// 		}		
// 	}
	sqrtValue = mySqrt( x );
	//cout << x << '\t' << sqrtValue << endl;
	if ( sqrtValue == -1 )
	{
		return false;
	}
	if( isPalindrome( sqrtValue ) == false )
	{		
		return false;
	}
	else
	{
		return true;
	}	
}
int main()
{
	ifstream infile( TESTIN );
	ofstream outfile( TESTOUT );
	int totalRecords ;
	infile >> totalRecords;
	long long A;
	long long B;
	long long count = 0 ;
	for( int round = 0 ; round < totalRecords ; round ++ )
	{
		infile >> A >> B;
		//cout << A << '\t' << B << endl ;
		count = 0 ;
		for( long long index = A ; index <= B ; index ++ )
		{
			if( isPalindrome( index ) )
			{
				if( isFair( index ) )
				{
					//cout << index << '\t' << mySqrt( index ) << endl;
					count ++;
				}
			}
		}
		//cout << "Case #" << round + 1 << ": " << count << endl;
		outfile << "Case #" << round + 1 << ": " << count << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}