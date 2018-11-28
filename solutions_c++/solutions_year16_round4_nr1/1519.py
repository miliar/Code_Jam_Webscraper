#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <cassert>

using namespace std;

string winner(string s) {
	while (s.length() > 1) {
		string s2;
		for (int i = 0; i < s.length(); i += 2) {
			string t = s.substr(i, 2);
			if (t == "RP" || t == "PR") s2 += "P";
			else if (t == "SP" || t == "PS") s2 += "S";
			else if (t == "RS" || t == "SR") s2 += "R";
			else return "";
		}
		s = s2;
	}
	return s;
}

string solve(int R, int P, int S) {
	if (R + P + S == 2) {
		string w = winner(string(P, 'P') + string(R, 'R') + string(S, 'S'));
		if (w == "") return "";
		return string(P, 'P') + string(R, 'R') + string(S, 'S');
	}
	if (R + P < S || P + S < R || S + R < P) 
		return "";
	for (int p = P; p >= 0; --p) {
		for (int r = R; r >= 0; --r) {
			int s = (R + P + S) / 2 - p - r;
			if (s > S || s < 0) continue;
			string s1 = solve(r, p, s);
			string s2 = solve(R - r, P - p, S - s);
			if (s1 != "" && s2 != "" && winner(s1) != winner(s2)) {
				return s1 + s2;
			}
		}
	}
	return "";
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		string ret = solve(R, P, S);
		if (ret == "") ret = "IMPOSSIBLE";
		cout << "Case #" << t << ": " << ret << endl;
	}
	return 0;
}