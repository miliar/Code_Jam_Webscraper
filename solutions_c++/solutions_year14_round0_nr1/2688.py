#include <iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (size_t tsc = 1; tsc <= t; tsc++) {

		int ans1, ans2;
		int v1[4][4], v2[4][4];

		cin >> ans1;
		ans1--;
		for (size_t i = 0; i < 4; i++) {
			for (size_t j = 0; j < 4; j++) {
				cin >> v1[i][j];
			}
		}

		cin >> ans2;
		ans2--;
		for (size_t i = 0; i < 4; i++) {
			for (size_t j = 0; j < 4; j++) {
				cin >> v2[i][j];
			}
		}

		int cnt = 0;
		int val = 1;
		for (size_t i = 0; i < 4; i++) {
			for (size_t j = 0; j < 4; j++) {
				if (v1[ans1][i] == v2[ans2][j]) {
					cnt++;
					val = v1[ans1][i];
				}
			}
		}
		cout << "Case #" << tsc<<": ";
		if (cnt == 0) {
			cout << "Volunteer cheated!";
		}
		else if (cnt == 1) {
			cout << val;
		}
		else {
			cout << "Bad magician!";
		}
		cout << "\n";
	}
}