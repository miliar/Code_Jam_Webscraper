#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int a1, a2;
		int n[16];
		int tmp;

		for (int i = 0; i < 16; i++)
			n[i] = 1;

		cin >> a1;
		for (int i = 0; i < 4; i++) {
			if (i + 1 == a1) {
				for (int j = 0; j < 4; j++) {
					cin >> tmp;
				}
			}
			else {
				for (int j = 0; j < 4; j++) {
					cin >> tmp;
					n[tmp-1] = 0;
				}
			}
		}

		cin >> a2;
		for (int i = 0; i < 4; i++) {
			if (i + 1 == a2) {
				for (int j = 0; j < 4; j++) {
					cin >> tmp;
				}
			}
			else {
				for (int j = 0; j < 4; j++) {
					cin >> tmp;
					n[tmp-1] = 0;
				}
			}
		}

		int count = 0;
		int answer = -1;
		for (int i = 0; i < 16; i++) {
			if (n[i] == 1) {
				count++;
				answer = i + 1;
			}
		}

		cout << "Case #" << t << ": ";
		if (count == 0) {
			cout << "Volunteer cheated!";
		}
		else if (count > 1) {
			cout << "Bad magician!";
		}
		else {
			cout << answer;
		}
		cout << endl;

	}
}
