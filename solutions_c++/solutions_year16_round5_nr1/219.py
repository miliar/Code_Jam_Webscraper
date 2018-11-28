#include <bits/stdc++.h>
using namespace std;

string s;
int mem[55][55];
int vis[55][55];
int vis_id;
int merge(char c, char d) {
	if (c == d)
		return 10;
	return 5;
}

int solve(int L, int R) {
	if (R < L)
		return 0;
	if ((R - L + 1) % 2 == 1)
		return 0;
	if (vis[L][R] == vis_id)
		return mem[L][R];
	vis[L][R] = vis_id;
	int ans = 0;
	if (s[L] == s[R]) {
		ans = 10 + solve(L + 1, R - 1);
		return mem[L][R] = ans;
	}
	if (s[L] == s[L + 1]) {
		ans = 10 + solve(L + 2, R);
		return mem[L][R] = ans;
	}
	for (int x = L + 1; x <= R; x += 2)
		ans = max(ans, solve(L + 1, x - 1) + merge(s[L], s[x]) + solve(x + 1, R));
	return mem[L][R] = ans;
}


int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/Round 3/A/A-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/Round 3/A/A-large.out", "w", stdout);

	int t; cin >> t;
	int id = 1;
	while (t--) {
		cin >> s;
		stack<char> S;
		int ans = 0;
		// 1 0 1 0 1 0 1 0 1 0 1 0 1
		for (int i = 0; i < int(s.size()); i++) {
			if (S.empty())
				S.push(s[i]);
			else {
				if (S.top() == s[i]) {
					S.pop();
					ans += 10;
				}
				else
					S.push(s[i]);
			}
		}
		ans += 5 * S.size() / 2;
		cout << "Case #" << id++ << ": " << ans << endl;
	}


	return 0;
}
