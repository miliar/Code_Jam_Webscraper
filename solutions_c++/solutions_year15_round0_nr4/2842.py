#include <iostream>
#include <fstream>
using namespace std;

int tt;

bool enumerate(int x, int r, int c) {
	if(r * c % x != 0) return false;
	
	if(x == 1) {
		return true;
	}
	
	if(x == 2) {
		if(r % 2 == 0 || c % 2 == 0) {
			return true;
		}
		
		return false;
	}
	
	if(x == 3) {
		// * * *
		if(r < 3 && c < 3) {
			return false;
		}

		// *
		// * *		
		if(r == 1 || c == 1) {
			return false;
		}
		
		return true;
	}
	
	if(x == 4) {
		// * * * *
		if(r < 4 && c < 4) {
			return false;
		}
		
		// * *
		// * *
		if(r == 1 || c == 1) {
			return false;
		}
		
		// * *
		//   * *
		if(r == 4 && c == 2 || r == 2 && c == 4) {
			return false;
		}
		
		return true;
	}
}

int main() {
	ifstream cin("input");
	
	cin >> tt;
	for(int cc=1; cc<=tt; cc++) {
		cout << "Case #" << cc << ": ";
		
		int x, r, c;
		cin >> x >> r >> c;
		
		if(enumerate(x, r, c)) {
			cout << "GABRIEL" << endl;
		}
		else {
			cout << "RICHARD" << endl;
		}
	}
	
	cin.close();
	return 0;
}
