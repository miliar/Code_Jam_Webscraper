#include <bits/stdc++.h>
using namespace std;

string G[105];
string B;


int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/Round 3/D/D-small-attempt4.in", "r", stdin);
	freopen("/home/ahmed/Desktop/Round 3/D/D-small-attempt4.out", "w", stdout);

	int t; cin >> t;
	int id = 1;
	while (t--) {
		int n, L; cin >> n >> L;
		for (int i = 0; i < n; i++)
			cin >> G[i];
		sort(G, G + n);
		cin >> B;

		if (G[n - 1] == B) {
			cout << "Case #" << id++ << ": IMPOSSIBLE" << endl;
			continue;
		}

		if (L == 1) {
			cout << "Case #" << id++ << ": 0 ?" << endl;
			continue;
		}

		string ans = "";
		for (int i = 0; i < L - 1; i++)
			if (i % 2 == 0)
				ans += "1";
			else
				ans += "0";
		ans += "0?";
		for (int i = 0; i < L - 1; i++)
			if (i % 2 == 0)
				ans += "1";
			else
				ans += "0";
		cout << "Case #" << id++ << ": " << ans << " ";
		for (int i = 0; i < L - 1; i++)
			cout << "?";
		cout << endl;

	}


	return 0;
}
