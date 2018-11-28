#include <iostream>
#include <algorithm>
#include <array>

using namespace std;

void do_case() {
	string s;
	cin >> s;

	string s2;
	for( char c : s ) {
		if( c < s2[0] ) {
			s2 += c;
		}
		else {
			s2 = c + s2;
		}
	}

	cout << s2;
}

int main() {
	unsigned int T;
	cin >> T;

	for( unsigned int i=0; i<T; ++i ) {
		cout << "Case #" << (i+1) << ": ";
		do_case();
		cout << endl;
	}
}
