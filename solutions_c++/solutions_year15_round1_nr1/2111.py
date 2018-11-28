#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>

using namespace std;

#define INF 1000000007

int T, N, x, y;
int m[10000];

void solve() {
	for (int i = 1; i < N; i++) {
		x += max(0, m[i - 1] - m[i]);
	}
	
	int dec = 0;
	for (int i = 1; i < N; i++) {
		dec = max(dec, m[i - 1] - m[i]);
	}
	for (int i = 0; i + 1 < N; i++) {
		y += min(dec, m[i]);
	}
}

int main() {
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) scanf("%d", &m[i]);
		x = y = 0;
		solve();
		printf("Case #%d: %d %d\n", i, x, y);
	}
	return 0;
}

