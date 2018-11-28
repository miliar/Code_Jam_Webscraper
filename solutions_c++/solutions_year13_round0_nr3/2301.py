#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <iterator>

using namespace std;

// #define DEV 1
#define LL long long

const LL MAXN = 1000 * 1000 * 10;

string LLtoStr( LL n ) {
	string temp;
	stringstream strstream;
	strstream << n;
	strstream >> temp;
	return temp;
}

bool isValid( string s ) {
	if( s.length() < 2 )
		return true;

	for( int i = 0; i < s.length(); ++i )
		if( s[ i ] > '2' )
			return false;
	return true;
}

bool checkpalind( string n ) {
	int l = n.length();
	int i = 0;
	while( i < l/2 ) {
		if( n[i] != n[l-1-i] )
			return false;
		i++;
	}
	return true;
}

bool checkpalindnum( LL n ) {
	/*
	string temp = "";
	while( n != 0 ) {
		int k = n % 10;
		n /= 10;
		temp = (char)(k + '0') + temp;
	}
	*/

	string temp = LLtoStr( n );
	return checkpalind( temp );
}

int main() {
	#ifndef DEV
		freopen( "C-large-1.in", "r", stdin );
		freopen( "C-large-1.out", "w+", stdout );
	#endif

	
	set< LL > nums;
	
	
	for( LL i = 1; i <= MAXN; ++i ) {
		if( nums.size() == 39 )
			break;

		string temp = LLtoStr( i );

		if( checkpalind( temp ) && checkpalindnum( i * i ) ) {
			nums.insert( nums.end(), i*i );
		}
		
	}

	int t;

	cin>>t;
	
	for( int i = 0; i < t; ++i ) {
		LL x, y;
		cin>>x>>y;

		set< LL >::iterator it = nums.lower_bound( x );
		set< LL >::iterator it2 = nums.upper_bound( y );
		int te = distance( it, it2 );

		cout<< "Case #" << i+1 << ": " << te <<endl;
	}

	#ifdef DEV
		system( "PAUSE" );
	#endif
	return 0;
}
