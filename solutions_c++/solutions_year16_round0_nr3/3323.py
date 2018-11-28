#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 16, J = 50;

vector<pair<ll, vector<int> > > ans;

inline int getDiv(ll curr, short base) {
	ll n = 0, b = 1;
	for (short i = 0; i < N; ++i) {
		n += b * ((curr >> i) & 1LL);
		b *= base;
	}
	for (ll i = 2; i * i <= n; i += 1 + (i & 1)) {
		if (n % i == 0)
		  return i;
	}
	return -1;
}

inline bool check(ll curr, vector<int>& factors) {
	factors.reserve(9);
	for (short base = 2; base <= 10; ++base) {
		factors.push_back(getDiv(curr, base));
		if (factors.back() == -1) return 0;
	}
	return 1;
}

inline void solve() {
	ll curr = (1LL << N) - 1;
	ans.reserve(J);
	while (ans.size() != J) {
		vector<int> factors;
		if (check(curr, factors)) ans.push_back( { curr, factors });
		curr -= 2;
	}
}

string con(ll &x) {
	string ans(N, 0);
	for (short i = 0; i < N; ++i)
		ans[N - i - 1] = '0' + (1 & (x >> i));
	return ans;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	vector<int> factors;

	solve();
	cout << "Case #1:\n";
	for (auto &x : ans) {
		cout << con(x.first);
		for (int div : x.second)
			cout << ' ' << div;
		cout << '\n';
	}

	return 0;
}
