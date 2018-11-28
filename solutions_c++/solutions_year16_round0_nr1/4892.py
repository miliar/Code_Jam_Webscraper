#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <map>

using namespace std;

void CheckDigits( vector< bool > & SeenDigits, unsigned int );
bool CheckDone( vector< bool > & SeenDigits );

//Example of loading info from a root file
int main( int argc, char * argv[] )
{
	//Find out how many iterations there are
	unsigned int nInputs = 0;
	cin >> nInputs;
	//nInputs = 10000000; //TEST
	//cout << nInputs << " tests" << endl;

	unsigned int maxMultiplier = 10000000;
	unsigned int maxMultiplyUsed = 0;
	unsigned int maxMultForInput = 0;

	//Loop over all inputs
	for ( unsigned int inputIndex = 0; inputIndex < nInputs; ++inputIndex )
	{
		//Read the input
		unsigned int inputNumber = 0;
		unsigned int outputNumber = 0;
		vector< bool > seenDigits( 10, false );
		cin >> inputNumber;
		//inputNumber = inputIndex; //TEST
		//cout << "input: " << inputNumber << endl;
		outputNumber = inputNumber;
		bool success = false;

		//Test multipliers
		for ( unsigned int multiplyBy = 1; multiplyBy <= maxMultiplier; ++multiplyBy )
		{
			outputNumber = inputNumber * multiplyBy;
			CheckDigits( seenDigits, outputNumber );

			if ( CheckDone( seenDigits ) )
			{
				//Make the "success" output
				//cout << "Case #" << inputIndex + 1 << ": " << outputNumber << " (multiply by = " << multiplyBy << ")" << endl;
				cout << "Case #" << inputIndex + 1 << ": " << outputNumber << endl;
				success = true;
				if ( multiplyBy > maxMultiplyUsed )
				{
					maxMultForInput = inputNumber;
					maxMultiplyUsed = multiplyBy;
				}
				break;
			}
		}

		//Failed
		if ( !success )
		{
			cout << "Case #" << inputIndex + 1 << ": INSOMNIA" << endl;
		}
	}

	//cout << "Max mult: " <<  maxMultiplyUsed << " for input " << maxMultForInput << endl;
	return 0;
}

void CheckDigits( vector< bool > & SeenDigits, unsigned int InputNumber )
{
	stringstream digitStream;
	digitStream << InputNumber;
	string digitString = digitStream.str();

	for ( char thisChar : digitString )
	{
		int thisDigit = thisChar - '0';//atoi( thisChar );
		SeenDigits[ thisDigit ] = true;
	}
}

bool CheckDone( vector< bool > & SeenDigits )
{
	bool done = true;
	for ( bool thisDigit : SeenDigits )
	{
		//cout << thisDigit << ", ";
		done &= thisDigit;
	}
	//cout << endl;
	return done;
}
