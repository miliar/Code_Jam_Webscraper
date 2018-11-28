#include <bits/stdc++.h>

using namespace std;

int T, N;
bool vis[10];
int main() {
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d", &N);
		if (N == 0) puts("INSOMNIA");
		else {
			memset(vis, 0, sizeof(vis));
			int L;
			for (L = N; ; L += N) {
				int tmp = L;
				while (tmp) {
					vis[tmp % 10] = true;
					tmp /= 10;
				}
				bool flag = true;
				for (int i = 0; i < 10; i++) 
					if (!vis[i]) {
						flag = false;
						break;
					}
				if (flag) break;
			}
			printf("%d\n", L);
		}
	}
	return 0;
}

