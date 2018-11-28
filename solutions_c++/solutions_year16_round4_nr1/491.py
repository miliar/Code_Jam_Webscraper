#include <bits/stdc++.h>
using namespace std;

int T;
int nR, nS, nP;
int N;
char s[3][2];

string gen(int lv, int wn) {
	if (lv == 0) {
		return (string(s[wn]));
	}
	string s1 = gen(lv - 1, wn);
	string s2 = gen(lv - 1, (wn + 1) % 3);
	if (s2 < s1)
		swap(s1, s2);
	return s1 + s2;
}

bool check(string s) {
	int cr = 0, cs = 0, cp = 0, len = s.size();
	for (int i = 0; i < len; ++i) {
		if (s[i] == 'P')
			cp ++;
		if (s[i] == 'R')
			cr ++;
		if (s[i] == 'S')
			cs ++;
	}
	return cr == nR && cs == nS && cp == nP;
}

int main() {
	scanf("%d", &T);
	s[0][0] = 'P';
	s[1][0] = 'R';
	s[2][0] = 'S';
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%d%d%d%d", &N, &nR, &nP, &nS);
		string sp = gen(N, 0);
		string sr = gen(N, 1);
		string ss = gen(N, 2);
		string ans = string("");
		string empty = string("");
		if (check(sp) && (ans == empty || sp < ans))
			ans = sp;
		if (check(sr) && (ans == empty || sr < ans))
			ans = sr;
		if (check(ss) && (ans == empty || ss < ans))
			ans = ss;
		if (ans == empty)
			ans = string("IMPOSSIBLE");
		printf("%s\n", ans.c_str());
	}
	return 0;
}