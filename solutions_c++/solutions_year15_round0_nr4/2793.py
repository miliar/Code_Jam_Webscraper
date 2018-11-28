#include <iostream>
using namespace std;
int t, x, r, c;

int task() { // 0 = rechard, 1 = gabriel
	if (x == 1) {
		return 1;
	}
	else if (x == 2) {
		if (r*c % 2 == 0) {
			return 1;
		}
		else {
			return 0;
		}
	}
	else if (x == 3) {
		if (r*c == 6 || r*c==12||r*c==9) {
			return 1;
		}
		else return 0;
	}
	else {
		if (r*c == 12 || r*c == 16) return 1;
		return 0;
	}
}

int main() {
	freopen("D-small-attempt4.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> t;

	for (int k = 1; k <= t; k++){
		cin >> x >> r >> c;
		int answer=task();
		//cout << x <<" "<< r <<" "<<c;
		if (answer == 0) {
			cout << "Case #" << k << ": " << "RICHARD" << endl;
		}
		else {
			cout << "Case #" << k << ": " << "GABRIEL" << endl;
		}
	}

}