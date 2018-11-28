#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve() {
	int N, X;
	cin >> N >> X;
	vector<int> s(N);
	for (int i = 0; i < N; ++i)
		cin >> s[i];
	sort(s.begin(), s.end());
	int i = 0, j = N-1;
	int res = 0;
	while (i <= j) {
		++res;
		if (i == j)
			break;
		int sum = s[i] + s[j];
		if (sum > X) {
			--j;
		}
		else {
			--j;
			++i;
		}
	}
	return res;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
