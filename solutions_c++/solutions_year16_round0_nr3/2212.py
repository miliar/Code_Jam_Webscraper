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

	int t;
	input >> t;

	int base;
	input >> base;

	int count;
	input >> count;

	output << "Case #1:\r\n";
	for( int i = 0; i < count; i++ ) {
		string s = "1";
		for( int j = 0; j < ( base - 2 ) / 2; j++ ) {
			bool digit = (((i >> j) & 1) != 0);
			s += ( digit ? "11" : "00" );
		}
		s += "1";

		output << s;
		for( int j = 2; j <= 10; j++ ) {
			output << " " << ( j + 1 );
		}
		output << endl;
	}
	
	return 0;
}