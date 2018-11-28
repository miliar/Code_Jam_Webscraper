#include <iostream>
using namespace std;

int solve(string s) {
	int ans = 0;
	char prev = '+';
	for (int i = s.size() - 1; i >= 0; i--) {
		if (s[i] != prev) {
			ans++;
			prev = s[i];
		}
	}
	return ans;
}

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		string S; cin >> S;
		cout << "Case #" << No << ": ";
		cout << solve(S) << endl;
	}
	return 0;
}
