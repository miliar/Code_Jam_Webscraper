#include <bits/stdc++.h>
using namespace std;
string ans[13][3];

int tr(char c) {
	if(c == 'P') return 0;
	if(c == 'R') return 1;
	if(c == 'S') return 2;
}

void init() {
	//p = 0, r = 1, s = 2
	ans[1][0] = "RS";
	ans[1][1] = "PS";
	ans[1][2] = "PR";

	for(int i = 2; i <= 12; i++) {
		int cnt[3][3];
		memset(cnt, 0, sizeof(cnt));
		for(int j = 0; j < 3; j++)
			for(int z = 0; z < ans[i - 1][j].size(); z++) cnt[j][tr(ans[i - 1][j][z])]++;
		for(int j = 0; j < 3; j++) {
			for(int k = 0; k < 3; k++) {
				int s[3], y[3];
				for(int z = 0; z < 3; z++) {
					s[z] = cnt[j][z] + cnt[k][z];
					y[z] = s[z];
				}
				sort(y, y + 3);
				if(y[2] - y[0] != 1 || s[0] + s[1] + s[2] != (1 << i)) continue;
				int g;
				if(s[0] == s[1]) g = 2;
				if(s[1] == s[2]) g = 0;
				if(s[0] == s[2]) g = 1;
				if(ans[i][g] == "") {
					ans[i][g] = ans[i - 1][j] + ans[i - 1][k];
				} else {
					ans[i][g] = min(ans[i][g], ans[i - 1][j] + ans[i - 1][k]);
				}
			}
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.ou", "w", stdout);
	init();
	int T, cases = 0;
	int n, p, r, s;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d%d%d", &n, &r, &p, &s);
		int t[3] = {p, r, s};
		printf("Case #%d: ", ++cases);
		sort(t, t + 3);
		if(t[2] - t[0] == 1) {
			int g;
			if(p == r) g = 2;
			if(p == s) g = 1;
			if(r == s) g = 0;
			printf("%s\n", ans[n][g].c_str());
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
