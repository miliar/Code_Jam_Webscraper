#include <bits/stdc++.h>

#define ll long long
#define ld double
#define pb push_back
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define Repd(i,n) for(int i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(int i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(int i = (a); i >= (b); --i)
#define Fit(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define Fitd(i,v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
#define group vector<int>

using namespace std;

int n, r, p, s;

string f(string x, int n) {
	string tmp;
	for (int i = 1; i <= n; ++i) {
		tmp = "";
		for (int j = 0; j < x.length(); ++j) {
			if (x[j] == 'R')
				tmp = tmp + "RS";
			else if (x[j] == 'P')
				tmp = tmp + "PR";
			else
				tmp = tmp + "PS";
		}
		x = tmp;
	}
	return x;
}

bool kt(string a) {
	int dr = 0, dp = 0, ds = 0;
	for (int i = 0; i < a.length(); ++i) {
		if (a[i] == 'R')
			dr++;
		else if (a[i] == 'P')
			dp++;
		else
			ds++;
	}
	return dr == r && dp == p && ds == s;
}

int cmp(string s, int l, int m, int r) {
	int i = l, j = m + 1;
	while (i <= m) {
		if (s[i] < s[j])
			return -1;
		if (s[i] > s[j])
			return 1;
		i++;
		j++;
	}
	return 0;
}

void sort(string &s, int l, int r) {
	if (l == r)
		return;
	int m = (l + r) >> 1;
	int L = r - l + 1;
	sort(s, l, m);
	sort(s, m + 1, r);
	int tmp = cmp(s, l, m, r);
	if (tmp > 0)
		for (int i = l; i <= m; ++i)
			swap(s[i], s[i + L / 2]);
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n >> r >> p >> s;
	string res = "Z";
	if (p) {
		string a = f("P", n);
		if (kt(a) && a < res)
			res = a;
	}
	if (r) {
		string a = f("R", n);
		if (kt(a) && a < res)
			res = a;
	}
	if (s) {
		string a = f("S", n);
		if (kt(a) && a < res)
			res = a;
	}
	if (res == "Z") {
		cout << "IMPOSSIBLE\n";
		return;
	}
//	cout << res << " ";
	sort(res, 0, (1 << n) - 1);
	cout << res << "\n";
}

int main() {
#ifdef LOCAL
	freopen("A-large (3).in", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
