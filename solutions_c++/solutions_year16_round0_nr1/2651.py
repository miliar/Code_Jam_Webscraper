#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <bitset>
#include <assert.h>

using namespace std;

const int NotFound = -1;

void processNum( int num, bitset<10>& result )
{
	while( num != 0 ) {
		int digit = num % 10;
		result.set( digit );
		num /= 10;
	}
}

int main()
{
	ifstream input("f:\\Input.txt", std::ifstream::in);
	//istream& input = cin;
	ofstream output("f:\\Output.txt", std::ofstream::out);

	int count;
	input >> count;

	for( int i = 0; i < count; i++ ) {
		int num;
		input >> num;

		if( num == 0 ) {
			output << "Case #" << ( i + 1 ) << ": INSOMNIA" << endl;
			continue;
		}

		int answer = num;
		bitset<10> result;
		while( true ) {
			processNum( answer, result );
			if( result.count() == 10 ) {
				break;
			}
			answer += num;
		}

		output << "Case #" << ( i + 1 ) << ": " << answer << endl;
	}
	
	return 0;
}