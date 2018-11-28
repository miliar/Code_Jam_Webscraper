/*
 * countingSheep.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: jpaone
 */

#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

short getLSD( long long int &N );
bool seenAll( map< short, int >* s );

int main( int argc, char *argv[] ) {

	if( argc != 2 ) {
		cerr << "Usage: ./countingSheep {file.in}" << endl;
		return -1;
	}

	ifstream fin( argv[1] );
	if( !fin ) {
		cerr << "Could not open " << argv[1] << endl;
		return -2;
	}

	int T;		// number of test cases
	fin >> T;

	for( int i = 0; i < T; ++i ) {
		long long int N;	// number to start from
		fin >> N;

		cout << "Case #" << i+1 << ": " << flush;

		if( N == 0 ) {
			cout << "INSOMNIA" << endl;
			continue;
		}

		map< short, int >* seenInts = new map<short, int>();

		long long int nextN = N;
		int counter = 1;
		do {
			nextN = N * counter++;

			while( nextN > 0 ) {
				short digit = getLSD( nextN );

				seenInts->insert( pair<short, int>( digit, 1 ) );
			}

		} while( !seenAll( seenInts ) );

		nextN = N * --counter;
		cout << nextN << endl;
	}

	fin.close();

	return 0;
}

short getLSD( long long int &N ) {
	if( N == 0 ) {
		return 0;
	} else {
		short res = N % 10;
		N /= 10;
		return res;
	}
}

bool seenAll( map< short, int >* s ) {
	return s->size() == 10;
}
