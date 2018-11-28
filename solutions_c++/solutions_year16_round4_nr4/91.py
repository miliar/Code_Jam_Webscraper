#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = 0;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		
		int n;
		cin >> n;
		vector<vector<char> > a(n, vector<char>(n));
		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) cin >> a[i][j];

		int ans = n * n + 1;
		for (int mask = 0; mask < (1 << (n * n)); mask++) {
			int cost = 0;
			vector<vector<char> > b = a;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (mask & (1 << (i * n + j))) {
						b[i][j] = '1';
						cost++;
					}
				}
			}

			bool can = 1;
			vector<int> p(n);
			for (int i = 0; i < n; i++) p[i] = i;
			do {
				vector<vector<char> > dp(n + 1, vector<char>(1 << n, 0));
				dp[0][0] = 1;
				for (int i = 0; i < n; i++) {
					for (int mask = 0; mask < 1 << n; mask++) {
						if (!dp[i][mask]) continue;
						bool was = 0;
						for (int j = 0; j < n; j++) {
							if (b[p[i]][j] == '1' && !(mask & (1 << j))) {
								was = 1;
								dp[i + 1][mask | (1 << j)] = 1;
							}
						}
						if (!was) can = 0;
					}
				}
			} while (next_permutation(p.begin(), p.end()));
			if (can) ans = min(ans, cost);
		}
		
		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}