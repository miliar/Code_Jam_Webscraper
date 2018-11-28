#include <bits/stdc++.h>
using namespace std;

int N, K;
string S;
int nc;

void flip(int x) {
	for (int i = x; i <= x + K - 1; ++i) S[i] = (S[i] == '+' ? '-' : '+');
}

void solve() {
	cin >> S >> K; N = (int)S.size();
	int ans = 0;
	for (int i = 0; i < N - K + 1; ++i) {
		if (S[i] == '-') flip(i), ++ans;
	}
	for (int i = 0; i < N; ++i) if (S[i] == '-') { printf("Case #%d: IMPOSSIBLE\n", ++nc); return; }
	printf("Case #%d: %d\n", ++nc, ans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	while(T--)
		solve();
}
