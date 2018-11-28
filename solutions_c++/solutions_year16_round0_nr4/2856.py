#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int K, C, S;
		cin >> K >> C >> S;

		cout << "Case #" << t << ':';
		if (C * S < K) cout << " IMPOSSIBLE";
		else {
			int counter = 0;
			while (counter < K) {
				long long position = 0;
				for (int i = 0; i < C; i++) {
					position = (position * K) + (counter < K ? counter : 0);
					counter++;
				}
				cout << ' ' << (position+1);
			}
		}
		cout << '\n';
	}

	return 0;
}
