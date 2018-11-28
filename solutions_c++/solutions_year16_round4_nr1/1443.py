#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t;

	cin >> t;
	for (int c = 1; c <= t; c++) {
		int n, r, p, s;

		cin >> n >> r >> p >> s;

		int num[3] = {r, s, p}, x = n / 2 % 3, start = 3;

		cout << "Case #" << c << ": ";

		if (n & 1)	// 2イコール1下
			if (num[0] == num[1] && num[2] == num[0] - 1 || num[1] == num[2] && num[0] == num[1] - 1 || num[2] == num[0] && num[1] == num[2] - 1)
				if (num[(x + 2) % 3] == num[x] - 1)			// グー始まり
					start = 0;
				else if (num[x] == num[(x + 1) % 3] - 1)	// チョキ始まり
					start = 1;
				else										// パー始まり
					start = 2;
			else
				cout << "IMPOSSIBLE" << endl;
		else		// 2イコール1上
			if (num[0] == num[1] && num[2] == num[0] + 1 || num[1] == num[2] && num[0] == num[1] + 1 || num[2] == num[0] && num[1] == num[2] + 1) {
				if (num[x] == num[(x + 1) % 3] + 1)
					start = 0;
				else if (num[(x + 1) % 3] == num[(x + 2) % 3] + 1)
					start = 1;
				else
					start = 2;
			} else
				cout << "IMPOSSIBLE" << endl;

		if (start != 3) {
			vector<char> v;

			v.push_back(start == 0 ? 'R' : start == 1 ? 'S' : 'P');
			for (int i = 0; i < n; i++) {
				vector<char> vt;
				for (int i = 0; i < v.size(); i++)
					if (v[i] == 'R') {
						vt.push_back('R');
						vt.push_back('S');
					} else if (v[i] == 'S') {
						vt.push_back('S');
						vt.push_back('P');
					} else {
						vt.push_back('P');
						vt.push_back('R');
					}
				v = vt;
			}

			int len = 1;
			for (int i = 0; i < n; i++) {
				vector<char> vt;
				for (int j = 0; j < v.size(); j += len * 2) {
					stringstream ss1, ss2;
					for (int k = j; k < j + len; k++)
						ss1 << v[k];
					for (int k = j + len; k < j + len * 2; k++)
						ss2 << v[k];
					string s1 = ss1.str(), s2 = ss2.str();
					if (s1 < s2) {
						for (int k = 0; k < len; k++)
							vt.push_back(s1[k]);
						for (int k = 0; k < len; k++)
							vt.push_back(s2[k]);
					} else {
						for (int k = 0; k < len; k++)
							vt.push_back(s2[k]);
						for (int k = 0; k < len; k++)
							vt.push_back(s1[k]);
					}
				}
				len <<= 1;
				v = vt;
			}

			for (auto& elem : v)
				cout << elem;
			cout << endl;
		}
	}

	return 0;
}
