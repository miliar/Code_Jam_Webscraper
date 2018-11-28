#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long ll;

stringstream ss;

#define DEBUG(A) cerr << "\tDEBUG: " << #A << " = " << A << "\n"

void testCase() {
	int selection[2];
	int grid[2][4][4];
	int chosen[17];
	for ( int i = 1 ; i <= 16 ; i++ ) {
		chosen[i] = 0;
	}
	for ( int i = 0 ; i < 2 ; i++ ) {
		cin >> selection[i];
		for ( int j = 0 ; j < 4 ; j++ ) {
			for ( int k = 0 ; k < 4 ; k++ ) {
				cin >> grid[i][j][k];
				if ( j == selection[i]-1 ) {
					chosen[grid[i][j][k]]++;
				}
			}
		}
	}
	int ans = -1;
	int counter = 0;
	for ( int i = 1 ; i <= 16 ; i++ ) {
		if ( chosen[i] == 2 ) {
			ans = i;
			counter++;
		}
	}
	if ( counter == 0 ) {
		ss << "Volunteer cheated!";
	} else if ( counter == 1 ) {
		ss << ans;
	} else {
		ss << "Bad magician!";
	}
}

int main() {
	int t;
	cin >> t;
	for ( int i = 0 ; i < t ; i++ ) {
		ss << "Case #"<<(i+1)<<": ";
		testCase();
		ss << endl;
	}
	cout << ss.str();
	return 0;
}

