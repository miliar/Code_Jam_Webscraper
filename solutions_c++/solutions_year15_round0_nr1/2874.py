#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t++ < T;) {
		int n; string s;
		cin >> n >> s;

		int standing = 0, add = 0;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] - '0' && standing < i) {
				add += i - standing;
				standing = i;
			}
			standing += s[i] - '0';
		}
		cout << "Case #" << t << ": " << add << endl;
	}
}