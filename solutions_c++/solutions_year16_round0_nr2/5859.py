#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	string s;
	int res, cs = 1, tst;
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for(cin >> tst; tst--; ) {
		cin >> s;
		res = 0;
		for(int i = s.size() - 1; i >= 0; --i) {
			if(s[i] == '-') {
				if(i && s[0] == '+') {
					for(int j = 0; j < s.size() && s[j] == '+'; ++j) {
						s[j] = '-';
					}
					++ res;
				}
				reverse(s.begin(), s.begin() + i + 1);
				for(int j = 0; j <= i; ++j)
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				res ++;
			}
		}
		cout << "Case #" << cs++ << ": " << res << '\n';
	}
	return 0;
}