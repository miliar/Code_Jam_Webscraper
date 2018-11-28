#include <bits/stdc++.h>

using namespace std;

#define ll long long

int t;


void solve();

int main() {
	ios::sync_with_stdio(0);

	bool file = true;
	if (file) {
		freopen("B-large.in","r", stdin);
		freopen("output.out", "w", stdout);
	}

	cin >> t;
	for (int z = 1; z<= t; z++) {
		cout << "Case #" << z << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

void solve() {
	string val;
	cin >> val;
	int res = 0;
	char last = val[0];
	for (int i = 1; i < val.length(); i++) {
		if (last != val[i])
			res++;
		last = val[i];
	}
	if (last == '-')
		res++;
	cout << res;
}
