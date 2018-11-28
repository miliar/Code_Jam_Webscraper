#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = 1005, INF = int(1e9);

int dp[N][N], pos[N];

int main() {
	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		int n;
		cin >> n;
		vector<int> perm;
		vector<pair<int, int> > p;
		perm.resize(n);
		for (int j = 0; j < n; j++) {
			cin >> perm[j];
			p.pb(mp(perm[j], j));
			pos[j] = 0;
		}
		sort(p.begin(), p.end());
		for (int i = 0; i < n; i++)		
			for (int j = 0; j < i; j++) {
				if (perm[j] > perm[i])
					pos[i]++;
			}
		for (int i = 0; i <= n; i++)
			for (int j = 0; j <= n; j++) 
				dp[i][j] = INF;
		dp[0][0] = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j <= i; j++) {
				int rest = n - i, po = pos[p[i].second];
				dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + po);
				dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + rest - po - 1);
			}
		
		int res = INF;
		for (int j = 0; j <= n; j++) 
			res = min(res, dp[n][j]);			
		printf("Case #%d: %d\n", q + 1, res);
	}



	return 0;
}
