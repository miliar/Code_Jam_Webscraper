#include <cstdio>
const int N = 110, aa[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int T, n, m, a[N][N];
char s[N][N];
bool check(int x, int y, int z){
	//printf("___%d %d %d\n", x, y, z);
	for (; ; ){
		x += aa[z][0];
		y += aa[z][1];
		//printf("%d %d\n", x, y);
		if (x <= 0 || y <= 0 || x > n || y > m) return false;
		if (a[x][y] >= 0) return true;
	}
}
int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti){
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i) scanf("%s", &s[i][1]);
		for (int i = 1; i <= n; ++i){
			for (int j = 1; j <= m; ++j){
				if (s[i][j] == '<') a[i][j] = 3;
				else if (s[i][j] == '>') a[i][j] = 1;
				else if (s[i][j] == '^') a[i][j] = 2;
				else if (s[i][j] == 'v') a[i][j] = 0;
				else a[i][j] = -1;
				//printf("%d ", a[i][j]);
			}
			//printf("\n");
		}
		bool bo = true;
		int ans = 0;
		for (int i = 1; i <= n; ++i){
			for (int j = 1; j <= m; ++j) if (a[i][j] >= 0){
				if (!check(i, j, a[i][j])){
					bool succ = false;
					for (int k = 0; k < 4; ++k) if (check(i, j, k)){
						succ = true;
						break;
					}
					if (!succ){
						bo = false;
						break;
					}
					else ++ans;
				}
			}
			if (!bo) break;
		}
		printf("Case #%d: ", Ti);
		if (bo) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
