#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
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
#define inf 1000000000
int t, n, m;
char a[111][111];
char di[256], dj[256];
int ci[111], cj[111];
int main() {

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	di['^'] = -1;
	di['v'] = +1;
	dj['<'] = -1;
	dj['>'] = +1;

	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cin >> n >> m;
		for(int i = 0; i < n; ++i) ci[i] = 0;
		for(int j = 0; j < m; ++j) cj[j] = 0;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				cin >> a[i][j];
				if (a[i][j] != '.') {
					++ci[i];
					++cj[j];
				}
			}
		}
		bool bad = 0;
		int fix = 0;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				if (a[i][j] != '.'){
					if (ci[i] == 1 && cj[j] == 1) {
						bad = 1;
						continue;
					}
					int ni = i, nj = j;
					int d_i = di[a[i][j]];
					int d_j = dj[a[i][j]];
					do {
						ni += d_i;
						nj += d_j;
						if (ni < 0 || nj < 0 || ni >= n || nj >= m) {
							++fix;
							break;
						}
						if (a[ni][nj] != '.') {
							break;
						}
					} while(1);
				}
			}
		}
		cout << "Case #" << tc << ": ";
		if (bad) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << fix << endl;
		}


	}
}
