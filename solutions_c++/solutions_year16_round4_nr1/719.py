#include<cstdio>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<sstream>
#include<cmath>
#include<cctype>
#include<cassert>
#include<cstring>
#include<cstdlib>

using namespace std;

const int debug = 0;
const int inf = 1000000000;

int N, R, P, S;

string winner(char c) {
	string s = "";
	s += c;

	for (int i = 0; i < N; i++) {
		string ss = "";
		for (int j = 0; j < s.size(); j++) {
			if (s[j] == 'P') ss += "PR";
			else if (s[j] == 'R') ss += "RS";
			else if (s[j] == 'S') ss += "PS";
		}
		s = ss;
	}

	int r, p, sc;
	r = p = sc = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == 'P') p++;
		if (s[i] == 'R') r++;
		if (s[i] == 'S') sc++;
	}
	if (p == P && r == R && sc == S) {
		for (int L = 1; L < s.size() ; L *= 2) {
			string res = "";
			for (int i = 0; i < s.size(); i += L * 2) {
				string s1 = s.substr(i, L);
				string s2 = s.substr(i + L, L);
				if (s1 > s2) swap(s1, s2);
				res += s1; res += s2;
			}
			s = res;
		}
		return s;
	} else return "";
}

int main() {
	int test, cases = 1;
	cin >> test;
	for (cases = 1; cases <= test; cases++) {
		cin >> N >> R >> P >> S;

		string s1 = winner('P');
		string s2 = winner('R');
		string s3 = winner('S');

		string res = "";
		if (s1 != "") {
			if (res == "") res = s1;
		}

		if (s2 != "") {
			if (res == "" || res > s2) res = s2;
		}

		if (s3 != "") {
			if (res == "" || res > s3) res = s3;
		}

		if (res == "") printf("Case #%d: %s\n", cases, "IMPOSSIBLE");
		else printf("Case #%d: %s\n", cases, res.c_str());
	}
	return 0;
}
