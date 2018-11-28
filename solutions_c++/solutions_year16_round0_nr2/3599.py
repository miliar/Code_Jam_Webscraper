#include <fstream>

using namespace std;

ifstream cin("in");
ofstream cout("out");

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int res = 0;
		string s;
		cin >> s;
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] != s[i - 1]) ++res;
		}
		if (res % 2 && s[0] == '+') ++res;
		if (res % 2 == 0 && s[0] == '-') ++res;
		cout << "Case #" << i + 1 << ": " << res << '\n';
	}
}
