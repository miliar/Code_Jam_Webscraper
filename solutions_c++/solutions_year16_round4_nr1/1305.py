#include <bits/stdc++.h>
using namespace std;

int N;
int R, P, S;

vector<string> pm(15); // pm[i] := minimal final string of depth i rooted with 'P'
vector<string> rm(15);
vector<string> sm(15);

void init() {
	pm[0] = "P";
	rm[0] = "R";
	sm[0] = "S";
	for (int i = 0; i < 12; i++) {
		pm[i+1] = min(pm[i] + rm[i], rm[i] + pm[i]);
		rm[i+1] = min(rm[i] + sm[i], sm[i] + rm[i]);
		sm[i+1] = min(sm[i] + pm[i], pm[i] + sm[i]);
	}
}

bool valid(string s) {
	// verify counts
	int cnt[256];
	cnt['R'] = cnt['P'] = cnt['S'] = 0;
	for (int j = 0; j < (int)s.length(); j++) {
		cnt[(int)s[j]]++;
	}
	if (cnt['R'] != R) return false;
	if (cnt['P'] != P) return false;
	if (cnt['S'] != S) return false;
	return true;
}

int main() {
	init();
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N;
		cin >> R >> P >> S;
		string a = pm[N];
		string b = rm[N];
		string c = sm[N];
		
		a = valid(a) ? a : "Z";
		b = valid(b) ? b : "Z";
		c = valid(c) ? c : "Z";
		
		string res = min(a, min(b, c));
		if (res == "Z")
			res = "IMPOSSIBLE";
		
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
