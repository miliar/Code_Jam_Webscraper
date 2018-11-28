#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
	int t = 0;
	int a = 0;
	int b = 0;
	int m = 0;
	int hit = 0;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> a;
		int rows[4] = { 0 };
		int tmp;
		for (int w = 0; w < 4; w++) {
			if (w + 1 != a) {
				cin >> tmp >> tmp >> tmp >> tmp;
				continue;
			}
			for (int h = 0; h < 4; h++) {
				cin >> rows[h];
				//cout << rows[h] << " ";
			}
		}
		//cout << endl;
		cin >> b;
		hit = 0;
		int ans = 0;
		for (int w = 0; w < 4; w++) {
			if (w + 1 != b) {
				cin >> tmp >> tmp >> tmp >> tmp;
				continue;
			}
			for (int h = 0; h < 4; h++) {
				cin >> m;
				//cout << m << " ";
				for (int k = 0; k < 4; k++) {
					if (m == rows[k]) {
						hit++;
						ans = m;
					}
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (hit == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if (hit == 1) {
			cout << ans << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}