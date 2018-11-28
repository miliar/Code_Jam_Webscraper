#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main () {
	freopen("reverse_pancake.txt", "w", stdout);
	int T,l;
	cin >> T;
	string s;
	bool ish = false;
	int res;
	for (int t = 1; t <= T; t++) {
		cin >> s;

		ish = (s[0] == '+')? true : false;
		l = s.length();
		res = 0;
		for (int i = 1; i < l ; i++) {
			if (ish && s[i] == '-') {
				ish = false;
				res++;
			}

			if (!ish && s[i] == '+') {
				ish = true;
				res++;
			}
		}
		if (!ish)res++;

		cout << "Case #" << t << ": " << res << "\n";

	}
	return 0;
}