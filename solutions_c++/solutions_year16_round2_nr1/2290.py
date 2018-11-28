#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;

string solve(std::string S)
{
	std::map<char, int> stringCounts;
	std::map<int, int> digitCounts;
	std::string ans;

	for( uint i = 0; i < S.size(); i++ ) {
		if( stringCounts.count(S[i]) == 0 ) {
			stringCounts.insert( std::map<char, int>::value_type( S[i], 1 ) );
		} else {
			stringCounts[S[i]]++;
		}
	}

	if( stringCounts.count('Z') > 0 ) {	// ZERO
		digitCounts.insert( std::map<int, int>::value_type( 0, stringCounts['Z'] ) );
		int minus = stringCounts['Z'];
		stringCounts['Z'] -= minus;
		stringCounts['E'] -= minus;
		stringCounts['R'] -= minus;
		stringCounts['O'] -= minus;
	}
	if( stringCounts.count('W') > 0 ) {	// TWO
		digitCounts.insert( std::map<int, int>::value_type( 2, stringCounts['W'] ) );
		int minus = stringCounts['W'];
		stringCounts['T'] -= minus;
		stringCounts['W'] -= minus;
		stringCounts['O'] -= minus;
	}
	if( stringCounts.count('U') > 0 ) {	// FOUR
		digitCounts.insert( std::map<int, int>::value_type( 4, stringCounts['U'] ) );
		int minus = stringCounts['U'];
		stringCounts['F'] -= minus;
		stringCounts['O'] -= minus;
		stringCounts['U'] -= minus;
		stringCounts['R'] -= minus;
	}
	if( stringCounts.count('X') > 0 ) {	// SIX
		digitCounts.insert( std::map<int, int>::value_type( 6, stringCounts['X'] ) );
		int minus = stringCounts['X'];
		stringCounts['S'] -= minus;
		stringCounts['I'] -= minus;
		stringCounts['X'] -= minus;
	}
	if( stringCounts.count('G') > 0 ) {	// EIGHT
		digitCounts.insert( std::map<int, int>::value_type( 8, stringCounts['G'] ) );
		int minus = stringCounts['G'];
		stringCounts['E'] -= minus;
		stringCounts['I'] -= minus;
		stringCounts['G'] -= minus;
		stringCounts['H'] -= minus;
		stringCounts['T'] -= minus;
	}
	if( stringCounts.count('O') > 0 ) {	// ONE
		digitCounts.insert( std::map<int, int>::value_type( 1, stringCounts['O'] ) );
		int minus = stringCounts['O'];
		stringCounts['O'] -= minus;
		stringCounts['N'] -= minus;
		stringCounts['E'] -= minus;
	}
	if( stringCounts.count('T') > 0 ) {	// THREE
		digitCounts.insert( std::map<int, int>::value_type( 3, stringCounts['T'] ) );
		int minus = stringCounts['T'];
		stringCounts['T'] -= minus;
		stringCounts['H'] -= minus;
		stringCounts['R'] -= minus;
		stringCounts['E'] -= minus * 2;
	}
	if( stringCounts.count('F') > 0 ) {	// FIVE
		digitCounts.insert( std::map<int, int>::value_type( 5, stringCounts['F'] ) );
		int minus = stringCounts['F'];
		stringCounts['F'] -= minus;
		stringCounts['I'] -= minus;
		stringCounts['V'] -= minus;
		stringCounts['E'] -= minus;
	}
	if( stringCounts.count('S') > 0 ) {	// SEVEN
		digitCounts.insert( std::map<int, int>::value_type( 7, stringCounts['S'] ) );
		int minus = stringCounts['S'];
		stringCounts['S'] -= minus;
		stringCounts['E'] -= minus * 2;
		stringCounts['V'] -= minus;
		stringCounts['N'] -= minus;
	}
	if( stringCounts.count('I') > 0 ) {	// NINE
		digitCounts.insert( std::map<int, int>::value_type( 9, stringCounts['I'] ) );
		int minus = stringCounts['I'];
		stringCounts['N'] -= minus * 2;
		stringCounts['I'] -= minus;
		stringCounts['E'] -= minus;
	}

	for( int i = 0; i <= 9; i++ ) {
		if( digitCounts.count(i) > 0) {
			for( int j = 0; j < digitCounts[i]; j++ ) {
				ans += i + '0';
			}
		}
	}
	return ans;
}

int main(int argc, char *argv[]) {

    int T;

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    string line;
    std::getline(ifs, line);
    T = stoi(line);

    for( int i = 1; i <= T; i++ ) {
    	std::getline(ifs, line);
    	ofs << "Case #" << i << ": " << solve(line) << endl;
    }

    ifs.close();
    ofs.close();

    return 0;
}







