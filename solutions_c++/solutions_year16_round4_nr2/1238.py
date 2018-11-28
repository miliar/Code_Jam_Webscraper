#pragma comment(linker, "/STACK:500000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <unordered_set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

#define y0 y0ChloeGraceMoretz
#define y1 y1ChloeGraceMoretz
#define ll long long
int nextInt() { int n; scanf("%d", &n); return n; }
ll nextLong() { ll n; scanf("%lld", &n); return n; }
const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = (int)2e9;

double p[20];

int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n, k;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &p[i]);
		}
		double res = 0.0;
		for (int mask = 0; mask < (1 << n); ++mask) {
			int len = 0;
			for (int i = 0; i < n; ++i) {
				if (mask & (1 << i)) {
					++len;
				}
			}
			if (len == k) {
				double curRes = 0;
				for (int mask2 = mask; mask2 > 0; mask2 = (mask2 - 1) & mask) {
					int cnt0 = 0;
					int cnt1 = 0;
					double curP = 1.0;
					for (int i = 0; i < n; ++i) {
						if (mask & (1 << i)) {
							if (mask2 & (1 << i)) {
								++cnt1;
								curP *= p[i];
							} else {
								++cnt0;
								curP *= 1.0 - p[i];
							}
						}
					}
					if (cnt0 == cnt1) {
						curRes += curP;
					}
				}
				res = max(curRes, res);
			}
		}
		printf("Case #%d: %.10lf\n", tt, res);
	}
	return 0;
}