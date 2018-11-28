#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

char rep[] = {'R', 'P', 'S'};
string memo[22][3];
string solve(int i, int cur) {
	if (memo[i][cur] != "") {
		return memo[i][cur];
	}
	if (i == 0) return string(1, rep[cur]);
	string r1 = solve(i - 1, cur);
	string r2 = solve(i - 1, (cur + 2) % 3);
	if (r1 > r2) swap(r1, r2);
	return memo[i][cur] = r1 + r2;
}

int n, res[3], c[3], nc[3];
vector<string> ans;
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n >> res[0] >> res[1] >> res[2];
		ans.clear();
		For(i,0,2) {
			memset(c, 0, sizeof c);
			c[i] = 1;
			For(j,1,n) {
				memset(nc, 0, sizeof nc);
				For(x,0,2) {
					nc[x] += c[x];
					nc[(x + 2) % 3] += c[x];
				}
				memcpy(c, nc, sizeof c);
			}
			if (c[0] == res[0] && c[1] == res[1] && c[2] == res[2]) {
				ans.push_back(solve(n, i));
			}
		}
		sort(ans.begin(), ans.end());
		if (ans.empty()) {
			puts("IMPOSSIBLE");
		} else {
			puts(ans.begin()->c_str());
		}
	}
	return 0;
}
