#include <array>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;


int solve ( std::vector<int>& s ) {
	int sofar = 0;   // people currently standing up
	int friends = 0; // friends invited
	for ( int i = 0; i < s.size(); ++i ) {
		if ( friends + sofar < i && s[i] ) { // if there is somebody with shyness i and there isn't enough people the make them stand up..
			int newfriends = i - sofar - friends;
			friends += newfriends; // ..invite some more friends
			s[i-1] += newfriends;
		}
		sofar += s[i]; // so they stand up
	}
	/*cout << friends << " ";
	for ( int i : s ) cout << i;
	cout << endl;*/

	return friends;
}


void readcase ( int n, ifstream& infile ) {
	int smax;
	string ss;

	infile >> smax >> ss; assert(smax >= 0);
	vector<int> s;

	for ( int i = 0; i < smax+1; ++i )
		s.push_back(ss[i] - '0');

	/*cout << smax << " ";
	for ( int i : s ) cout << i;
	cout << endl;*/

	cout << "Case #" << n+1 << ": " << solve(s) << endl;
}




int main ( int argc, char** argv ) {
	if ( argc < 2 ) {
		cout << "Give me one file as input." << endl;
		return 1;
	}

	ifstream infile(argv[1]);

	int t;
	infile >> t;
	for ( int i = 0; i < t; ++i ) {
		readcase(i, infile);
	}

	return 0;
}