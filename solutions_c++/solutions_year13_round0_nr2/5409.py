#include <iostream>
using namespace std;

int N, M;
int board[10][10];

string solve() {

	for( int r = 0 ; r < ( 1 << N ) ; ++r ) for ( int c = 0 ; c < ( 1 << M ) ; ++c ) {
		bool ok = true;
		for( int i = 0 ; i < N ; ++i ) for( int j = 0 ; j < M ; ++j ) {
			if ( (r>>i) & 1 || (c>>j) & 1 ) {
				if( !board[i][j] ) {
					ok = false;
					goto Fail;
				}
			}
			else {
				if( board[i][j] ) {
					ok = false;
					goto Fail;
				}
			}
		}
		Fail:
			if( ok ) return "YES";	

	}

	return "NO";
}

int main() {
	int ncase;

	cin >> ncase;

	for( int caseno = 1 ; caseno <= ncase ; ++caseno ) {
		cin >> N >> M;
		for( int i = 0 ; i < N ; ++i ) for( int j = 0 ; j < M ; ++j ) {
			cin >> board[i][j];
			board[i][j] = 2 - board[i][j]; 
		}
		cout << "Case #" << caseno << ": ";
		cout << solve() << endl;	
	}

}
