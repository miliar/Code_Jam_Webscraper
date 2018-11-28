#include <stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
using namespace std;

int MAXN = (2 << 12) + 10;

string s[13][130];
char beat[130];
string v = "SPR";
int cnt[130];

string gao(int N, char c) {
	if (s[N][c].size() > 0) return s[N][c];
	if (N == 0) {
		return s[0][c] = c;
	} else {
		string a = gao(N - 1, c);
		string b = gao(N - 1, beat[c]);
		if (a < b) {
			return s[N][c] = a + b;
		} else {
			return s[N][c] = b + a;
		}
	}
}

int check(int N, char c, int cnt[]) {
	int val[130] = {0};
	string& S = s[N][c];
	//puts(S.c_str());
	for (int i = 0; i < S.size(); i++) {
		val[S[i]]++;
	}
	for (int i = 0; i < v.size(); i++) {
		//printf("%d %d\n", val[v[i]], cnt[v[i]]);
		if (val[v[i]] != cnt[v[i]]) return 0;
	}
	return 1;
}

int main() {
	int cas;
	beat['R'] = 'S';
	beat['S'] = 'P';
	beat['P'] = 'R';
	gao(12, 'S');
	gao(12, 'P');
	gao(12, 'R');

	/*
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++)
			puts(s[i][v[j]].c_str());
	}
	*/

	scanf("%d", &cas);
	for (int re = 1; re <= cas; re++) {
		memset(cnt, 0, sizeof(cnt));
		int N;
		scanf("%d%d%d%d", &N, &cnt['R'], &cnt['P'], &cnt['S']);
		string ans = "Z";
		for (int i = 0; i < v.size(); i++) {
			if (check(N, v[i], cnt)) {
				if (s[N][v[i]] < ans)
					ans = s[N][v[i]];
			}
		}
		if (ans == "Z") {
			ans = "IMPOSSIBLE";
		}
		printf("Case #%d: %s\n", re, ans.c_str());
	}
}