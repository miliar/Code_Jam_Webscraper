#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)

// Premature optimization is the root of all evil

using namespace std;


void solveacase() {

	int R, C;
	cin >> R >> C;

	cin.get();
	char grid[C][R];
	forn(y, R) {
		forn(x, C) {
			grid[x][y] = cin.get();
		}
		cin.get();
	}

	int ans = 0;

	forn(x, C) {
		int n = 0;
		bool firstbad = false;
		bool lastbad = false;
		int loc = 0;
	
		forn(y, R) {
			if ( grid[x][y] != '.' ) {
				if ( n == 0 ) {
					firstbad = grid[x][y] == '^';
					loc = y;
				}
				++n;
				lastbad = grid[x][y] == 'v';
			}


		}

		if ( n == 1 ) {
			int m = 0;
			forn(x, C) {
				if ( grid[x][loc] != '.' ) ++m;
			}
			if ( m == 1 ) {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}

		if ( firstbad ) ++ans;
		if ( lastbad ) ++ans;
	}

	forn(y, R) {
		int n = 0;
		bool firstbad = false;
		bool lastbad = false;
	
		forn(x, C) {
			bool danger = false;
			if ( grid[x][y] != '.' ) {
				if ( n == 0 ) {
					firstbad = grid[x][y] == '<';
				}
				++n;
				lastbad = grid[x][y] == '>';
			}

		}
		if ( firstbad ) ++ans;
		if ( lastbad ) ++ans;
	}

	cout << ans << endl;
}

int main ( int, char** ) {

	int T;
	cin >> T;

	for ( int i = 1; i <= T; ++i ) {
		cout << "Case #" << i << ": ";
		solveacase();
	}


	return 0;
}
