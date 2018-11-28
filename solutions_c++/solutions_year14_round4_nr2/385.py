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
map<int, int> pos;
int A[1005];
int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		int N, ans = 0;
		scanf("%d", &N);
		pos.clear();
		for (int i = 0; i < N; ++i) {
			scanf("%d", &A[i]);
			pos[A[i]] = i;
		}
		sort(A, A + N, greater<int>());
		for (int i = 0; i < N; ++i) {
			int vleft = 0, vright = 0;
			for (int j = 0; j < i; ++j)
				if (pos[A[j]] < pos[A[i]]) {
					++vright;
				} else {
					++vleft;
				}
			ans += min(vleft, vright);
		}
		printf("Case #%d: %d\n", cn, ans);
	}
}

