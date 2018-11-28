#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main( int argc, char *argv[] ) {

	ifstream fileIn( argv[1] );

	int T;
	fileIn >> T;
	
	for( int i = 1; i <= T; i++ ) {

		cout << "Case #" << i << ": " << flush;

		string word;
		fileIn >> word;

		string answer = "";

		for( int j = 0; j < word.length(); j++ ) {
			char newLetter = word.at( j );

			if( answer.length() == 0 ) {
				answer = answer + newLetter;
			} else if( answer.at( 0 ) <= newLetter ) {
				answer = newLetter + answer;
			} else {
				answer = answer + newLetter;
			}
		}

		cout << answer << endl;
	}

	fileIn.close();
	return 0;

}
