#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	freopen("A-large.in", "rt",stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	int id = 0;
	while (t--) {
		int sz;
		string str;
		cin >> sz >> str;
		int sm = 0, ans = 0;
		for (int i = 0; i <= sz; ++i) {
			if (i > sm) {
				ans += i - sm;
				sm = i;
			}
			sm += str[i] - '0';
		}
		cout << "Case #" << ++id << ": " << ans << '\n';
	}

	return 0;
}
