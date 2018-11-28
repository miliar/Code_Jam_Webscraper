#include <bits/stdc++.h> 
using namespace std;

const int N = 21;

double memo[N][N];
double p[N];
int n, k;

double v[N];

double ans;


double dp(int ind, int toYes) {
	if (toYes < 0) return 0;
	if (ind == k) return !toYes;

	auto &res = memo[ind][toYes];
	if (res == res) return res;

	res = v[ind] * dp(ind + 1, toYes - 1)
	  + (1 - v[ind]) * dp(ind + 1, toYes);

	return res;
}

void rec(int i, int j) {
	if (j == k) {
		memset(memo, -1, sizeof memo);
		ans = max(ans, dp(0, k / 2));
		return ;
	}
	if (i == n) return;
	v[j] = p[i];
	rec(i + 1, j + 1);
	rec(i + 1, j);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	cout << fixed << setprecision(6);
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
			cin >> p[i];
		ans = 0;
		rec(0, 0);

		cout << "Case #" << cs << ": " << ans << '\n';

	}

}
