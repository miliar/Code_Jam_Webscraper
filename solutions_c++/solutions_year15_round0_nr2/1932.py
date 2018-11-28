#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
int t, n;
int d[1111];
int f[1111][1111];
int main() {

	for(int need = 1; need <= 1000; ++need) {
		for(int have = 1; have <= 1000; ++have) {
			f[need][have] = 1e9;
			if (have <= need) f[need][have] = 0; else
				for(int part = 1; part < have; ++part) {
					f[need][have] = min(f[need][have], f[need][part] + f[need][have - part] + 1);
				}
		}
	}

//	cerr << f[6][18] << endl;
//
//	exit(0);

	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		cin >> n;
		memset(d, 0, sizeof(d));
		for(int i = 0; i < n; ++i) {
			cin >> d[i];
		}

		int ans = 1e9;
		for(int need = 1; need <= 1000; ++need) {
			int cur = need;
			for(int i = 0; i < n; ++i) {
				cur += f[need][d[i]];
			}
			ans = min(ans, cur);
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
