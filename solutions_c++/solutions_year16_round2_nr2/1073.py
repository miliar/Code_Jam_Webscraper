#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

string s[2], o0, o1;
vector<pair<int, int> > questions;
int s0, s1, sol;

int valueOf(const string & str) {
	int val = 0;
	for (int i = 0; i < str.length(); i++)
		val = val * 10 + (str[i] - '0');
	return val;
}

void comb(int q) {
	if (q >= questions.size()) {
		int v0 = valueOf(s[0]);
		int v1 = valueOf(s[1]);
		int diff = abs(v0 - v1);
		if ((diff < sol) || (diff == sol && v0 < s0) || (diff == sol && v0 == s0 && v1 < s1)) {
			s0 = v0;
			s1 = v1;
			sol = diff;
			o0 = s[0];
			o1 = s[1];
		}
		return;
	}

	int i = questions[q].first;
	int j = questions[q].second;
	for (char d = '0'; d <= '9'; d++) {
		s[i][j] = d;
		comb(q + 1);
	}

}

int main() {
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		cin >> s[0] >> s[1];

		questions.clear();
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < s[i].length(); j++)
				if (s[i][j] == '?')
					questions.push_back(make_pair<int, int>(i, j));

		sol = INT_MAX;
		comb(0);
		cout << "Case #" << caseCounter << ": " << o0 << " " << o1 << endl;

	}
	return 0;
}
