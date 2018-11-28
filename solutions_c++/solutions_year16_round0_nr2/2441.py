#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int getFlipsCount( const string& s ) {
	int state = 0;
	int count = 0;
	for ( char c : s ) {
		switch ( state ) {
			case 0:
				if ( c == '-' ) {
					count++;
					state = 1;
				}
				break;
			case 1:
				if ( c == '+' )
					state = 0;
				break;
		}
	}
	count *= 2;
	if ( s[0] == '-' )
		count--;
	return count;
}

int main() {
	int t = 0;
	string s;

	ifstream in( "D:\\Sources\\C++\\CodeJam\\2016\\stage_1\\in.txt" );
	ofstream out( "D:\\Sources\\C++\\CodeJam\\2016\\stage_1\\out.txt" );
	in >> t;
	getline( in, s );
	for ( int i = 1; i <= t; i++ ) {
		getline( in, s );

		out << "Case #" << i << ": " << getFlipsCount( s ) << endl;
	}
	return 0;
}

