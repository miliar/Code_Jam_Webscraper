#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ff first
#define ss second
#define mp make_pair
#define pb push_back

typedef long long llong;
typedef pair<int, int> pii;

const string imposs = "IMPOSSIBLE";

void flip(string &str, int start, int len) {

	for (int i = start; i < start + len; i++) {
		str[i] = (str[i] == '+' ? '-' : '+');
	}

}

void process() {

	string str;
	cin >> str;

	int k;
	cin >> k;

	int n = str.size();
	int ans = 0;

	for (int i = 0; i <= n - k; i++) {

		if (str[i] == '-') {
			ans++;
			flip(str, i, k);
		}

	}

	bool valid = true;

	for (char c : str) {
		if (c == '-') valid = false;
	}

	if (valid) cout << ans;
	else cout << imposs;

}

void solve() {

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {

		cout << "Case #" << (i + 1) << ": ";
		process();
		cout << endl;

	}
	
}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	#ifdef LOCAL
		ifstream in("in");
		cin.rdbuf(in.rdbuf());

		ofstream out("out");
		cout.rdbuf(out.rdbuf());
	#endif

	solve();

	return 0;

}