#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

void update(int n, set<int> &s) {
	while (n) {
		s.insert(n % 10);
		n /= 10;
	}
}

int solve(int N) {
	set<int> s;
	for (int i = 1; ; ++i) {
		update(i * N, s);
		if (s.size() == 10) return i;
	}
}

int main() {
	int T;
	cin >> T;

	for (int tt = 1; tt <= T; ++tt) {
		cout << "Case #" << tt << ": ";
		int N;
		cin >> N;
		if (N == 0) cout << "INSOMNIA\n";
		else cout << solve(N) * N << '\n';
	}

	return 0;
}