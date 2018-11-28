#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int possible[2] = {0, 0};
		for (int i = 0; i < 2; ++i) {
			int answer; // not 42 :(
			cin >> answer;
			--answer;
			for (int r = 0; r < 4; ++r) {
				for (int c = 0; c < 4; ++c) {
					int num;
					cin >> num;
					if (r == answer) {
						--num;
						possible[i] |= 1 << num;
					}
				}
			}
		}
		possible[0] &= possible[1];
		cout << "Case #" << t << ": ";
		switch (__builtin_popcount(possible[0])) {
			case 0:
				cout << "Volunteer cheated!";
				break;
			case 1:
				cout << 32 - __builtin_clz(possible[0]);
				break;
			default:
				cout << "Bad magician!";
		}
		cout << endl;
	}
}
