#include <iostream>
#include <bitset>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
using namespace std;

bool isOk(string& s) {
	if (s == "") return true;
	string next = "";
	for (int i = 0; i+1 < s.size(); i += 2) {
		if (s[i] == s[i+1]) return false;
		if (s[i] == 'P') {
			if (s[i+1] == 'R') next += 'P';
			if (s[i+1] == 'S') next += 'S';
		}
		if (s[i] == 'R') {
			if (s[i+1] == 'P') next += 'P';
			if (s[i+1] == 'S') next += 'R';
		}
		if (s[i] == 'S') {
			if (s[i+1] == 'P') next += 'S';
			if (s[i+1] == 'R') next += 'R';
		}
	}
	return isOk(next);
}

void backtrack(int i, int n, int r, int p, int s, string path, string& sol) {
	if (sol != "IMPOSSIBLE") return;
	//if (!isOk(path)) return;
	if (i == n) {
		if (isOk(path)) sol = path;
		return;
	}
	if (p > 0 && r > 0) backtrack(i + 2, n, r-1, p-1, s, path + "PR", sol);
	if (p > 0 && s > 0) backtrack(i + 2, n, r, p-1, s-1, path + "PS", sol);
	if (r > 0 && p > 0) backtrack(i + 2, n, r-1, p-1, s, path + "RP", sol);
	if (r > 0 && s > 0) backtrack(i + 2, n, r-1, p, s-1, path + "RS", sol);
	if (s > 0 && p > 0) backtrack(i + 2, n, r, p-1, s-1, path + "SP", sol);
	if (s > 0 && r > 0) backtrack(i + 2, n, r-1, p, s-1, path + "SR", sol);
}

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		cout << "Case #" << cas << ": ";
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string sol = "IMPOSSIBLE";
		backtrack(0, (1 << n), r, p, s, "", sol);
		cout << sol << endl;
	}
}

