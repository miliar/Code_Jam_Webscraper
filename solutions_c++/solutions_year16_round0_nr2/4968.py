#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <map>

using namespace std;

unsigned int FindFirstBoxed( string const& InputStack );
void FlipToHere( unsigned int const FirstBoxed, string & InputStack );

//Example of loading info from a root file
int main( int argc, char * argv[] )
{
	//Find out how many iterations there are
	unsigned int nInputs = 0;
	cin >> nInputs;
	//cout << nInputs << " tests" << endl;

	//Loop over all inputs
	for ( unsigned int inputIndex = 0; inputIndex < nInputs; ++inputIndex )
	{
		//Read input
		string inputStack = "";
		cin >> inputStack;
		//cout << "input: " << inputStack << endl;

		unsigned int flips = 0;
		while ( true )
		{
			//Find the first boxed pancake
			unsigned int firstBoxed = FindFirstBoxed( inputStack );

			if ( firstBoxed == inputStack.size() )
			{
				//All the same - check they are happy side up
				if ( inputStack[ 0 ] != '+' ) ++flips;

				//Output
				cout << "Case #" << inputIndex + 1 << ": " << flips << endl;
				break;
			}
			else
			{
				//Flip everything up to first boxed
				FlipToHere( firstBoxed, inputStack );
				++flips;
			}
		}

		//For the sake of completeness, I'm guessing that the general solution is just 2x(number minority)+(1 if '-' is majority)
	}

	return 0;
}

unsigned int FindFirstBoxed( string const& InputStack )
{
	char const firstPancake = InputStack[ 0 ];

	//Look for first pancake that isn't like the top
	for ( unsigned int pancakeIndex = 1; pancakeIndex < InputStack.size(); ++pancakeIndex )
	{
		if ( firstPancake != InputStack[ pancakeIndex ] )
		{
			return pancakeIndex;
		}
	}

	//If you got this far then the stack was fine 
	return InputStack.size();
}

void FlipToHere( unsigned int const FirstBoxed, string & InputStack )
{
	for ( unsigned int pancakeIndex = 0; pancakeIndex < FirstBoxed; ++pancakeIndex )
	{
		if ( InputStack[ pancakeIndex ] == '+' )
		{
			InputStack[ pancakeIndex ] = '-';
		}
		else
		{
			InputStack[ pancakeIndex ] = '+';
		}
	}
	//cout << "flipped to: " << InputStack << endl;
}
