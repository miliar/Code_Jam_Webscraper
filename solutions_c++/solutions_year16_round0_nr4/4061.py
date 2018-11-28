#include <iostream>
#include <fstream>
#include <string>
 
#include <algorithm>
#include <set>
#include <iterator>
#include "BigIntegerLibrary.hh"

using namespace std;

int k, c, s;

void solve(ofstream& out) {
	
	if (k == s) {
		for ( int i = 0; i < k; i++ ) {
			out << i + 1 << ' ';
		}
		out << endl;
		return;
	}
	if (s * c < k) {
		out << "IMPOSSIBLE" << endl;
	    return;	    	
	}
	int tile = 1;
	BigInteger* res = new BigInteger[s];
	BigInteger position;
	for ( int i = 0; i < s; i++ ) {
	    position = BigInteger(1);
	     
		for ( int j = 0; j < c; j++ ) {
		    position -= 1;
		    position *= k;
			position += tile;
	        tile += 1;
	        if (tile > k)
	            tile = 1;
	    }
	    res[i] = position;
	}
	for ( int i = 0; i < s; i++ ) {
		out << res[i] << ' ';
	}
	out << endl;
	return;
}

int main(int argc, char* argv[]) {	
	string inputFile = (argc > 1) ? argv[1] : "input.txt";
	string outputFile = (argc > 2) ? argv[2] : (argc > 1) ? (inputFile + "out.txt") : "output.txt";
	
	cout << inputFile << '\n' << outputFile << '\n';
	
	ifstream in;
	ofstream out;
	in.open(inputFile);
	out.open(outputFile);
	out.precision(15);

	int tests;
	in >> tests;
	cout << "tests : " << tests << '\n';
	for (int test = 1; test <= tests; ++test) {
		out << "Case #" << test << ": ";
		// Grab input
		in >> k >> c >> s;
		// Solve the problem and give feedback to the end user;
		//out << solve(out) << endl;
		solve(out);
		cerr << "cerr check : " << test << endl;
	}

	in.close();
	out.close();

	cout << inputFile << '\n' << outputFile << '\n';

	cin.get();
	return 0;
}