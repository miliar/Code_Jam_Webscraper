#include <iostream>
#include <string>
using namespace std;

int main()  {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;

	for (int tc = 1; tc <= T; ++tc) {
		string s;
		cin >> s;

		int c = 0;
		char prev = 0;

		for (size_t i = 0; i < s.length(); ++i) {
			if (s[i] == prev) continue;

			++c, prev = s[i];
		}

		if (s.back() == '+') --c;
		cout << "Case #" << tc << ": " << c << endl;
	}

}
