#include <bits/stdc++.h>
using namespace std;

int TC, N, R, P, S;

string rec1(int l, int obj) {
	if (l == 0) {
		if (obj == 0) return "P";
		else if (obj == 1) return "R";
		else return "S";
	}
	if (obj == 0) {
		string a = rec1(l - 1, 0);
		string b = rec1(l - 1, 1);
		if (a < b) return a + b;
		else return b + a;
	} else if (obj == 1) {
		string a = rec1(l - 1, 1);
		string b = rec1(l - 1, 2);
		if (a < b) return a + b;
		else return b + a;
	} else {
		string a = rec1(l - 1, 0);
		string b = rec1(l - 1, 2);
		if (a < b) return a + b;
		else return b + a;
	}
}

bool eval(string s, int r, int p, int s1) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'R') r--;
		else if (s[i] == 'P') p--;
		else if (s[i] == 'S') s1--;
	}
	if (r == 0 && p == 0 && s1 == 0) return 1;
	else return 0;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		string a = rec1(N, 0);
		string b = rec1(N, 1);
		string c = rec1(N, 2);
		string ans = "";
		if (eval(a, R, P, S)) {
			if (ans == "") ans = a;
			else if (a < ans) ans = a;
		}
		if (eval(b, R, P, S)) {
			if (ans == "") ans = b;
			else if (b < ans) ans = b;
		}
		if (eval(c, R, P, S)) {
			if (ans == "") ans = c;
			else if (c < ans) ans = c;
		}
		if (ans == "") printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %s\n", tc, ans.c_str());
	}
}
