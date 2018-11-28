#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

const int CARD = 16,
		  ROW = 4,
		  COL = 4;

int main ( void )
{
	int T;
	cin >> T;

	for ( int t = 1; t <= T; ++t ) {
		int cards[CARD] = { 0 },
			row;

		for ( int i = 0; i < 2; ++i ) {
			cin >> row;
			for ( int r = 0; r < ROW; ++r ) {
				for ( int c = 0; c < COL; ++c ) {
					int num;
					cin >> num;
					if ( r == row - 1 ) {
						++cards[num - 1];
					}
				}
			}
		}

		set<int> s1, s2;
		for ( int i = 0; i < CARD; ++i ) {
			if ( cards[i] == 1 ) {
				s1.insert( i + 1 );
			}
			if ( cards[i] == 2 ) {
				s2.insert( i + 1 );
			}
		}
		cout << "Case #" << t << ": ";
		if ( s2.size() == 1 ) {
			cout << *s2.begin();
		}
		else if ( s2.size() == 0 ) {
			cout << "Volunteer cheated!";
		}
		else {
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
};
