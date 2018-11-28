#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int T, n, m;
char s[100], ch[105][105];
bool l[105][105], r[105][105], u[105][105], d[105][105];

int main(int argc, char** argv) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (int times=0; times<T; times++) {
		printf("Case #%d: ", times+1);
		scanf("%d%d", &n, &m);
		for (int i=0; i<n; i++) {
			gets(s);
			for (int j=0; j<m; j++) ch[i][j] = getchar();
		}
		memset(l, false, sizeof(l));
		memset(r, false, sizeof(r));
		memset(u, false, sizeof(u));
		memset(d, false, sizeof(d));
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++)
				if (ch[i][j] != '.') {
					l[i][j] = true;
					break;
				}
			for (int j=m-1; j>=0; j--)
				if (ch[i][j] != '.') {
					r[i][j] = true;
					break;
				}
		}
		for (int j=0; j<m; j++) {
			for (int i=0; i<n; i++)
				if (ch[i][j] !='.') {
					u[i][j] = true;
					break;
				}
			for (int i=n-1; i>=0; i--)
				if (ch[i][j] != '.') {
					d[i][j] = true;
					break;
				}
		}
		
		bool flag = true;
		int ans = 0;
		for (int i=0; i<n; i++) {
			if (!flag) break;
			for (int j=0; j<m; j++)
				if (ch[i][j] != '.') {
					if (l[i][j] && r[i][j] && u[i][j] && d[i][j]) {
						flag = false;
						break;
					}
					if (l[i][j] && ch[i][j] == '<') ans ++;
					else if (r[i][j] && ch[i][j] == '>') ans ++;
					else if (u[i][j] && ch[i][j] == '^') ans ++;
					else if (d[i][j] && ch[i][j] == 'v') ans ++;
				}
		}
		if (!flag) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}

