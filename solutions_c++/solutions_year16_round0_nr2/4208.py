#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		string str;
		cin >> str;
		str.push_back('+');
		char last = str[0];
		int cnt = 0, len = str.size();

		for (int i = 1; i < len; ++i)
			if (str[i] != last) {
				last = str[i];
				++cnt;
			}

		cout << "Case #" << t << ": " << cnt << endl;
	}

	return 0;
}