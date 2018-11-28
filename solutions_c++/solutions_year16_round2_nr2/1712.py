#include <iostream>
#include <sstream>
#include <string>
#include <climits>

using namespace std;

uint64_t string2Uint(string s) {
	stringstream ss;
	ss << s;
	uint64_t n;
	ss >> n;
	return n;
}

uint64_t getDiff(uint64_t left, uint64_t right) {
	if (left < right)
		return getDiff(right, left);
	return left - right;
}

struct score {
	string C;
	string J;
	uint64_t diff;
	score(string _C, string _J, uint64_t _diff)
		: C(_C), J(_J), diff(_diff) {}
};

void dfs(string &s, score &currMin, int idx, int l) {
	if (idx == s.length()) {
		string strC = s.substr(0, l),
			strJ = s.substr(l);
		uint64_t C = string2Uint(strC),
		J = string2Uint(strJ);
		uint64_t diff = getDiff(C, J);
		if (diff < currMin.diff)
			currMin = score(strC, strJ, diff);
		return;
	}
	if (s[idx] != '?') {
		dfs(s, currMin, idx + 1, l);
		return;
	}
	for (char c = '0'; c <= '9'; c++) {
		s[idx] = c;
		dfs(s, currMin, idx + 1, l);
		s[idx] = '?';
	}
}

score closeScore(string C, string J) {
	score result("0", "0", ULLONG_MAX);
	string s = C + J;
	dfs(s, result, 0, C.length());
	return result;
}

int main() {
	//score result = closeScore("?5", "?0");
	//cout << result.C << " " << result.J << endl;
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string C, J;
		cin >> C >> J;
		score result = closeScore(C, J);
		cout << "Case #" << t <<": " << result.C << " " << result.J << endl;
	}
}