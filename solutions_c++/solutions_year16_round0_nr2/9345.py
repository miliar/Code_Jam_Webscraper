#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
const int N = 5e5;
const ld EPS = (ld)1e-10;
const ll MOD = (ll) 1e9 + 7;
const int INF = (int) 1e9;

string s;

int dp[(1 << 11)];

int get(string s) {
	int id = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '1') {
			id |= (1 << i);
		}
	}
	return id;
}

string change(string a, int r) {
	for (int i = 0; i <= r; ++i) {
		a[i] ^= 1;
	}
	int l = 0;
	while (l < r) {
		swap(a[l], a[r]);
		++l;
		--r;
	}
	return a;
}

int stress() {
	fill(dp, dp + 1040, INF);
	queue <string> q;
	q.push(s);
	dp[get(s)] = 0;
	while (!q.empty()) {
		string cur = q.front();
		q.pop();
		for (int i = 0; i < s.size(); ++i) {
			string nxt = change(cur, i);
			if (dp[get(nxt)] > dp[get(cur)] + 1) {
				dp[get(nxt)] = dp[get(cur)] + 1;
				q.push(nxt);
			}
		}
	}
	return dp[(1 << s.size()) - 1];
}

void make_inv(int r) {
	for (int i = 0; i <= r; ++i) {
		s[i] ^= 1;
	}
	int l = 0;
	while (l < r) {
		swap(s[l], s[r]);
		++l;
		--r;
	}
}

int solve(int num) {
	cin >> s;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '+') s[i] = '1';
		else s[i] = '0';
	}
	string t = s;
	int cur = s.size() - 1;
	int answer = 0;
	for (int i = s.size() - 1; i >= 0; --i) {
		if (s[i] == '1') continue;
		if (s[0] == '0') {
			make_inv(i);
			++answer;
			continue;
		}
		int pos = -1;
		int len = 0, mx = 0;
		for (int j = 0; j < i; ++j) {
			if (s[j] == '1') ++len;
			else len = 0;
			if (len > mx) {
				mx = len;
				pos = j;
			}
		}
		make_inv(pos);
		make_inv(i);
		answer += 2;
	}
	s = t;
	cout << "Case #" << num << ": " << answer << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
#ifdef KOBRA
	freopen("toster", "r", stdin);
//    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
#endif
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; ++i) {
		solve(i);
//		cout << stress() << '\n';
	}
	return 0;
}
