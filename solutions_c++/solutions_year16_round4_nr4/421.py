#include <bits/stdc++.h>

using namespace std;

#define get(mask, x, y) ((mask) & (1 << (((x) * N) + (y))))

int N;
int H[5][5];
int K[5][5];

bool check(vector<int> & perm, int n, vector<bool> & fr) {
	if(n == N) return true;
	bool ans = false;
	for(int u = 0; u < N; ++u)
		if(fr[u] && K[perm[n]][u]) ans = true;
	if(!ans) return false;
	for(int u = 0; u < N && ans; ++u) {
		if(fr[u] && K[perm[n]][u]) {
			fr[u] = false;
			ans = check(perm, n + 1, fr);
			fr[u] = true;
		}
	}
	return ans;
};

void solve(int t) {
	cin >> N;
	for(int n = 0; n < N; ++n) {
		string s;
		cin >> s;
		for(int m = 0; m < N; ++m)
			H[n][m] = int(s[m] == '1');
	}
	int ans = 1 << 20;
	for(unsigned m = 0; m < (1 << (N * N)); ++m) {
		bool ok = true;
		int cost = 0;
		for(int x = 0; x < N; ++x)
			for(int y = 0; y < N; ++y) {
				K[x][y] = get(m, x, y) != 0;
				cost += K[x][y] - H[x][y];
				if(!K[x][y] && H[x][y])
					ok = false;
			}
		if(!ok) continue;
		if(cost >= ans) continue;
		vector<int> perm(N);
		iota(perm.begin(), perm.end(), 0);
		ok = true;
		do {
			vector<bool> fr(N, true);
			if(!check(perm, 0, fr))
				ok = false;
				
		} while(ok && next_permutation(perm.begin(), perm.end()));
		if(ok)
			ans = cost;
	}
	printf("Case #%d: %d\n", t, ans);
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
		solve(t);
}
