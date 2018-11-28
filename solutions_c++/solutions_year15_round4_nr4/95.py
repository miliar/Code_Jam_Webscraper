#include <cstdio>

const int N = 12;

int n, m;
int v[N][N];
int ans;
int all[1000][N][N];

bool ok(int x, int y){
	int cnt = 0;
	if (x > 0) cnt += (v[x][y] == v[x - 1][y]);
	cnt += (v[x][y] == v[x][(y + m - 1) % m]);
	cnt += (v[x][y] == v[x][(y + 1) % m]);
	cnt += (v[x][y] == v[x + 1][y]);
	return cnt == v[x][y];
}

void dfs(int x, int y){
	if (x == n){
		for(int i = 0; i < m; i++){
			int cnt = 0;
			cnt += (v[n - 1][i] == v[n - 1][(i + m - 1) % m]);
			cnt += (v[n - 1][i] == v[n - 1][(i + 1) % m]);
			cnt += (v[n - 1][i] == v[n - 2][i]);
			if (cnt != v[n - 1][i]) return;
		}
		bool ok = false;
		for(int i = 0; i < ans; i++){
			for(int j = 0; j < m; j++){
				bool wrong = false;
				for(int a = 0; wrong == false && a < n; a++){
					for(int b = 0; wrong == false && b < m; b++){
						if (all[i][a][b] != v[a][(j + b) % m]) wrong = true;
					}
				}
				if (wrong == false) return;
			}
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				all[ans][i][j] = v[i][j];
			}
		}
		ans++;
		return;
	}
	if (y == m){
		dfs(x + 1, 0);
		return;
	}
	if (x == 0 || x == n - 1){
		for(int i = 1; i <= 3; i++){
			v[x][y] = i;
			if (x && !ok(x - 1, y)) continue;
			dfs(x, y + 1);
		}
	}
	else{
		for(int i = 1; i <= 4; i++){
			v[x][y] = i;
			if (x && !ok(x - 1, y)) continue;
			dfs(x, y + 1);
		}
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &m);
		ans = 0;
		dfs(0, 0);
		printf("%d\n", ans);
	}
}
