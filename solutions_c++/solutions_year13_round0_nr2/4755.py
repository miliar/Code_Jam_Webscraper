#include <cstdio>
#include <cstring>

using namespace std;
int T,C;
int n, m;
int a[128][128], f[128][128];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &a[i][j]);
		int ans = 1;
		for (int x = 1; x <= 100; x++) {
			memset(f, 0, sizeof(f));
			for (int i = 0; i < n; i++) {
				int cnt = 0; 	
			        for (int j = 0; j < m; j++) 	
					cnt += (a[i][j] == x);
				if (cnt == m)
				    for (int j =0; j < m; j++)
					f[i][j] = 1;
			}
			for (int i = 0; i < m; i++) {
				int cnt = 0;
				for (int j = 0; j < n; j++)
					cnt += (a[j][i] == x);
				if (cnt == n)
					for (int j = 0; j < n; j++)
						f[j][i] = 1;
			}

			for (int i = 0; i < n; i++) 
				for (int j = 0; j < m; j++)
					if (a[i][j] == x && f[i][j] == 0)
						ans = 0;
			if (ans == 0) break;
			for (int i =0; i < n; i++)
				for (int j = 0; j < m; j++)
					if (a[i][j] == x) a[i][j] = x+1;
		}
		printf("Case #%d: ", ++C);
		if (ans) puts("YES");
		else puts("NO");
	}
	return 0;
}
