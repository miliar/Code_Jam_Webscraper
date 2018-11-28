#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool check(vector<bool>& s) {
	for (int i = 0; i < s.size(); ++i) if (!s[i]) return false;
	return true;
}

void flip(vector<bool>& s, int m) {
	for (int i = 0; i <= m; ++i) {
		s[i] = !s[i];
	}
}

int lastToFlip(vector<bool>& s) {
	for (int i = s.size()-1; i >= 0; --i) {
		if (!s[i]) return i;
	}
}

int testcase() {
    string s;
    getline (cin,s);
	vector<bool> v(s.length());
	for (int i = 0; i < s.length(); ++i) v[i] = (s[i] == '-') ? false : true;
	int n = 0;
	while(!check(v)) {
		flip(v, lastToFlip(v));
		++n;
	}

	return n;
}

int main() {
	int t;
	cin >> t;
    string s;
    getline (cin,s);
	for (int i = 1; i <= t; ++i) {
		int n = testcase();
		cout << "Case #" << i << ": " << n << endl;
	}
}
