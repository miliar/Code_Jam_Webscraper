#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string compress(string s) {
	stringstream ss;
	char last = 'e';
	for (int i = 0; i < s.size(); i++) {
		if (s[i] != last) {
			last = s[i];
			ss << s[i];
		}
	}
	return ss.str();
}
map<string, int> m;
map<string, bool> seen;


int dp(string s){
	if (s == "-") return 1;
	if (s == "+") return 0;
	if (m.find(s) != m.end()) return m[s];

	seen[s] = true;
	int bestScore = 1000;

	for (int i = 1; i <= s.size(); i ++) {
		string t = s;
		reverse(t.begin(), t.begin() + i);
		for (int j = 0; j < i; j ++){
			if (t[j] == '+') t[j] = '-';
			else t[j] = '+';
		}

		string tCompressed = compress(t);
		if(!seen[t]){
			int score = dp(tCompressed) + 1;
			bestScore = min(bestScore, score);
		}
	}

	m[s] = bestScore;
	return bestScore;
}
int main() {
	int n;
	cin >> n;

	for (int tc = 0; tc < n; tc ++){
		string cur;
		cin >> cur;
		cur = compress(cur);
		int ans = dp(cur);
		cout << "Case #" << tc+1 << ": " << ans << endl;
	}
	return 0;
}
