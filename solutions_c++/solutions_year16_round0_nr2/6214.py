#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for (int t = 0; t < T; ++t) {
		string S; cin >> S;
		cout << "Case #" << (t + 1) << ": ";
		/**/
		int n = S.length();
		int pointer = 0;
		int actions = 0;
		char symb = S[0];
		while (pointer < n) {
			if (S[pointer] != symb) {
				symb = S[pointer];
				actions += 1;
			}
			pointer += 1;
		}
		if (symb == '-') actions++;
		cout << actions;
		/**/
		cout << endl;
	}
}