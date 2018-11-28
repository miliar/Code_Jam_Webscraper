#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <map>
#include <cmath>
#include <bitset>

using namespace std;

void CandidateToBinary( unsigned long long CoinCandidate, vector< bool > & OutputBits );
unsigned long long BinaryToBase( vector< bool > const& Binary, unsigned int const Base );
unsigned long long LowestDivisor( unsigned long long InThisBase );

//Example of loading info from a root file
int main( int argc, char * argv[] )
{
	//Find out how many iterations there are
	unsigned int nInputs = 0;
	cin >> nInputs;

	//Loop over all inputs (whatever, why not?)
	for ( unsigned int inputIndex = 0; inputIndex < nInputs; ++inputIndex )
	{
		//Read input
		unsigned int stringLength = 0;
		unsigned int coinNumber = 0;
		cin >> stringLength >> coinNumber;
		//cout << "N: " << stringLength << " J: " << coinNumber << endl;
		unsigned int coinsMade = 0;
		unsigned long long const firstCoin = pow( 2, ( stringLength - 1 ) ) + 1;
		unsigned long long const lastCoin = pow( 2, stringLength );

		cout << "Case #" << inputIndex + 1 << ":" << endl;

		//Make some coins
		for ( unsigned long long coinCandidate = firstCoin; coinCandidate < lastCoin; coinCandidate += 2 )
		{
			if ( coinsMade == coinNumber ) break;

			vector< bool > outputBits( stringLength, false );
			vector< unsigned long long > divisors( 9, 0 );
			bool goodCoin = true;
			CandidateToBinary( coinCandidate, outputBits );

			//Test each base
			for ( unsigned int base = 2; base <= 10; ++base )
			{
				unsigned long long inThisBase = BinaryToBase( outputBits, base );
				unsigned long long divisor = LowestDivisor( inThisBase );

				//fail primes
				if ( divisor )
				{
					divisors[ base - 2 ] = divisor;
				}
				else
				{
					goodCoin = false;
					break;
				}
			}

			if ( goodCoin )
			{
				for ( bool bit : outputBits ) cout << bit;
				for ( unsigned long long divisor : divisors ) cout << " " << divisor;
				cout << endl;
				++coinsMade;
			}
		}
	}

	return 0;
}

//I'm sure there's a built-in method but whatever
void CandidateToBinary( unsigned long long CoinCandidate, vector< bool > & OutputBits )
{
	for ( unsigned int place = 0; place < OutputBits.size(); ++place )
	{
		unsigned long long twoPow = pow( 2, OutputBits.size() - 1 - place );
		OutputBits[ place ] = ( CoinCandidate >= twoPow );
		if ( OutputBits[ place ] ) CoinCandidate -= twoPow;
	}
}

unsigned long long BinaryToBase( vector< bool > const& Binary, unsigned int const Base )
{
	unsigned long long result = 0;

	for ( unsigned int place = 0; place < Binary.size(); ++place )
	{
		if ( Binary[ place ] )
		{
			result += pow( Base, Binary.size() - 1 - place );
		}
	}

	return result;
}

unsigned long long LowestDivisor( unsigned long long InThisBase )
{
	//Ignore 1 (trivial) and 2 (all binary ending in 1)
	unsigned long long maxDivisor = sqrt( InThisBase );
	for ( unsigned long long tryDivisor = 3; tryDivisor <= maxDivisor; ++tryDivisor )
	{
		if ( !( InThisBase % tryDivisor ) ) return tryDivisor;
	}

	//If you get this far, it's prime
	return 0;
}
