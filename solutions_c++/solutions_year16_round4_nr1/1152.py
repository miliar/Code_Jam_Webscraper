#include <bits/stdc++.h> 
using namespace std;

string arr[13];
string all[13][1 << 13];

char lose[128];
void build(int level, int ind) {
	if (!level) {
		all[level][ind] = arr[level][ind];
		return;
	}
	arr[level - 1][ind * 2] = arr[level][ind];
	arr[level - 1][ind * 2 + 1] = lose[arr[level][ind]];

	build(level - 1, ind * 2);
	build(level - 1, ind * 2 + 1);

	if (all[level - 1][ind * 2] > all[level - 1][ind * 2 + 1])
	  swap(all[level - 1][ind * 2], all[level - 1][ind * 2 + 1]);
	all[level][ind] = all[level - 1][ind * 2] + all[level - 1][ind * 2 + 1];
}

int n, r, p, s;
int cnt[128];
inline bool valid() {
	memset(cnt, 0, sizeof cnt);
	for (int i : all[n][0])
		++cnt[i];
	return (cnt['R'] == r && cnt['P'] == p && cnt['S'] == s);
}

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	lose['R'] = 'S';
	lose['S'] = 'P';
	lose['P'] = 'R';

	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> n >> r >> p >> s;
		arr[n].resize(1);
		for (int i = n - 1; i >= 0; --i)
			arr[i].resize(arr[i + 1].size() * 2);

		string ans;

		arr[n][0] = 'R';
		build(n, 0);

		if (valid() && (!ans.size() or all[n][0] < ans)) ans = all[n][0];

		arr[n][0] = 'S';
		build(n, 0);
		if (valid() && (!ans.size() or all[n][0] < ans)) ans = all[n][0];

		arr[n][0] = 'P';
		build(n, 0);
		if (valid() && (!ans.size() or all[n][0] < ans)) ans = all[n][0];

		cout << "Case #" << cs << ": ";

		if (ans.size())
			cout << ans;
		else
			cout << "IMPOSSIBLE";
		cout << '\n';

	}

}
