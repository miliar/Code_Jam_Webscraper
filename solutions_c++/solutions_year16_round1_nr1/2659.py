#include <bits/stdc++.h>

using namespace std;

#define ll long long

int t;


void solve();

int main() {
	ios::sync_with_stdio(0);

	bool file = true;
	if (file) {
		freopen("A-large.in","r", stdin);
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
	string word;
	cin >> word;
	string res = "";
	res+= word[0];
	for (int i = 1; i < word.size(); i++) {
		if (res[0] <= word[i])
			res = word[i] + res;
		else
			res+= word[i];
	}
	cout << res;
}
