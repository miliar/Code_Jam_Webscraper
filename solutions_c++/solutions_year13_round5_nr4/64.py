#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
#define pii pair<int, int>
#define pdd pair<double, double>
#define mp make_pair
#define x first
#define y second
#define L(s) ((int)(s).size())
#define pb push_back
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(), (s).end()
int n, t;
string s;
map<int, int> renum;
int numer[21][1 << 20];
int ex[21][66666];
int sz[21];
double f[66666][444], g[66666][444];
int main() {

	for(n = 1; n <= 20; ++n) {
		cerr << n << endl;
		renum.clear();
		int k = 0;
		for(int i = 0; i < (1 << n); ++i) {
			VI sh(0);
			int x = i;
			for(int b = 0; b < n; ++b) {
				sh.pb(x);
				x = (x >> 1) | ((x & 1) << (n - 1));
			}
			int num = k;
			for(int b = 0; b < n; ++b) {
				if (renum.count(sh[b])) {
					num = renum[sh[b]];
					break;
				}
			}
			for(int b = 0; b < n; ++b) {
				renum[sh[b]] = num;
			}
			if (num == k) ++k;
			ex[n][num] = i;
		}
		for(int i = 0; i < (1 << n); ++i)
			numer[n][i] = renum[i];
		sz[n] = k;
	}

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		cin >> s;
		n = L(s);

		int mask = 0;
		int bits = 0;
		for(int i = 0; i < n; ++i) if (s[i] == 'X') {  mask |= (1 << i); ++bits; }
		
		for(int i = 0; i < sz[n]; ++i)
			for(int j = 0; j <= n * n; ++j)
				f[i][j] = 0;

		f[numer[n][mask]][0] = 1;
		
		for(int act = 0; act < n - bits; ++act) {
			
			for(int i = 0; i < sz[n]; ++i)
				for(int j = 0; j <= n * n; ++j)
					g[i][j] = 0;

			for(int i = 0; i < sz[n]; ++i)
				for(int j = 0; j <= n * n; ++j) {
					if (abs(f[i][j]) < 1e-15) continue;
					int mask = ex[n][i];
					for(int bit = 0; bit < n; ++bit) {
						int wt;
						for(wt = 0; mask & (1 << ((bit + wt) % n)); ++wt);
						int nask = mask | (1 << ((bit + wt) % n));
						g[numer[n][nask]][j + n - wt] += f[i][j] / n;
					}
				}

			for(int i = 0; i < sz[n]; ++i)
				for(int j = 0; j <= n * n; ++j)
					f[i][j] = g[i][j];
		}

		double ans = 0;
		for(int i = 0; i < sz[n]; ++i)
			for(int j = 0; j <= n * n; ++j)
				ans += f[i][j] * j;

		printf("Case #%d: %0.9lf\n", tc, ans);
	}
} 