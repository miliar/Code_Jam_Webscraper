#include <iostream>
using namespace std;

string solve(int x) {
	if (!x) return "INSOMNIA";
	bool used[10];
	int count = 0;
	int k = x;
	int xx = x;
	while (true) {
		while (k) {
			int c = k % 10;
			if (!used[c]) {
				count++;
				used[c] = true;
			}
			k /= 10;
		}
		if (count == 10) break;
		k = (xx += x);
	}
	return to_string(xx);
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int x; cin >> x;
		cout << "Case #" << t << ": " << solve(x) << endl;
	}
}
