#include <bits/stdc++.h>
using namespace std;

const string w[] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

map<char, int> z[10];

void sub(int k, map<char, int>& cnt, vector<int>& ans) {
	for (auto it : z[k]) {
		assert(cnt[it.first] >= it.second);
		cnt[it.first] -= it.second;
	}
	ans.push_back(k);
}

void solve() {
	string s; cin >> s;

	map<char, int> cnt;
	for (char c : s) {
		cnt[c]++;
	}

	vector<int> ans;
	while (cnt['Z']) {
		sub(0, cnt, ans);
	}
	while (cnt['X']) {
		sub(6, cnt, ans);
	}
	while (cnt['S']) {
		sub(7, cnt, ans);
	}
	while (cnt['G']) {
		sub(8, cnt, ans);
	}
	while (cnt['H']) {
		sub(3, cnt, ans);
	}
	while (cnt['W']) {
		sub(2, cnt, ans);
	}
	while (cnt['U']) {
		sub(4, cnt, ans);
	}
	while (cnt['F']) {
		sub(5, cnt, ans);
	}
	while (cnt['O']) {
		sub(1, cnt, ans);
	}
	while (cnt['I']) {
		sub(9, cnt, ans);
	}
	sort(ans.begin(), ans.end());

	for (int x : ans) {
		cout << x;
	}
	cout << endl;
}

int main() {
	for (int i = 0; i < 10; i++) {
		for (char c : w[i]) {
			z[i][c]++;
		}
	}

	ios::sync_with_stdio(false);

	int n; cin >> n;
	for (int k = 1; k <= n; k++) {
		cout << "Case #" << k << ": ";
		solve();
	}

	return 0;
}

