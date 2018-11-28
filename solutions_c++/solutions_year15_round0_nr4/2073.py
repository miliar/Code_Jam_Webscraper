#include <iostream>
#include <cmath>
using namespace std;

bool solve() {

	int X,R,C;
	cin >> X >> R >> C;

	float fill = R * C;
	if ( (fill / X) != floor(fill / X)) {
		return false;
	}

	switch(X) {
		case 1:
			return true;
			break;
		case 2:
			return true;
			break;
		case 3:
			if (R >= 2 && C >= 2) return true;
			break;
		case 4:
			if (R >= 3 && C >= 3) return true;
			break;
		default:

			break;

	}

	return false;
}

int main () {

    int t = 0;
    cin >> t;

    bool res;

    for (int i = 0; i < t; ++i) {
        res = solve();
        cout << "Case #" << (i+1) << ": "; 
        if (res) cout << "GABRIEL" << '\n';
        else cout << "RICHARD" << '\n';         
    }

}