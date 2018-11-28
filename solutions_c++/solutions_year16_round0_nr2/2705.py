#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <bitset>
#include <assert.h>
#include <string>

using namespace std;

const int NotFound = -1;

int main()
{
	ifstream input("f:\\Input.txt", std::ifstream::in);
	//istream& input = cin;
	ofstream output("f:\\Output.txt", std::ofstream::out);

	int count;
	input >> count;

	for( int i = 0; i < count; i++ ) {
		string sequence;
		input >> sequence;

		int result = 0;
		int currentPos = 0;
		while( true ) {
			int minusBegin = sequence.find( '-', currentPos );
			if( minusBegin == NotFound ) {
				break;
			}
			int minusEnd = sequence.find( '+', minusBegin + 1 );
			result += ( minusBegin == 0 ? 1 : 2 );
			if( minusEnd == NotFound ) {
				break;
			}
			currentPos = minusEnd + 1;
		}

		output << "Case #" << ( i + 1 ) << ": " << result << endl;
	}
	
	return 0;
}