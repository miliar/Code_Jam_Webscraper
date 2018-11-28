#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int res = 0;
		for (int i = 1; i < (int)s.size(); i++)
			if (s[i] != s[i-1])
				res++;
		if (s[s.size()-1] == '-')
			res++;
		cout << "Case #" << t << ": " << res << endl;
	}
}
