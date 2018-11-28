#include <stdio.h>
#include <cassert>
#include <cstring>
#include <map>
#include <set>
#include <time.h>
#include <algorithm>
#include <stack>
#include <queue>
#include <utility>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

typedef pair <int, int> ii;
typedef pair <long long, long long> ll;

double p[555], d[55][55];

double get(vector <double> &t, int k) {

	for (int i = 0; i <= k; i++) {
		for (int j = 0; j <= k; j++) {
			d[i][j] = 0.0;
		}
	}
	d[0][k / 2] = 1.0;

	for (int i = 0; i < k; i++) {
		for (int j = 0; j <= k; j++) {
			if( j ) d[i + 1][j] += d[i][j - 1] * t[i];
			if( j+1 <= k ) d[i + 1][j] += d[i][j + 1] * (1.0 - t[i]);
		}
	}
	return d[k][k / 2];
}

void solve() {
	int k, n;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%lf", p + i);
	double ans = 0.0;
	for (int i = 0; i < (1 << n); i++) {
		int c = 0;
		for (int j = 0; j < n; j++) {
			if (i & (1 << j))
				++c;
		}
		if (c == k) {
			
			vector <double> t;
			for (int j = 0; j < n; j++) {
				if (i & (1 << j)) {
					t.push_back(p[j]);
				}
			}
			
			ans = max(ans, get(t, k));
		}
	}
	printf("%lf\n", ans);
	

}

int main() {

	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int R = 1; R <= T; R++) {
		printf("Case #%d: ", R);
		solve();

	}

}