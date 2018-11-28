#include <bits/stdc++.h>

using namespace std;

string solve(int p, int r, int s) {
	if(p < 0 || r < 0 || s < 0) return "";
	if(p + r + s == 1) {
		if(p) return "P";
		if(r) return "R";
		if(s) return "S";
	}
	if(p + r + s == 2) {
		if(p == 2 || r == 2 || s == 2) return "";
		if(!p) return "RS";
		if(!r) return "PS";
		if(!s) return "PR";
	}

	int S = (p+r+s)/4;
	string R = solve(p-S, r-S, s-S);
	if(R == "") return "";
	string E;
	for(auto c: R) {
		if(c == 'P') E += "PRPS";
		if(c == 'R') E += "PRRS";
		if(c == 'S') E += "PSRS";
	}
	return E;
}

int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string S = solve(p, r, s);
		if(S == "") S = "IMPOSSIBLE";
		cout << "Case #" << i << ": " << S << endl;
	}
}
