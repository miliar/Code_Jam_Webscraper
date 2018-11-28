#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

const double EPS = 1e-9;
const ll INF = 1e17;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);

	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

	int t;
	cin >> t;

	for (int testNum = 0; testNum < t; testNum++) {
		string s;
		cin >> s;

		while (!s.empty() && s.back() == '+') s.pop_back();

		int ans = unique(all(s)) - s.begin();

		cout << "Case #" << testNum + 1 << ": " << ans << "\n";
	}

	return 0;
}
