#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <iostream>
using namespace std;

double dp[1 << 20];
double prob[1 << 20];
string ma; 
int n;

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("D.in", "r", stdin);

	int T;
	cin >> T;
	for (int _ = 1; _ <= T; ++_) {
		cin >> ma;
		n = ma.size();
		int stat = 0;
		int c = 0;
		for (int i = 0; i < n; ++i) {
			if (ma[i] == 'X') {
				stat ^= 1 << i;
			} else {
				c++;
			}
		}
		for (int i = 0; i < 1 << n; ++i) {
			dp[i] = 0;
			prob[i] = 0;
		}
		prob[stat] = 1;
		double ans = 0;
		for (int i = 0; i < (1 << n); ++i) {
			if ((stat & i) != stat) {
				continue;
			}
			if (i == (1 << n) - 1) {
				continue;
			}
			for (int j = 0; j < n; ++j) {
				int k = j;
				int cost = n;
				while (i >> k & 1) {
					cost--;
					k = (k + 1) % n;
				}
				dp[i ^ (1 << k)] += (dp[i] + cost * prob[i]) / n;
				prob[i ^ (1 << k)] += prob[i] / n;
			}

		}

		ans = dp[(1 << n) - 1];
		printf("Case #%d: %.10f\n", _, ans);
	}
}
