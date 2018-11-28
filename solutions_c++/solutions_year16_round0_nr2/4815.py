#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

char s[110];

int fun(int a) {
	while (a >= 0 && s[a] == '+') a--;
	return a;
}

int main() {
	//freopen("in.txt", "r", stdin);
	int T, cas = 1;
	cin >> T;
	while (T--) {
		cout << "Case #" << cas++ << ": ";
		cin >> s;
		int pos = (int)strlen(s) - 1, ans = 0;
		while (1) {
			pos = fun(pos);
			//cout << pos << endl;
			if (pos == -1) break;
			if (s[0] == '-') {
				reverse(s, s + pos + 1);
				for (int i = 0; i <= pos; i++) {
					if (s[i] == '+') s[i] = '-';
					else s[i] = '+';
				}
			} else {
				int i = 0;
				while (i < pos && s[i] == '+') {
					s[i] = '-';
					i++;
				}
			}
			//cout << s << endl;
			ans++;
		}
		cout << ans << endl;
	}
	return 0;
}
