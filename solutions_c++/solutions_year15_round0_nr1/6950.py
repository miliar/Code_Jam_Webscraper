#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, S;
	string str;
	cin >> T;
	for (int k = 0; k < T; ++k) {
		int ans = 0, count = 0;
		cin >> S >> str;
		for (int i = 0; i < str.size(); ++i) {
			if (count < i) {
				int delta = i - count;
				ans += delta;
				count += delta;
			}
			count += str[i] - '0';
		}
		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
	return 0;
}