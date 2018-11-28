#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;

unsigned solve() {
	unsigned N, X;
	cin >> N >> X;
	assert(N > 0 && N <= 10000);
	assert(X > 0 && X <= 700);
	vector<unsigned> s(N);
	for (unsigned i = 0; i < N; i++) {
		cin >> s[i];
		assert(s[i] > 0 && s[i] <= X);
	}
	sort(s.begin(), s.end(), greater<unsigned>());
	for (unsigned i = 0; i < s.size() - 1; i++) {
		if (s[i] + s.back() <= X)
			s.pop_back();
	}
	return s.size();
}

int main() {
	int T;
	cin >> T;
	assert(T > 0 && T <= 100);
	for (int i = 0; i < T; i++) {
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
	}
	return 0;
}
