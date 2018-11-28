#include <iostream>
using namespace std;
int cur;
int guess;
int T;
int first_row[4];
int main() {
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int count = 0;
		int num[4];
		cin >> guess;
		for (int j = 1; j <= 4; j++) {
			if (j == guess) {
				for (int k = 1; k <= 4; k++) {
					cin >> first_row[k-1];	
				}
			}
			else
				for (int k = 1; k <= 4; k++)
					cin >> cur;
		}

		cin >> guess;
		for (int j = 1; j <= 4; j++) {
			if (j == guess) {
				for (int k = 1; k <= 4; k++) {
					cin >> cur;	
					for (int p = 0; p < 4; p++) {
						if (cur == first_row[p]) {
							num[count] = cur;
							count++;
						}
					}
				}
			}
			else
				for (int k = 1; k <= 4; k++)
					cin >> cur;
		}
		if (count == 1)
			cout << "Case #" << i << ": " << num[0] << endl;
		else if (count > 1)
			cout << "Case #" << i << ": Bad magician!" << endl;
		else
			cout << "Case #" << i << ": Volunteer cheated!" << endl;

	}
}
