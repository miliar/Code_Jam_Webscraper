#include <iostream>
#include <cstdio>
#include <algorithm>
#include <array>
#include <vector>

using namespace std;

int main() {
  int t;
  cin >> t;
  for ( int k = 1; k <= t; k++ ) {
	array<bool, 17> ss;
	fill( ss.begin(), ss.end(), false );
	int r;
	cin >> r;
	r--;
	array<int, 16> table;
	for ( int i = 0; i < 16; i++ ) {
	  cin >> table[ i ];
	}
	for ( int i = 4 * r; i < 4 * ( r + 1 ); i++ ) {
	  ss[ table[ i ] ] = true;
	}

	cin >> r;
	r--;
	for ( int i = 0; i < 16; i++ ) {
	  cin >> table[ i ];
	}
	for ( int i = 0; i < 4; i++ ) {
	  for ( int j = 0; j < 4; j++ ) {
		if ( i == r ) {
		  ss[ table[ 4 * i + j ] ] &= true;
		} else {
		  ss[ table[ 4 * i + j ] ] = false;
		}
	  }
	}
	
	int c = count( ss.begin(), ss.end(), true );
	cout << "Case #" << k << ": ";
	if ( c == 0 ) {
	  cout << "Volunteer cheated!" << endl;
	} else if ( c == 1 ) {
	  cout << distance( ss.begin(), find( ss.begin(), ss.end(), true ) ) << endl;
	} else {
	  cout << "Bad magician!" << endl;
	}
  }
}
