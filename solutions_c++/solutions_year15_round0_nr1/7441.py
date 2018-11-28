#include <bits/stdc++.h>
using namespace std;

int invite_friends(string s) {
	int min_friends = 0;
	int xtra_person = s[0] - '0';
	int add_person;
	int audience;
	for (int i = 1; i < s.length(); ++i) {
		audience = s[i] - '0';
		if (audience != 0) {
			if (xtra_person >= i) {
				xtra_person += audience;
			} else {
				add_person = (i - xtra_person);
				min_friends += add_person;
				xtra_person += (add_person + audience);
			}
		}
	}
	return min_friends;
}
int main(int argc, char **argv) {
	ifstream fin(argv[1]);
	if (!fin) {
		cout << "could not open " << fin << endl;
		exit(0);
	}
	ofstream fout(argv[2]);
	if (!fout) {
		cout << "could not open " << fout << endl;
		exit(0);
	}
	int cases, n;
	fin >> cases;
	string s;
	for (int t = 1; t <= cases; ++t) {
		fin >> n;
		fin >> s;
		fout << "Case #" << t << ": " << invite_friends(s) << endl;
	}
	return 0;
}
