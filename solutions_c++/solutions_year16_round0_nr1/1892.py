#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		long long num;
		cin >> num;
		long long ans = num;
		unordered_set<char> s;
		string temp = to_string(ans);
		for (char x : temp) {
			s.insert(x);
		}
		while (s.size() != 10 && ans > 0) {
			ans += num;
			for (char x : to_string(ans)) {
				s.insert(x);
			}
		}
		if (ans <= 0) {
			cout << "Case #" << (i+1) << ": " << "INSOMNIA" << endl;
		} else {
			cout << "Case #" << (i+1) << ": " << ans << endl;
		}
	}
}
