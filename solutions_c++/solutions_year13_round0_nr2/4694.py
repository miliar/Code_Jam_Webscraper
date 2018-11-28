#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
int n, m;
int i, j, k;
int x, y;
int t;
int T, cas;
int p, q;
int a[111][111];
bool ff;
bool yes[111][111];
bool ans;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &T);
	while (T--){
		scanf("%d%d", &n, &m);
		memset(yes, 0, sizeof yes);
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				scanf("%d", &a[i][j]);
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++){
				ff = true;
				for (k = 1; k <= n; k++)
					ff &= a[k][j] <= a[i][j];
				yes[i][j] |= ff;
				ff = true;
				for (k = 1; k <= m; k++)
					ff &= a[i][k] <= a[i][j];
				yes[i][j] |= ff;
			}
		ans = true;
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				ans &= yes[i][j];
		printf("Case #%d: ", ++cas);
		puts(ans ? "YES" : "NO");
	}
}
