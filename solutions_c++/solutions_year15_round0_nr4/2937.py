#include <iostream>
#include <queue>

using namespace std;

int main() {
	int T;

	cin >> T;
	for (int c=1; c<=T; c++) {
		int X, R, C;
		bool gabriel = false;
		cin >> X >> R >> C;
		if ((R * C) % X == 0) {
			if (X==1) {
				gabriel = true;
			} else if (X==2) {
				gabriel = true;
			} else if (X==3) {
				if ((2<=C&&3<=R)
					|| (3<=C&&2<=R))
					gabriel = true;
			} else if (X==4) {
				if ((3<=C && 4<=R)
					|| (4<=C && 3<=R)) {
					gabriel = true;
				}
			}
		}

		if (gabriel)
			cout << "Case #" << c << ": " << "GABRIEL" << endl;
		else
			cout << "Case #" << c << ": " << "RICHARD" << endl;
	}

	return 0;
}