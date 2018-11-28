#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int solve() {
	int N, X;
	scanf("%d%d", &N, &X);
	vector<int> sz;
	for (int i = 0; i < N; i++) {
		int v;
		scanf("%d", &v);
		sz.push_back(v);
	}
	sort(sz.begin(), sz.end());
	int p = sz.size() - 1;
	int match = 0;
	for (int i = 0; i < p; i++) {
		while (i < p && sz[i] + sz[p]>X) p--;
		if (i < p) {
			match++;
			p--;
		}
	}
	return sz.size() - match;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int c = 1; c <= T; c++) {
		printf("Case #%d: %d\n", c, solve());
	}
}