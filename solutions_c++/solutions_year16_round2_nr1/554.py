#include <bits/stdc++.h>
using namespace std;

int cnt[128];
string nums[] =
  { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

pair<int, char> mp[10] = { { 0, 'Z' }, { 6, 'X' }, { 4, 'U' }, { 3, 'R' }, { 2, 'W' },
  { 1, 'O' }, { 5, 'F' }, { 7, 'S' }, { 8, 'G' }, { 9, 'N' } };

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);



	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		memset(cnt, 0, sizeof cnt);
		string s;
		cin >> s;
		for (char x : s)
			++cnt[x];
		string ans;
		for (auto p : mp) {
			while (cnt[p.second]) {
				ans += p.first + '0';
				for (char x : nums[p.first])
					--cnt[x];
			}
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << cs << ": " << ans << '\n';
	}

	return 0;
}
