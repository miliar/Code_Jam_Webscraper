#include <iostream>
#include <fstream>

using namespace std;

int main() {
	string s, res;
	int tst;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tst;
	for(int t = 1; t <= tst; ++t) {
		cin >> s;
		res = "";
		res += s[0];
		for(int i = 1; i < s.size(); ++i) {
			if(s[i] >= res[0]) {
				string tmp = "";
				tmp += s[i];
				res = tmp + res;
			}
			else
				res += s[i];
		}
		cout << "Case #" << t << ": " << res << '\n';
	}
}