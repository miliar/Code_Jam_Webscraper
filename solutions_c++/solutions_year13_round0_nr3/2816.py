// fs.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

bool IsPalindrome( unsigned long n ) {
	ostringstream ostr;
	ostr << n;
	string str = ostr.str();
	for( unsigned i = 0; i < str.size()/2; i++ ) {
		if( str[i] != str[ str.size()-1-i ] ) return false;
	}
	return true;
}
unsigned long NumPalindromes( unsigned long a, unsigned long b ) {
	unsigned long x = 1;
	while( x*x < a ) x++;
	unsigned long cnt = 0;
	while( x*x <= b ) {
		if( IsPalindrome( x ) && IsPalindrome( x*x ) ) cnt++;
		x++;
	}
	return cnt;
}

int _tmain(int argc, _TCHAR* argv[])
{
	string mainfile = "small.txt";
	string infile = string("../") + mainfile;
	string outfile = string("../out") + mainfile;
	cout << outfile << endl;
	ifstream data( infile );
	ofstream outdata( outfile );
	int T;
	data >> T;
	for( int t = 1; t <= T; t++ ) {
		unsigned long a, b;
		data >> a >> b;
		outdata << "Case #" << t << ": " << NumPalindromes( a, b ) << endl;
	}
	outdata.close();
	data.close();
	return 0;
}

