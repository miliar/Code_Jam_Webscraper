#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <cassert>
#include <climits>
using namespace std;
int S[10005];
int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		int N, X;
		scanf("%d%d", &N, &X);
		for (int i = 0; i < N; ++i) scanf("%d", &S[i]);
		sort(S, S + N);
		int p = N - 1, ans = N;
		for (int i = 0; i < N; ++i) {
			while (i < p && S[i] + S[p] > X) --p;
			if (i >= p) break;
			--ans;
			--p;
		}
		printf("Case #%d: %d\n", cn, ans);
	}
}

