#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;

	for (int tt = 1; tt <= T; ++tt) {
		int K, C, S;
		cin >> K >> C >> S;
		cout << "Case #" << tt << ": ";
		for (int j = 1; j <= S; ++j) {
			cout << j << ' ';
		}
		cout << '\n';
	}

	return 0;
}