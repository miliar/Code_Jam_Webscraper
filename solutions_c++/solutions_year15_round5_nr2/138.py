#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define exit(a) {prt(a);return 0;}
#define PI 3.141592653589
#define int2 pair<int, int>

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n";
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";

int main() {
	int tests = next();
	for (int test = 1; test <= tests; test++) {
		int n = next(), k = next();
		int s[n - k + 1];
		for (int i = 0; i < n - k + 1; i++) s[i] = next();
		vector<int> val[k];
		for (int i = 0; i < k; i++) val[i].pb(0);
		for (int i = 0; i < n - k; i++) val[i % k].pb(val[i % k][val[i % k].size() - 1] + s[i + 1] - s[i]);
		//prtn(val[0], val[0].size());
		//prtn(val[1], val[1].size());
		vector<int> imax(0);
		vector<int> imin(0);
		for (int i = 0; i < k; i++) {
			int imn = 0;
			int imx = 0;
			for (int j = 0; j < val[i].size(); j++) {
				if (val[i][j] < val[i][imn]) imn = j;
				if (val[i][j] > val[i][imx]) imx = j;
			}
			imax.pb(imx);
			imin.pb(imn);
		}
		int maxdiff = 0;
		for (int i = 0; i < k; i++) maxdiff = max(maxdiff, val[i][imax[i]] - val[i][imin[i]]);

		bool can[k + 1][k];
		for (int i = 0; i <= k; i++) for (int j = 0; j < k; j++) can[i][j] = false;
		can[0][0] = true;
		for (int i = 0; i < k; i++) {
			int diff = val[i][imax[i]] - val[i][imin[i]];
			int dist = min(maxdiff - diff, k - 1);
			int add = (val[i][0] - val[i][imin[i]]) % k;
			for (int j = 0; j < k; j++) if (can[i][j])
				for (int t = 0; t <= dist; t++) can[i + 1][(add + j + t) % k] = true;
		}
		if (!can[k][(s[0] + k * 100000) % k]) maxdiff++;




		printf("Case #%d: %d\n", test, maxdiff);
	}

}
