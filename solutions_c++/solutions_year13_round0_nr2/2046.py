#include <iostream>
#include <cstdio>

using namespace std;

const int maxn = 100;

int a[maxn][maxn];
int mi[maxn], mj[maxn];

int main() {
	freopen("inputB2.txt", "r", stdin);
	freopen("outputB2.txt", "w", stdout);
	int t, T;
	scanf("%d", &T);
	for(t = 1; t <= T; ++t) {
		int n, m;
		scanf("%d%d", &n, &m);
		memset(mi, -1, sizeof(mi));
		memset(mj, -1, sizeof(mj));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j) {
				scanf("%d", &a[i][j]);
				mi[i] = max(mi[i], a[i][j]);
				mj[j] = max(mj[j], a[i][j]);
			}
		bool res = true;
		for(int i = 0; i < n && res; ++i)
			for(int j = 0; j < m && res; ++j) {
				if(min(mi[i], mj[j]) != a[i][j])
					res = false;
			}
		printf("Case #%d: ", t);
		if(res)	printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}