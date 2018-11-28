#include <iostream>
using namespace std;

int main() {
	int T, N, temp;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":";
		cin >> N >> temp >> temp;
		for (int j = 1; j <= N; j++) {
			cout << " " << j;
		}
		cout << "\n";
	}
	return 0;
}