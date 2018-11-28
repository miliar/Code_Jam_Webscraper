#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof((x).begin()) e=(x).begin(); e!=(x).end(); ++e)

const int N = 100 + 10;

int n;
double V, X;
int alive[N];
double R[N], C[N];

void solve()
{
	cin >> n;
	cin >> V >> X;
	double minC = 100, maxC = 0;
	double temp = 0, totR = 0;
	for(int i = 0; i < n; ++ i) {
		alive[i] = true;
		cin >> R[i] >> C[i];
		temp += R[i] * C[i];
		totR += R[i];
		minC = min(minC, C[i]);
		maxC = max(maxC, C[i]);
	}

	temp /= totR;

	if (maxC + 1e-8 < X || minC - 1e-8 > X) {
		puts("IMPOSSIBLE");
		return;
	}

	for( ; abs(temp - X) > 1e-8; ) {
		if (temp > X) {
			int id = -1;
			for(int i = 0; i < n; ++ i) {
				if (! alive[i]) continue;
				if (id < 0 || C[id] < C[i]) {
					id = i;
				}
			}
			double otherTemp = 0, otherR = 0;
			for(int i = 0; i < n; ++ i) {
				if (! alive[i]) continue;
				if (id == i) continue;
				otherTemp += R[i] * C[i];
				otherR += R[i];
			}
			double newR = (otherR * X - otherTemp) / (C[id] - X);
			if (newR < 0) {
				alive[id] = false;
			} else {
				R[id] = newR;
			}
		} else {
			int id = -1;
			for(int i = 0; i < n; ++ i) {
				if (! alive[i]) continue;
				if (id < 0 || C[id] > C[i]) {
					id = i;
				}
			}
			double otherTemp = 0, otherR = 0;
			for(int i = 0; i < n; ++ i) {
				if (! alive[i]) continue;
				if (id == i) continue;
				otherTemp += R[i] * C[i];
				otherR += R[i];
			}
			double newR = (otherR * X - otherTemp) / (C[id] - X);
			if (newR < 0) {
				alive[id] = false;
			} else {
				R[id] = newR;
			}
		}
		temp = 0;
		totR = 0;
		for(int i = 0; i < n; ++ i) {
			if (alive[i]) {
				temp += R[i] * C[i];
				totR += R[i];
			}
		}
		temp /= totR;
	}

	printf("%.12f\n", V / totR);
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
