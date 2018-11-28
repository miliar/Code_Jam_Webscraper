#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

double DP[500][500];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("outputfast.txt", "w", stdout);
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		cout << "Case #" << test << ": ";
		double ans = 0.;
		int n, k;
		cin >> n >> k;
		vector <double> p(n);
		for (int i = 0; i < n; i++) {
			cin >> p[i];
		}
		sort(p.begin(), p.end());
		for (int i = 0; i < n; i++)
			p.push_back(p[i]);


		for (int i = 0; i < n; i++) {
			vector <double> cur;
			for (int j = 0; j < k; j++)
				cur.push_back(p[j + i]);
				
			memset(DP, 0, sizeof(DP));
			DP[0][0] = 1.0;
			for (int j = 0; j < k; j++)
				for (int j2 = 0; j2 < k; j2++)
					if (DP[j][j2]) {
						DP[j + 1][j2 + 1] += DP[j][j2] * cur[j];
						DP[j + 1][j2] += DP[j][j2] * (1. - cur[j]);
					}
			if (ans < DP[k][k / 2])
				ans = DP[k][k / 2];
		}


		printf("%.9f\n", ans);
	}

	return 0;
}