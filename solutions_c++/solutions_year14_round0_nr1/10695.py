#include <iostream>

using namespace std;

int main() {
	int num, first, second;
	int play[4];
	int play2[4];
	int cnt, target;
	int tmp;

	cin >> num;
	for (int k = 0; k < num;k++) {
		cnt = 0;
		target = 0;

		cin >> first;

		for (int i = 0;i < 4;i++) {
			for (int j = 0; j < 4;j++) {
				cin >> tmp;
				if (first == i+1) {
					play[j] = tmp;
				}
			}
		}

		// cout << play[0] << " " << play[1] << endl;
		cin >> second;
		for (int i = 0;i < 4;i++) {
			for (int j = 0; j < 4;j++) {
				cin >> tmp;
				if (second == i+1) {
					play2[j] = tmp;
				}
			}
		}

		for (int i = 0;i < 4;i++) {
			for (int j = 0;j < 4;j++) {
				if (play[i] == play2[j]) {
					cnt++;
					target = play[i];
				}
			}
		}

		cout << "Case #" << k+1 << ": ";

		if (cnt == 1)
			cout << target << endl;
		else if (cnt > 1)
			cout << "Bad magician!" << endl;
		else 
			cout << "Volunteer cheated!" << endl;
	}

	return 0;
}