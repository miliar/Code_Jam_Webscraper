#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {

	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);

	int t;
	int b;
	long long m;
	int ans[50], tn;
	bool vis[100];
	int i, j;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		//printf("t= %d, cas = %d\n", t, cas);
		cin >> b;
		cin >> m;
		//printf ("%d %I64d\n", b, m);
		memset(ans, 0, sizeof(ans));
		memset(vis, 0, sizeof(vis));
		tn = 0;
		i = 0;
		while (m) {
			if (m % 2 == 1) {
				ans[tn++] = i;
				vis[i+1] = 1;
			}
			m /= 2;
			i += 1;
		}
		//printf("tn = %d\n", tn);
		if (ans[tn-1] > b-2) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
			continue;
		}
		if (ans[tn-1] == b-2 && tn > 1) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
			continue;
		}
		if (ans[tn-1] == b-2 && tn == 1) {
			printf("Case #%d: POSSIBLE\n", cas);
			for (i = 0; i < b; i++) {
				for (j = 0; j < b; j++) {
					if (j <= i)
						printf("0");
					else
						printf("1");
				}
				printf("\n");
			}
			continue;
		}
		printf("Case #%d: POSSIBLE\n", cas);
		for (i = 0; i < b; i++) {
			for (j = 0; j < b; j++) {
				if (j <= i)
					printf("0");
				else if (j != b-1)
					printf("1");
				else if (vis[i])
					printf("1");
				else
					printf("0");
			}
			printf("\n");
		}
	}
	return 0;
}
