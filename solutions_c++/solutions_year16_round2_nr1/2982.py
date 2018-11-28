#include <bits/stdc++.h>
#include <iostream>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	REP(o, t) {
		string str;
		map<char, int> letters;
		cin >> str;
		for (auto it: str) {
			letters[it] += 1;
		}
		// for (auto it : letters) {
		// 	cout << it.first << " " << it.second << endl;
		// }
		vector<int> res(10);
		vector<string> names = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
		vector<pair<char, int>> combination = { make_pair('Z', 0), make_pair('G', 8), make_pair('H', 3), make_pair('T', 2), make_pair('X', 6), make_pair('R', 4), make_pair('F', 5), make_pair('O', 1), make_pair('S', 7), make_pair('I', 9) };
		// for (int i = 0, i < combination.size(); ++i) {
		for (auto it: combination) {
			res[it.second] += letters[it.first];
			for (auto l: names[it.second]) {
				letters[l] -= res[it.second];
			}
		}
		cout << "Case #" << o + 1 << ": ";
		REP(i, 10) {
			REP(x, res[i]) {
				cout << i;
			}
		}
		cout << "\n";
		for (int i = 'A'; i <= 'Z'; ++i) {
			if (letters[i] != 0) {
				cout << (char)(i) << ": " << letters[i] << endl;
			}
		}
	}
	return 0;
}
#endif