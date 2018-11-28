#include <iostream>
#include <vector>

using namespace std;

int calculate(string s, int n) {
	int l1,  res, c;
	int i, j;
	bool f;
	vector<int> match;

	static string vowels = "aeiou";
	static int l2 = vowels.length();

	l1 = s.length();
	c = 0;
	for  (i = 0; i < l1; ++i) {
		f = true;
		for (j = 0; j < l2; ++j) {
			if (vowels[j] == s[i]) {
				f = false;
				break;
			}
		}
		if (f) {
			c++;
		} else {
			c = 0;
		}
		if (c >= n) {
			match.push_back(i);
		}

	}

	c = 0;
	res = 0;
	for (i = 0; i < match.size(); ++i) {
		j = match[i];
		// cout << j << endl;
		// 
		res += (j + 2 - n - c) * (l1 - j);
		// cout << (j + 2 - n - c) << endl << endl;
		// cout << match[i] << endl;
		c = j - n + 2;
	}
	return res;
}

int main() {
	int T;
	int i;

	int n;
	string s;

	cin >> T;

	for (i = 1;  i <= T; ++i) {
		cin >> s >> n;
		cout << "Case #" << i << ": " << calculate(s, n) << endl;
	}
}
