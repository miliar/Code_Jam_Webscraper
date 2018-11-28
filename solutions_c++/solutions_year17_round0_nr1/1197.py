#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		int K;
		cin >> s >> K;

		int c = 0;
		for (size_t i = 0; i <= s.length() - K; i++) {
			if (s[i] == '+') continue;
			for (size_t j = i; j < i + K; j++) {
				s[j] = s[j] == '+' ? '-' : '+';
			}
			c++;
		}

		if (s.find('-') == string::npos) {
			printf("Case #%d: %d\n", t, c);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}

	return 0;
}