#include <bits/stdc++.h>

#define ll long long
#define ld long double
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

const int nm = 30;

int n;
char a[nm][nm];
char a2[nm][nm];
int b[nm];
bool fr[nm];

bool thu(int i) {
	if (i == n)
		return 1;
	int dem = 0;
	for (int j = 0; j < n; ++j) {
		if (fr[j] && a2[b[i]][j] == '1') {
			fr[j] = 0;
			dem++;
			if (!thu(i + 1))
				return 0;
			fr[j] = 1;
		}
	}
	return dem;
}

bool kt(int mask) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (a[i][j] == '1' || ((mask >> (i * n + j)) & 1))
				a2[i][j] = '1';
			else
				a2[i][j] = '0';
		}
		a2[i][n] = 0;
	}
	for (int i = 0; i < n; ++i)
		b[i] = i;
	do {
		memset(fr, 1, sizeof(fr));
		if (!thu(0))
			return 0;
	} while (next_permutation(b, b + n));
	return 1;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	int last = 1 << (n * n);
	int res = n * n;
	for (int mask = 0; mask < last; ++mask) {
		if (__builtin_popcount(mask) < res && kt(mask))
			res = __builtin_popcount(mask);
	}
	cout << res << "\n";
}

int main() {
#ifdef LOCAL
	freopen("D-small-attempt0 (1).in", "r", stdin);
//	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
