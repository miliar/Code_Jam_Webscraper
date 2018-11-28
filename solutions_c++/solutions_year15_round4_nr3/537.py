#include <bits/stdc++.h>
using namespace std;
int T, N;
char s[20], str[50000];
int e[5005], f[5005], ne[5005], nf[5005];
vector<int> v[205];
map<string, int> m;
int main() {
	freopen("c.small.in", "r", stdin);
	freopen("c.small.out", "w", stdout);
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d\n", &N);
		int ans = 0, ma = INT_MAX;
		m.clear();
		for (int i = 0; i < N; ++i) {
			gets(str);
			v[i].clear();
			int cnt = 0;
			str[strlen(str)+1] = 0;
			while (sscanf(str+cnt, "%s", s) == 1) {
				auto it = m.find(string(s));
				if (it == m.end()) v[i].push_back(m[string(s)] = m.size());
				else v[i].push_back(it->second);
				cnt += strlen(s)+1;
			}
		}
		memset(e, 0, sizeof e);
		memset(f, 0, sizeof f);
		for (auto it:v[0]) e[it] = 1;
		for (auto it:v[1]) {
			if (e[it]) ++ans;
			f[it] = 1;
		}
		if (N == 2) {
			printf("Case #%d: %d\n", TC, ans);
			continue;
		}
		for (int bs = 0; bs < (1<<(N-2)); ++bs) {
			int cnt = 0;
			for (int k = 0; k < N-2; ++k) {
				if (bs & (1<<k)) { //e
					for (auto it:v[k+2]) {
						if (++e[it] == 1 && f[it] > 0) ++cnt;
					}
				}
				else { //f
					for (auto it:v[k+2]) {
						if (++f[it] == 1 && e[it] > 0) ++cnt;
					}
						
				}
			}
			for (int k = 0; k < N-2; ++k) {
				if (bs & (1<<k)) { //e
					for (auto it:v[k+2]) --e[it];
				}
				else { //f
					for (auto it:v[k+2]) --f[it];
				}
			}
			ma = min(ma, cnt);
		}
		printf("Case #%d: %d\n", TC, ans+ma);
	}
}
