#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int maxn = 110;
int a[maxn][maxn];
int rmx[maxn], cmx[maxn];
int N, M;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	int nc = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		for (int i = 0; i < N; i++) {
			rmx[i] = -1;
			for (int j = 0; j < M; j++) {
				rmx[i] = max(rmx[i], a[i][j]);
			}
		}
		for (int i = 0; i < M; i++) {
			cmx[i] = -1;
			for (int j = 0; j < N; j++) {
				cmx[i] = max(cmx[i], a[j][i]);
			}
		}
		int fg = 1;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (a[i][j] < rmx[i] && a[i][j] < cmx[j])
					fg = 0;
			}
			if (!fg)
				break;
		}
		printf("Case #%d: ", ++nc);
		if (fg)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
