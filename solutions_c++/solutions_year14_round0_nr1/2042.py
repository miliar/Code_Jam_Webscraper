#include <iostream>
#include <cstdio>
using namespace std;

int solve(int r1, int* b1, int r2, int* b2) {
	int cnt[16];
	for (int i = 0; i < 16; i++) {
		cnt[i] = 0;
	}
	for (int i = 0; i < 4; i++) {
		int k1 = (r1 - 1) * 4 + i;
		int k2 = (r2 - 1) * 4 + i;
		cnt[b1[k1] - 1] ++;
		cnt[b2[k2] - 1] ++;
	}
	int ans = -1;
	for (int i = 0; i < 16; i++) {
		if (cnt[i] > 1) {
			if (ans > -1) {
				return 0;
			}
			ans = i + 1;
		}
	}
	return ans;
}

int main() {
	int T, r1, r2;
	int b1[16], b2[16];
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> r1;
		for (int j = 0; j < 16; j++) {
			cin >> b1[j];
		}
		cin >> r2;
		for (int j = 0; j < 16; j++) {
			cin >> b2[j];
		}
		int ans = solve(r1, b1, r2, b2);
		cout << "Case #" << (i + 1) << ": ";
		if (ans == -1) {
			cout << "Volunteer cheated!\n";
		} else if (ans == 0) {
			cout << "Bad magician!\n";
		} else {
			cout << ans << "\n";
		}	
	}
	return 0;
}
