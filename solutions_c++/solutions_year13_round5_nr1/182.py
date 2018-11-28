#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;
typedef long long ll;

double solve(ll B, int N, ll X[]) {
	sort(X, X+37);
	ll c[40] = {};
	double ans = 0.0;
	ll z = 0;
	for (int i = 1; i <= 1000; i++) {
		for (int j = 36; j >= 0; j--) {
			if (X[j] < i) {
				c[j]++;
				X[j]++;
				B--;
				z++;
			}
			if (B < 0)
				goto NEXT;
			int n = 0;
			for (int j = 0; j < 37; j++) {
				if (X[j] == X[0])
					n++;
			}
			//printf("n=%d z=%lld\n", n, z);
			double r = 0.0;
			for (int j = 0; j < n; j++) {
				//printf("c[%d]=%lld\n", j, c[j]);
				double d = (c[j]*36.0 - z);
				r += d;
			}
			ans = max(ans, r/n);
		}
	}
NEXT:
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		ll B;
		int N;
		ll X[40] = {};
		cin >> B >> N;
		for (int j = 0; j < N; j++) {
			cin >> X[j];
		}
		double r = solve(B, N, X);
		printf("Case #%d: %.12f\n", i+1, r);
	}
}
