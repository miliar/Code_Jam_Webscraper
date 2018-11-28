#include<bits/stdc++.h>

using namespace std;

char ans[(1 << 12) + 1];

bool solve(int r, int p, int s, char R, char P, char S) {
	if (r + p + s == 1) {
		if (r) ans[0] = 'R';
		if (p) ans[0] = 'P';
		if (s) ans[0] = 'S';
		
		return true;
	}
	
	if ((r + p - s) % 2 == 1) {
		strcpy(ans, "IMPOSSIBLE");
		
		return false;
	}
	
	int pr = (r + p - s) / 2;
	int ps = p - pr;
	int rs = s + pr - p;
	
	char RR, PP, SS;
	
	if (R < P && R < S) {
		if (P < S) {
			PP = '0';
			RR = '1';
			SS = '2';
		}
		else {
			RR = '0';
			PP = '1';
			SS = '2';
		}
	}
	else if (P < S) {
		if (R < S) {
			PP = '0';
			SS = '1';
			RR = '2';
		}
		else {
			SS = '0';
			PP = '1';
			RR = '2';
		}
	}
	else {
		if (P < R) {
			SS = '0';
			RR = '1';
			PP = '2';
		}
		else {
			RR = '0';
			SS = '1';
			PP = '2';
		}
	}
	
	if (pr < 0 || ps < 0 || rs < 0 || solve(rs, pr, ps, RR, PP, SS) == false) {
		strcpy(ans, "IMPOSSIBLE");
		
		return false;
	}
	
	ans[r + p + s] = 0;
	for (int i = (r + p + s) / 2 - 1; i >= 0; i--) {
		if (ans[i] == 'P') {
			ans[2 * i    ] = (P < R ? 'P' : 'R');
			ans[2 * i + 1] = (P < R ? 'R' : 'P');
		}
		else if (ans[i] == 'R') {
			ans[2 * i    ] = (R < S ? 'R' : 'S');
			ans[2 * i + 1] = (R < S ? 'S' : 'R');
		}
		else {
			ans[2 * i    ] = (P < S ? 'P' : 'S');
			ans[2 * i + 1] = (P < S ? 'S' : 'P');
		}
	}
	
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, r, p, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		
		solve(r, p, s, 'R', 'P', 'S');
		
		printf("Case #%d: %s\n", t, ans);
	}
	
	return 0;
}
