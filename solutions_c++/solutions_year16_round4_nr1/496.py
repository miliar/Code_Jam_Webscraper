#include <bits/stdc++.h>
using namespace std;

int N = 0;
char chr[111111];

bool solve(int dep, int P, int S, int R) {
	int ccnt[3] = {0};
	if (dep == N) {
		for (int who = 1<<dep, cnt = 0; cnt < (1<<dep); ++cnt, ++who) {
			if (chr[who] == 'P') ++ccnt[0];
			if (chr[who] == 'R') ++ccnt[1];
			if (chr[who] == 'S') ++ccnt[2];
		}
		return ccnt[0] == P && ccnt[1] == R && ccnt[2] == S;
	}
	for (int who = 1<<dep, cnt = 0; cnt < (1<<dep); ++cnt, ++who) {
		if (chr[who] == 'P') {
			chr[2*who] = 'P';
			chr[2*who+1] = 'R';
		}
		if (chr[who] == 'R') {
			
			chr[2*who] = 'R';
			chr[2*who+1] = 'S';
		}
		if (chr[who] == 'S') {
			chr[2*who] = 'P';
			chr[2*who+1] = 'S';
		}
	}
	return solve(dep+1, P, S, R);
}

string ans[1111111];

void print() {

	for (int who = 1<<N, cnt = 0; cnt < 1<<N; ++cnt, ++who) ans[who] = chr[who];

	for (int dep = N-1; dep >= 0; --dep) {
		for (int who = 1<<dep, cnt = 0; cnt < 1<<dep; cnt++, who++) {
			string a = ans[who*2];
			string b = ans[who*2+1];
			if (a > b) swap(a, b);
			ans[who] = a + b;
		}
	}
	cout << ans[1] << endl;
}

int main(void) {
	

	int cases; scanf("%d", &cases);

	int cas = 0;
	while (cases--) {
		printf("Case #%d: ", ++cas);

		scanf("%d", &N);
		int R, P, S; scanf("%d %d %d", &R, &P, &S);
		chr[1] = 'P';
		if (solve(0, P, S, R)) {
			print();
			continue;
		}
		chr[1] = 'R';
		if (solve(0, P, S, R)) {
			print();
			continue;
		}
		chr[1] = 'S';
		if (solve(0, P, S, R)) {
			print();
			continue;
		}

		puts("IMPOSSIBLE");
	}

	return 0;
}