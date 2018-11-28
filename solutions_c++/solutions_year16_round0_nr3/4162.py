#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

bool IsPrime ( unsigned long long value, unsigned long long &multiplier )
{
	if ( value == 0 || value == 1 )
		return true;

	for ( unsigned long long i = 2; i <= sqrt(value); i++ )
	{
		if ( value % i == 0 )
		{
			multiplier = i;
			return false;
		}
	}
	return true;
}

long double power ( long double value, long double power ) {
	long double result = 1;

	for ( long double i = 0; i < power; ++i ) {
		result *= value;
	}

	return ( result );
}

unsigned long long baseConvert ( string str, int base )
{
	unsigned long long value = 0;
	for ( int i = str.length () - 1, j = 0; i >= 0; i--, j++ )
	{
		if ( str[i] == '1' )
		{
			value += ( unsigned long long ) power ( base, j );
		}
	}
	return value;
}

bool isJam ( string str )
{
	if ( str[str.length () - 1] == '0' || str[0] == '0' )
		return false;

	bool isJam = true;
	unsigned long long multiplier[9] = { 0 };

	for ( int j = 2; j <= 10; j++ )
	{
		unsigned long long value = baseConvert ( str, j );
		if ( IsPrime ( value, multiplier[j - 2] ) )
		{
			isJam = false;
			break;
		}
	}

	if ( isJam )
	{
		//print
		cout << str;
		for ( int j = 2; j <= 10; j++ )
			cout << " " << multiplier[j - 2];
		cout << endl;
	}
	return isJam;
}

string convertIntToBinaryString ( unsigned long long intVal, int N )
{

	char *binaryChar = ( char * ) malloc ( sizeof ( char ) * ( N + 1 ) );
	memset ( binaryChar, '0', N + 1 );
	int i;
	for ( i = N - 1; intVal > 0; i-- )
	{
		if ( intVal % 2 == 0 )
			binaryChar[i] = '0';
		else
			binaryChar[i] = '1';
		intVal /= 2;
	}
	binaryChar[N] = '\0';
	string binaryString ( binaryChar );
	free ( binaryChar );
	return binaryString;
}

int main ()
{
	int T;
	cin >> T;
	unsigned long long arr[11] = { 0 };

	for ( int i = 1; i <= T; i++ )
	{
		int N, J;

		cin >> N >> J;

		cout << "Case #" << i << ":" << endl;

		int noOfJam = 0;

		char *str = new char[N + 1];
		memset ( str, '0', N + 1 );

		str[0] = '1';
		str[N - 1] = '1';
		str[N] = '\0';

		unsigned long long lowerLimit = baseConvert ( str, 2 );

		for ( int j = 1; j < N - 1; j++ )
			str[j] = '1';

		unsigned long long upperLimit = baseConvert ( str, 2 );

		for ( unsigned long long range = lowerLimit; range <= upperLimit && noOfJam < J; range++ )
		{
			string binaryStr = convertIntToBinaryString ( range, N );
			if ( isJam ( binaryStr ) )
				noOfJam++;
		}

		delete ( str );
	}
}