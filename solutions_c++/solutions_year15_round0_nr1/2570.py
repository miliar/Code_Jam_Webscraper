/*
 * main.cpp
 *
 *  Created on: 11 ???, 2015 ?.
 *      Author: Tigran
 */



#include <iostream>
#include <string>
#include <cassert>

using std::cin;
using std::cout;
using std::endl;

int solve( const std::string& s )
{
	int r = 0; // needed people
	int a = 0; // number of people clapping
	for ( int i = 0; i < (int)s.length(); ++i ) {
		int cnt = s[ i ] - '0';
		if ( a < i ) {
			r += i - a;
			a = i;
		}
		a += cnt;
	}
	return r;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int n;
		std::string s;
		cin >> n >> s;
		assert( (int)s.length() == n + 1 );
		cout << "Case #" << tc << ": " << solve( s ) << endl;
	}
	return 0;
}
