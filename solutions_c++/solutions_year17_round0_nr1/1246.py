#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

int main() {
	int t, tbk;
	char s[1001];
	int c;
	int l;
	int k;
	cin >> t;
	tbk = t;
	while (t) {
		t--;
		c = 0;
		cin >> s >> k;
		cout << "Case #" << tbk - t << ": ";
		l = strlen(s);
		for (int i = 0; i <= l-k; i++) {
			if (s[i] == '+')
				continue;
			for (int j = 0; j < k; j++) {
				s[i+j] = (s[i+j] == '-' ? '+' : '-');
			}
			c++;
		}
		for (int i = l-k+1; i < l; i++) {
			if (s[i] == '-') {
				cout << "IMPOSSIBLE" << endl;
				break;
			}
			if (i == l-1) {
				cout << c << endl;
			}
		}
	}
}
