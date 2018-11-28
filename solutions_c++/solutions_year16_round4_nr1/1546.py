#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int N, R, P, S;

inline char rps(char l, char r) {
	string cmp = string(1, (char)min(l, r));
	cmp += (char)max(l, r);
	if (cmp == "PR") {
		return 'P';
	}
	if (cmp == "PS") {
		return 'S';
	}
	return 'R';
}

bool play(const string& s) {
	string cur, prev(s);
	while (prev.length() != 1) {
		cur = "";
		for (int i = 0; i < prev.length(); i += 2) {
			if (prev[i] == prev[i+1])
				return false;
			cur += rps(prev[i], prev[i+1]);
		}
		swap(cur, prev);
	}
	return true;
}

string solve() {
	stringstream ss;
	for (int i = 0; i < P; ++i) {
		ss << 'P';
	}
	for (int i = 0; i < R; ++i) {
		ss << 'R';
	}
	for (int i = 0; i < S; ++i) {
		ss << 'S';
	}

	bool success = false;
	string buf = ss.str();
	string sol;
	do {
		if (play(buf)) {
			if (!success) {
				sol = string(buf);
			} else if (buf < sol) {
				sol = string(buf);
			}
			success = true;
		}

	} while (next_permutation(buf.begin(), buf.end()));

	if (success) {
		return sol;
	}
	return "IMPOSSIBLE";
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}
