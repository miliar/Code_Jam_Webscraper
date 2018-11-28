#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	int n, row1, row2;
	int values[4] = {};

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> row1;
		for (int j = 1; j <= 4; j++) {
			int value;
			for (int k = 0; k < 4; k++) {
				cin >> value;
				if (j == row1) values[k] = value;
			}
		}

		int found = 0;
		cin >> row2;
		for (int j = 1; j <= 4; j++) {
			int value;
			for (int k = 0; k < 4; k++) {
				cin >> value;
				if (j == row2) {
					if (find(values, values + 4, value) != (values + 4)) {
						if (found == 0) {
							found = value;
						} else if (found > 0) {
							found = -1;
						}
					}
				}
			}
		}

		cout << "Case #" << i << ": ";
		if (found > 0) {
			cout << found;
		} else if (found == -1) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}
}
