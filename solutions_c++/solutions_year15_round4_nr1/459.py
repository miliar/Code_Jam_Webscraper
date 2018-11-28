#include <cassert>
#include <string>
#include <sstream>
#include <iostream>
#include <deque>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstring>

using namespace std;

typedef pair<int,int> PI;
typedef long long LL;
char b[104][104];

const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};
const char* direction = "^>v<"; 

int dir_index( char c ) {
	switch( c ) {
	case '^':
		return 0;
	case '>':
		return 1;
	case 'v':
		return 2;
	case '<':
		return 3;
	default:
		assert(0);
	}
	return -1;
}

int rows, cols;

bool get_next( int r, int c, int dir, int& r2, int& c2 ) {
	r2 = r + dr[dir];
	c2 = c + dc[dir];
	
	bool foundOther = false;
	while( 0 <= r2 && r2 < rows && 0 <= c2 && c2 < cols ) {
		if( b[r2][c2] != '.' ) {
			return true;
		}
		r2 += dr[dir];
		c2 += dc[dir];
	}
	return false;
}

int main() {
	int cases;

	cin >> cases;

	for( int caseno = 1; caseno <= cases; ++caseno ) {
		cout << "Case #" << caseno << ": ";
		cin >> rows >> cols;
		for( int r =0 ; r < rows; ++r ) {
			cin >> b[r];
		}
		int res = 0;
		for( int r = 0; r < rows; ++r ) {
			for( int c = 0; c < cols; ++c ) {
				if( b[r][c] != '.' ) {
					int dir = dir_index( b[r][c] );
					int r2; 
					int c2;
					
					if( !get_next( r, c, dir, r2, c2 ) ) {
						bool found = false;
						for( int dir2 = 0; dir2 < 4; ++dir2 ) {
							if( dir2 == dir ) continue;
							if( get_next( r, c, dir2, r2, c2 ) ) {
								b[r][c] = direction[dir2];
								++res;
								found = true;
								break;
							}
						}
						if( !found ) goto impossible;
					}
				}
			}
		}
		cout << res << endl;
		continue;
	impossible:;
		cout << "IMPOSSIBLE\n";
	}
	return 0;
}

