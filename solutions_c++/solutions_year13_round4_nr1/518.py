#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>
#include <deque>
#include <string.h>


using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
#define debug(x) cerr << #x << ": " << (x) << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector <vi> vvi;


typedef pair<int, int> pii;


int delta(int k, int n) {
	return k * (2 * n + 1 - k) / 2;
}

void solve() {
	int n, m;
	cin >> n >> m;

	vvi pass(n, vi(n, 0));

	int was = 0;
		
	vi o(m), e(m), p(m);
	for (int i = 0; i < m; ++i) {
		cin >> o[i] >> e[i] >> p[i];
		--o[i], --e[i];

		pass[ o[i] ][ e[i] ] += p[i];
		was += p[i] * delta(e[i] - o[i], n);
	}

	for (int from = 0; from < n; ++from) {
		for (int to = from + 1; to < n; ++to) {
			if (pass[from][to] == 0) {
				continue;
			}
			// cerr << "at " << from << ", " << to << endl;
			for (int a = from + 1; a <= to; ++a) {
				for (int b = max(a + 1, to); b < n; ++b) {
					if (pass[a][b] == 0)
						continue;
					int value = min(pass[a][b], pass[from][to]);
					// cerr << "swapped " << from << ", " << to << " with " << a << ", " << b << endl;
					pass[from][to] -= value;
					pass[a][b] -= value;
					pass[from][b] += value;
					pass[a][to] += value;
				}
			}
		}
	}

	int res = 0;
	for (int from = 0; from < n; ++from) {
		for (int to = from + 1; to < n; ++to) {
			res += pass[from][to] * delta(to - from, n);
		}
	}

	int ans = was - res;
	cout << ans << endl;
}



void init() {
	int nx = 10;
	for (int i = 1; i < nx; ++i) {
		for (int j = 1; j < nx; ++j) {
			for (int d = 0; d < nx; ++d) {


			}
		}

	}


}


int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);
	//std::ios::sync_with_stdio(false);

	init();


	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t + 1 << ": ";
		solve();
	}

    return 0;
}

