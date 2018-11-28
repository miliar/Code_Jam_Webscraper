
#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int K, C, S;
		cin >> K >> C >> S;

		for (int i = 1; i <= S; i++) {
			cout << i;
			if (i < S) cout << ' ';
		}
		cout << endl;
	}
	return 0;
}
