#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	ifstream fin("input.in");
	ofstream fout("output.out");
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	int T;
	fin >> T;
	string s, ans;
	for (int t = 1; t <= T; t++) {
		ans = "";
		fout << "Case #" << t << ": ";
		fin >> s;
		ans += s[0];
		for (int i = 1; i < s.length(); i++) {
			if (s[i] < ans[0]) ans += s[i];
			else ans = s[i] + ans;
		}
		fout << ans << endl;
	}
}