#include <iostream>
#include <fstream>
using namespace std;

int n, c[26];

int main() {
	ifstream in("A-large.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("A-large.out");
	cout.rdbuf(out.rdbuf());
	int T, kase = 0, n;
	cin >> T;
	while (T--) {
		int count = 0, mx1, mx2, mx1i, mx2i;
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> c[i],
			count += c[i];
		cout << "Case #" << ++kase << ":";
		while (count != 0) {
			mx1 = mx2 = mx1i = mx2i = -1;
			for (int i = 0; i < n; ++i) {
				if (c[i] > mx1) mx2 = mx1, mx1 = c[i], mx2i = mx1i, mx1i = i;
				else if (c[i] > mx2) mx2 = c[i], mx2i = i;
			}
			count -= 2;
			c[mx1i]--, c[mx2i]--;
			bool flag = 0;
			for (int i = 0; i < n; ++i)
				if (c[i] > count / 2) flag = 1;
			if (!flag) {
				cout << " " << char('A' + mx1i) << char('A' + mx2i);
				continue;
			}
			c[mx1i]--, c[mx2i]++;
			flag = 0;
			for (int i = 0; i < n; ++i)
				if (c[i] > count / 2) flag = 1;
			if (!flag) {
				cout << " " << char('A' + mx1i) << char('A' + mx1i);
				continue;
			}
			c[mx1i]++, count++;
			flag = 0;
			for (int i = 0; i < n; ++i)
				if (c[i] > count / 2) flag = 1;
			if (!flag) {
				cout << " " << char('A' + mx1i);
				continue;
			}
		}
		if (T) cout << endl;
	}
}