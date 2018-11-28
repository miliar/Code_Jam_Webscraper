#include <iostream>
#include <string>
#include <cassert>
using namespace std;

void test()
{
	int n;
	cin >> n;
	string *s = new string [n];
	for (int i = 0; i < n; i++) {
		cin >> s[i];
	}
	assert(n >= 1);
	string p;
	for (int j = 0; j < s[0].size(); j++) {
		if (p.size() == 0 || s[0][j] != p[p.size() -1]) {
			p += s[0][j];
		}
	}
	int m = p.size();
	int *cnt = new int [m];
	for (int j = 0; j < m; j++) {
		cnt[j] = 0;
	}
	for (int i = 0; i < n; i++) {
		int k = 0;
		for (int j = 0; j < m; j++) {
			int c = 0;
			while (k < s[i].size() && s[i][k] == p[j]) {
				k++;
				c++;
			}
			if (c == 0) {
				cout << "Fegla Won";
				return;
			}
			cnt[j] += c;
		}
		if (k != s[i].size()) {
			cout << "Fegla Won";
			return;
		}
	}
	for (int j = 0; j < m; j++) {
		cnt[j] = (cnt[j] *2 + n) / (n *2);
	}
	int moves = 0;
	for (int i = 0; i < n; i++) {
		int k = 0;
		for (int j = 0; j < m; j++) {
			int c = 0;
			while (k < s[i].size() && s[i][k] == p[j]) {
				k++;
				c++;
			}
			moves += abs(cnt[j] - c);
		}
	}
	cout << moves;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i +1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}

