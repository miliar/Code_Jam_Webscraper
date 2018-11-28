#include <bits/stdc++.h>
using namespace std;

#define rep(i, f, t) for (int i = f; i < t; ++i)
#define trav(x, a) for (auto& x : a)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int solve() {
	int N;
	string s;
	cin >> N >> s;
	int ind = 0;
	int res = 0;
	int count = 0;
	trav(c, s) {
		int a = c - '0';
		if (a)
			res = max(res, ind - count);
		count += a;
		++ind;
	}
	return res;
}

int main() {
	int T;
	cin >> T;
	rep(i,0,T)
		cout << "Case #" << i+1 << ": " << solve() << endl;
}
