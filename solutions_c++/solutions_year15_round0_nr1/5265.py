#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void fastInOut();

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	fastInOut();
	int t, sMax;
	string x;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		cin >> sMax >> x;
		int tot = 0, ret = 0;
		for (int s = 0; s <= sMax; ++s) {
			if (tot < s)
				ret += (s - tot), tot = s;
			tot += (x[s] - '0');
		}
		cout << "Case #" << tst << ": " << ret << "\n";
	}
	return 0;
}

void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
