#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		string str;
		cin >> str;
		vector<int> hist(26, 0);
		for (char c : str) {
			++hist[c-'A'];
		}
		vector<int> result(10, 0);
		while (hist['Z'-'A'] > 0) {
			++result[0];
			for (char c : "ZERO") {
				--hist[c-'A'];
			}
		}
		while (hist['W'-'A'] > 0) {
			++result[2];
			for (char c : "TWO") {
				--hist[c-'A'];
			}
		}
		while (hist['U'-'A'] > 0) {
			++result[4];
			for (char c : "FOUR") {
				--hist[c-'A'];
			}
		}
		while (hist['R'-'A'] > 0) {
			++result[3];
			for (char c : "THREE") {
				--hist[c-'A'];
			}
		}
		while (hist['O'-'A'] > 0) {
			++result[1];
			for (char c : "ONE") {
				--hist[c-'A'];
			}
		}
		while (hist['F'-'A'] > 0) {
			++result[5];
			for (char c : "FIVE") {
				--hist[c-'A'];
			}
		}
		while (hist['X'-'A'] > 0) {
			++result[6];
			for (char c : "SIX") {
				--hist[c-'A'];
			}
		}
		while (hist['S'-'A'] > 0) {
			++result[7];
			for (char c : "SEVEN") {
				--hist[c-'A'];
			}
		}
		while (hist['G'-'A'] > 0) {
			++result[8];
			for (char c : "EIGHT") {
				--hist[c-'A'];
			}
		}
		while (hist['I'-'A'] > 0) {
			++result[9];
			for (char c : "NINE") {
				--hist[c-'A'];
			}
		}
		cout << "Case #" << (t+1) << ": ";
		for (int i = 0; i < result.size(); ++i) {
			for (int j = 0; j < result[i]; ++j) {
				cout << i;
			}
		}
		cout << endl;
	}
}