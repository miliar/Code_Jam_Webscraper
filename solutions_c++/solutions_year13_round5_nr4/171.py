#include <cstdio>
#include <iomanip>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

typedef long double ld;

const int Maxn = 21;
const int MaxN = 1 << Maxn;

int t;
ld dp[Maxn][MaxN];

int delta(int n, int m, int v)
{
	int delta = 0;
	while (m & 1 << v) {
		delta++;
		v = (v + 1) % n;
	}
	return delta;
}

ld f(int n, int m)
{
	if (dp[n][m] < 0.0)
		if (m == (1 << n) - 1) dp[n][m] = 0.0l;
		else {
			double res = 0.0;
			for (int i = 0; i < n; i++) {
				int d = delta(n, m, i);
				res += (n - d + f(n, m | 1 << (i + d) % n)) / ld(n);
			}
			dp[n][m] = res;
		}
	return dp[n][m];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	fill((ld*)dp, (ld*)dp + Maxn * MaxN, -1.0);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		string s; cin >> s;
		int m = 0;
		for (int i = 0; i < s.length(); i++)
			m |= (s[i] == 'X') << i;
		cout << "Case #" << tc << ": " << fixed << setprecision(14) << f(s.length(), m) << endl; 
	}
	return 0;
}