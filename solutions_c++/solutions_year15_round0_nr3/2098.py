#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>

using namespace std;

#define mp make_pair
#define sqr(x) ((x) * (x))
#define all(a) a.begin(), a.end()

typedef long long int64;

const int INF = (int) 2e9;
const int64 INF64 = (int64) 1e18;
const double EPS = 1e-9;

int a[][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};

inline int mult(int x, int y) {
	return a[abs(x)][abs(y)] * (x > 0 ? 1 : -1) * (y > 0 ? 1 : -1);
}

int m[300];
int dp[10100][10100];
char s[10100];
int k[4];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	m['1'] = 1;
	m['i'] = 2;
	m['j'] = 3;
	m['k'] = 4;

	int tests;
	scanf("%d", &tests);
	for (int t = 0; t < tests; t++) {

		int l, x;
		scanf("%d%d", &l, &x);
		scanf("%s", s);

		for (int i = 0; i <= l; i++) {
			dp[i][i] = 1;
			for (int j = i + 1; j <= l; j++) {
				dp[i][j] = mult(dp[i][j - 1], m[s[j - 1]]);
			}
		}

		k[0] = 1;
		for (int i = 1; i < 4; i++) {
			k[i] = mult(k[i - 1], dp[0][l]);
		}

		for (int k1 = 0; k1 < 4; k1++) {
				for (int k2 = 0; k2 < 4; k2++) {
					for (int k3 = 0; k3 < 4; k3++) {
						if (k1 + k2 + k3 + 2 > x || (k1 + k2 + k3 + 2) % 4 != x % 4) {
							continue;
						}
						for (int i = 0; i <= l; i++) {
							for (int j = 0; j <= l; j++) {
								if (mult(k[k1], dp[0][i]) == 2 && mult(mult(dp[i][l], k[k2]), dp[0][j]) == 3 && 
									mult(dp[j][l], k[k3]) == 4) {
									printf("Case #%d: YES\n", (t + 1));
									goto loop;
								}
							}
						}
					}
				}
		}

		for (int k1 = 0; k1 < 4; k1++) {
			for (int k2 = 0; k2 < 4; k2++) {
				if (k1 + k2 + 1 > x || (k1 + k2 + 1) % 4 != x % 4) {
					continue;
				}
				for (int i = 0; i <= l; i++) {
					for (int j = i; j <= l; j++) {
						if (mult(k[k1], dp[0][i]) == 2 && dp[i][j] == 3 &&
							mult(dp[j][l], k[k2]) == 4) {
								printf("Case #%d: YES\n", (t + 1));
								goto loop;
						}
					}
				}
			}
		}

		/*for (int i = 0; i <= l; i++) {
			for (int j = 0; j <= l; j++) {
				for (int k1 = 0; k1 < 4; k1++) {
					for (int k2 = 0; k2 < 4; k2++) {
						for (int k3 = 0; k3 < 4; k3++) {
							if (k1 + k2 + k3 + 2 > x || (k1 + k2 + k3 + 2) % 4 != x % 4) {
								continue;
							}

							if (mult(k[k1], dp[0][i]) == 2 && mult(mult(dp[i][l], k[k2]), dp[0][j]) == 3 &&
								mult(dp[j][l], k[k3]) == 4) {
									printf("Case #%d: YES\n", (t + 1));
									goto loop;
							}
						}

						if (i > j && (k1 + k2 + 1 > x || (k1 + k2 + 1) % 4 != x % 4)) {
							continue;
						}

						if (mult(k[k1], dp[0][i]) == 2 && dp[i][j] == 3 &&
							mult(dp[j][l], k[k2]) == 4) {
								printf("Case #%d: YES\n", (t + 1));
								goto loop;
						}
					}
				}
			}
		}*/

		printf("Case #%d: NO\n", (t + 1));
		loop: ;
	}

	return 0;
}