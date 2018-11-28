#include <bits/stdc++.h>
using namespace std;

bool valid;
string get(int r, int p, int s) {
	int n = r + p + s;

	if (n == 0)
		return "";

	if (n == 1) {
		if (r == 1)
			return "R";
		if (p == 1)
			return "P";
		if (s == 1)
			return "S";
		assert(0);
	}

	if (n == 2) {
		if (max(r, max(s, p)) == n)
			return "IMPOSSIBLE";
		if (s == 0)
			return "PR";
		if (p == 0)
			return "RS";
		if (r == 0)
			return "PS";
		assert(0);
	}
	assert(n % 4 == 0);
	int blocks = n / 4;
	if (min(r, min(p, s)) < blocks) {
		valid = false;
		return "IMPOSSIBLE";
	}

	r -= blocks;
	p -= blocks;
	s -= blocks;

	string ans = get(r, p, s);
	if (ans == "IMPOSSIBLE")
		return "IMPOSSIBLE";
	string ret = "";
	for (int i = 0; i < int(ans.size()); i++)
		if (ans[i] == 'R')
			ret += "PRRS";
		else if (ans[i] == 'P')
			ret += "PRPS";
		else
			ret += "PSRS";
	return ret;
}


int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/Round 2/A/A-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/Round 2/A/A-large.out", "w", stdout);

	int id = 1;
	int t; cin >> t;
	while (t--) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << id++ << ": " << get(r, p, s) << endl;
	}


	return 0;
}
