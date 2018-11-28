#include "stdafx.h"
#include <iostream>
#include <math.h>
#include <list>

using namespace std;

static double PalindromeLastFail = 0;
static list<double> Palindrome;
static list<double> SquareAndFair;

static bool IsPalindrome( double value )
{
	list<double>::iterator i;

	// See if we've already calculated it.
	for( i = Palindrome.begin(); i != Palindrome.end(); ++i )
	{
		if( value == *i )
		{
			return true;
		}
		else if( *i > value )
		{
			return false;
		}
	}

	// We went through the entire list but this value is less than our last fail so we know its no good.
	if( value < PalindromeLastFail )
	{
		return false;
	}

	double numberOfDigits = log10 (value) + 1;
	modf( numberOfDigits, &numberOfDigits );
	double numberOfComparisons = numberOfDigits / 2;
	modf( numberOfComparisons, &numberOfComparisons );

	for( double i = 0; i < numberOfComparisons; i++ )
	{
		// Compare the values starting at both end points.
		double digitAIndex = i;
		double digitBIndex = numberOfDigits - i - 1;

		double temp = value / pow( 10, digitAIndex + 1 );     // Get larger place value
		modf( temp, &temp );
		temp = value - ( temp * pow( 10, digitAIndex + 1 ) ); // Subtract it from the initial value to get the current place value.
		temp = temp / pow( 10, digitAIndex );                 // Divide it by that number place to get value
		modf( temp, &temp );                                  // Ignore fractional part.

		double digitAValue = temp;

		temp = value / pow( 10, digitBIndex + 1 );
		modf( temp, &temp );
		temp = value - ( temp * pow( 10, digitBIndex + 1 ) );
		temp = temp / pow( 10, digitBIndex );
		modf( temp, &temp );

		double digitBValue = temp;

		if( digitAValue != digitBValue )
		{
			PalindromeLastFail = value;
			return false;
		}
	}

	Palindrome.push_back( value );

	return true;
}

static bool IsSquareAndSquareValuePalindrome( double value )
{
	double sqrtOfValue = sqrt( value );
	double intpart;
	double fractpart = modf (sqrtOfValue , &intpart);

	return fractpart == 0 && IsPalindrome( intpart );
}

static void FairAndSquare_ReadInput()
{
	int  numTestCases;

	// read number of test cases
	scanf( "%d", &numTestCases );

	for( int i = 0; i < numTestCases; ++i )
	{
		double minRange = 0;
		double maxRange = 0;

		// read range values
		scanf( "%lg", &minRange );
		scanf( "%lg", &maxRange );

		if( maxRange < minRange ) break;

		double numberFairAndSquare = 0;
		for( double j = minRange; j <= maxRange; j++ )
		{
			// check each number in the range to see if they're fair and square
			list<double>::iterator iterator;

			// See if we've already calculated it.
			for( iterator = SquareAndFair.begin(); iterator != SquareAndFair.end(); ++iterator )
			{
				if( j == *iterator )
				{
					numberFairAndSquare++;
				}
				else if( *iterator > j )
				{
					break;
				}
			}
		}

		printf( "Case #%d: %.0lf\n", i + 1, numberFairAndSquare );
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	// build a list of possible square and fair
	Palindrome.clear();
	PalindromeLastFail = 0;
	SquareAndFair.clear();

	for( double i = 0; i <= pow( 10, 3 ); i++ )
	{
		// check each number in the range to see if they're fair and square
		if( IsPalindrome( i ) && IsSquareAndSquareValuePalindrome( i ) )
		{
			SquareAndFair.push_back( i );
		}
	}

	FairAndSquare_ReadInput();

	return( 0 );
}

