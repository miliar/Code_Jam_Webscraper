#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve() {
	static int tc = 1;
	cout << "Case #" << tc << ": ";
	tc++;
	int N, K;
	cin >> N >> K;
	bool impossible = false;
	rep(i,0,N) {
		string s;
		cin >> s;
		if (count(all(s), '0')) continue;
		impossible = true;
	}
	if (impossible) cout << "IMPOSSIBLE" << endl;
	else {
		rep(i,0,K-1) cout << "?0";
		cout << "? 0";
		rep(i,0,K-1) cout << '1';
		cout << endl;
	}
	string str;
	cin >> str;
}

int main() {
	int N;
	cin.sync_with_stdio(false);
	cin >> N;
	while (N --> 0) solve();
}
