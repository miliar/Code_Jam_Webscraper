#include <bits/stdc++.h>

using namespace std;

#define INP "inp.txt"
#define OUT "out.txt"

int T, N, ia[1<<17+2];
string s, sa[1<<17+2];
std::vector<string> vs;
std::set<string> ss;

void pre() {
	ia[0] = 0;
	for(int i = 0; i < 1 << 17; i++) {
		if(i * 2 + 1 <= 1 << 17) ia[i * 2 + 1] = ia[i] + 1;
		if(i * 2 + 2 <= 1 << 17) ia[i * 2 + 2] = ia[i] + 1;
	}
}

string solve() {
	if(s.length() == 1) return s;
	string tmp = "";
	sa[0] = tmp + s[0];
	vs.clear();
	ss.clear();
	for(int i = 1; i <= (1 << s.length()) - 2; i++) {
		string root = sa[(i - 1) >> 1];
		if(i % 2) sa[i] = tmp + s[ia[i]] + root;
		else sa[i] = root + s[ia[i]];
		if(sa[i].length() == s.length()) vs.push_back(sa[i]), ss.insert(sa[i]);
	}
	cout << ss.size() << endl;;
	sort(vs.begin(), vs.end());
	//for(int i = 0; i < vs.size(); i++) cout << vs[i] << endl;
	return vs[(int)vs.size() - 1];
}

string solve2() {
	string tmp = "", ans = "";
	ans += s[0];
	for(int i = 1; i < s.length(); i++) {
		if(tmp + s[i] + ans > ans + s[i]) ans = tmp + s[i] + ans;
		else ans += s[i];
	}
	return ans;
}

int main () {
	freopen(INP, "r", stdin);
	freopen(OUT, "w", stdout);

	pre();
	scanf(" %d ", &T);
	for(int tt = 1; tt <= T; tt++) {
		cin >> s;
		//string s1 = solve();
		string s2 = solve2();
		//if(s1 != s2) cout << "wrong " << s1 << " " << s2 << endl;

		cout << "Case #" << tt << ": " << solve2() << endl;
	}
	return 0;
}