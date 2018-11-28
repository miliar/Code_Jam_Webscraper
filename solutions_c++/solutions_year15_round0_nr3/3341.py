#include <iostream>
#include <algorithm>
using namespace std;

char arr[5][5] =
{
		{0, 0, 0, 0, 0},
		{0, 1, 2, 3, 4},
		{0, 2, -1, 4, -3},
		{0, 3, -4, -1, 2},
		{0, 4, 3, -2, -1}
};

int main(int argc, char* argv[]) {
	freopen("C-small-attempt1.in","r",stdin); freopen("Dijkstra.out","w",stdout);
	int T;
	cin >> T;
	for (int aaa = 1; aaa <= T; aaa++) {
		int L, X;
		cin >> L >> X;
		string s;
		cin >> s;

		for (int i = 0; i < s.size(); i++) {
			if (s[i] == 'i') s[i] = '2';
			else if (s[i] == 'j') s[i] = '3';
			else s[i] = '4';
		}

		bool eye = false;
		bool jay = false;
		bool kay = false;
		int i = 0;

		int sign = 1;
		int c = 1;
		while (i < s.size()) {
			c = arr[c][s[i] - '0'];
			if (c < 0) {
				c = -c;
				sign *= -1;
			}

			i++;
			if (i == s.size() && X > 1) {
				i = 0;
				X--;
			}

			if (c * sign == 2) {
				eye = true;
				break;
			}
		}

		sign = 1;
		c = 1;
		while (i < s.size()) {
			c = arr[c][s[i] - '0'];
			if (c < 0) {
				c = -c;
				sign *= -1;
			}

			i++;
			if (i == s.size() && X > 1) {
				i = 0;
				X--;
			}

			if (c * sign == 3) {
				jay = true;
				break;
			}
		}

		sign = 1;
		c = 1;
		while (i < s.size()) {
			c = arr[c][s[i] - '0'];
			if (c < 0) {
				c = -c;
				sign *= -1;
			}

			i++;
			if (i == s.size() && X > 1) {
				i = 0;
				X--;
			}
		}
		if (c * sign == 4) {
			kay = true;
		}

		if (eye && jay && kay) {
			cout << "Case #" << aaa << ": YES\n";
		} else {
			cout << "Case #" << aaa << ": NO\n";
		}
	}
}
