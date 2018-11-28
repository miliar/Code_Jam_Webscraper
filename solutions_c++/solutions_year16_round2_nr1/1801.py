#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int ch[100], a[10];

int main() {
	int t, l, tc = 1;
	string s;
	cin >> t;
	while (t--) {
		cin >> s;
		memset(ch, 0, sizeof ch);
		memset(a, 0, sizeof a);
		l = s.length();
		for (int i = 0; i < l; i++) {
			ch[(int)s[i] - (int)'A' + 1]++;
		}

		while (ch[26]) {
			a[0]++;
			ch[26]--; ch[5]--; ch[18]--; ch[15]--;
		}

		while (ch[23]) {
			a[2]++;
			ch[20]--; ch[23]--; ch[15]--;
		}

		while (ch[21]) {
			a[4]++;
			ch[6]--; ch[15]--; ch[21]--; ch[18]--;
		}

		while (ch[24]) {
			a[6]++;
			ch[19]--; ch[9]--; ch[24]--;
		}

		while (ch[7]) {
			a[8]++;
			ch[5]--; ch[9]--; ch[7]--; ch[8]--; ch[20]--;
		}

		while (ch[15]) {
			a[1]++;
			ch[15]--; ch[14]--; ch[5]--;
		}

		while (ch[8]) {
			a[3]++;
			ch[20]--; ch[8]--; ch[18]--; ch[5]--; ch[5]--;
		}

		while (ch[6]) {
			a[5]++;
			ch[6]--; ch[9]--; ch[22]--; ch[5]--;
		}

		while (ch[19]) {
			a[7]++;
			ch[19]--; ch[5]--; ch[22]--; ch[5]--; ch[14]--;
		}

		while (ch[9]) {
			a[9]++;
			ch[14]--; ch[9]--; ch[14]--; ch[5]--;
		}
		cout << "Case #" << tc++ << ": ";
		for (int i = 0; i < 10; i++) {
			while (a[i]--) {
				cout << i;
			}
		}
		cout << endl;
	}
}