#include <cstdio>
#include <algorithm>
using namespace std;

int t[111][111];
int mxr[111], mxc[111];

bool test() {
	int n,m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		mxr[i] = 0;
	}
	for (int j = 0; j < m; j++) {
		mxc[j] = 0;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &t[i][j]);
			mxr[i] = max(mxr[i], t[i][j]);
			mxc[j] = max(mxc[j], t[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (t[i][j] != mxr[i] && t[i][j] != mxc[j]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: %s\n", i, test() ? "YES" : "NO");
	}
	return 0;
}
