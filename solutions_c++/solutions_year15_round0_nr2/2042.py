#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstring>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;


void solve(int test) {
	int D;
	scanf("%d", &D);
	vector<int> a(D);
	for (int i = 0; i < D; i++) scanf("%d", &a[i]);
	int ans = 1000;
	for (int w = 1; w <= 1000; w++) {
		int res = w;
		for (int i = 0; i < D; i++) res += (a[i] - 1) / w;
		ans = min(res, ans);
	}
	printf("Case #%d: %d\n", test, ans);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) solve(t);
}
