#include <iostream>
#include <string>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int tc = 1; tc <= cases; tc++) {
		int max_s;
		string s;
		cin >> max_s >> s;

		int people = 0;
		int answer = 0;
		for (int i = 0; i < s.size(); i++) {
			if (i != 0) {
				if (people < i) {
					int diff = i - people;
					answer += diff;
					people += diff;
				}
			}
			people += (int)(s[i] - '0');
		}

		cout << "Case #" << tc << ": " << answer << endl;
	}
	return 0;
}