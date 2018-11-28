#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll t, n, ct;
bool vis[10];

void addin(ll x) {
	while (x != 0) {
		if (!vis[x%10])
			ct++;
		vis[x%10] = 1;

		x /= 10;
	}
}
int main() {
	ifstream cin("input.txt");
	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> n;
		cout << "Case #" << i+1 << ": ";

		memset(vis, 0, sizeof(vis));
		ct = 0;

		if (n == 0) {
			cout << "INSOMNIA" << endl; continue;
		}

		for (int j = 1; j <= 1000000000; ++j) {
			addin(n*j);
			if (ct == 10) {
				cout << n*j << endl;
				break;
			}
		}
	}
}