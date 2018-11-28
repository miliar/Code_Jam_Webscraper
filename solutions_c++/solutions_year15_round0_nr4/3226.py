#include <iostream>

#define FOR(i, n) for (UI i = 0; i < n;++i)
using namespace std;

typedef unsigned int UI;

UI T;

void run() {
	UI X, R, C;
	cin >> X >> R >> C;

	switch (X) {
		case 1:
			cout << "GABRIEL" << endl;
			break;
		case 2:
			if (R % 2 == 0 || C % 2 == 0)
				cout << "GABRIEL" << endl;
			else
				cout << "RICHARD" << endl;
			break;
		case 3:
			if ((R % 3 == 0 || C % 3 == 0) && R > 1 && C > 1)
				cout << "GABRIEL" << endl;
			else
				cout << "RICHARD" << endl;
			break;
		case 4:
			if (R<=2 || C <= 2) {
				cout << "RICHARD" << endl;
				break;
			}
			if (R % 4 == 0 || C % 4 == 0 || (C % 2 == 0 && R % 2 == 0))
				cout << "GABRIEL" << endl;
			else
				cout << "RICHARD" << endl;
	}
}

int main() {
	cin >> T;
	FOR(i, T) {
		cout << "Case #" << i+1 << ": ";
		run();
	}
	return 0;
}
