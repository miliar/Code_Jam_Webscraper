#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())

int __lcm(int a, int b) {
	return (a / __gcd(a, b)) * b;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
	  freopen("B-small-attempt0.in", "rt", stdin);
	  freopen("out.txt", "wt", stdout);

	int t;
	cin >> t;
	int m[5];
	int id = 0;
	while (t--) {
		int b, n;
		cin >> b >> n;
		int lcm = 1;
		for (int i = 0; i < b; ++i) {
			cin >> m[i];
			lcm = __lcm(lcm, m[i]);
		}
		int mod = 0;
		priority_queue<pair<int,int>> q;
		for (int i = 0; i < b; ++i) {
			mod += lcm / m[i];
			q.push({0, -i});
		}
		int ans = 0;
		for (int i = 0; i < mod; ++i) {
			pair<int,int> p = q.top();
			q.pop();
			if ((n - 1) % mod == i) {
				ans = -p.second + 1;
			}
			p.first -= m[-p.second];
			q.push(p);
		}
		cout << "Case #" << ++id << ": " << ans << '\n';
	}

	return 0;
}
