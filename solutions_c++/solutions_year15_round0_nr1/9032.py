#include <iostream>
#include <string>

using namespace std;

int main() {
	int cases;
	int maxshy;
	string shyaud;

	cin >> cases;


	for (int c = 0; c < cases; c++) {
		int aud = 0;
		int expectate = 0;
		int guest = 0;

		cin >> maxshy >> shyaud;

		for (int i = 0; i < maxshy+1; i++) {
			expectate = i;



			if (aud < expectate) {
				if (guest < (expectate - aud)) {
					guest = expectate - aud;
				}
			}
			aud += shyaud[i] - '0';

		}

		aud = maxshy - aud;
		if (aud < 0) {
			aud = 0;
		}
		cout << "Case #" << c+1 << ": " << guest << endl;

	}
}
