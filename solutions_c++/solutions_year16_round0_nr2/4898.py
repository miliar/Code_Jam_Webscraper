#include <iostream>
#include <string>
#include <vector>

using namespace std;

unsigned int do_case() {
	string input;
	cin >> input;

	vector<bool> pancakes( input.size() );
	for( size_t i=0; i<input.size(); ++i )
		pancakes[i] = (input[i]=='+');

	unsigned int wrong_blocks = 0;
	for( size_t i=0; i<pancakes.size(); ++i ) {
		if( !pancakes[i] ) {
			++wrong_blocks;
			for( ; i<pancakes.size() && !pancakes[i]; ++i ) ;
		}
	}

	unsigned int flips = 0;
	if( !pancakes[0] ) {
		--wrong_blocks;
		++flips;
	}
	flips += wrong_blocks*2;

	return flips;
}

int main() {
	int T;
	cin >> T;

	for( int i=0; i<T; ++i ) {
		cout << "Case #" << (i+1) << ": " << do_case() << endl;
	}
}
