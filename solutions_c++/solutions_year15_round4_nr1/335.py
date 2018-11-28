#include <cstdio>
#include <map>

using std::map;

const int N = 233;

const int fx[] = {-1, 0, 0, 1}, fy[] = {0, -1, 1, 0};

int n, m;
char graph[N][N];
map<char, int> dict;

bool in_range(int x, int y){
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool have(int x, int y, int f){
	x += fx[f];
	y += fy[f];
	while(in_range(x, y)){
		if (graph[x][y] != '.') return true;
		x += fx[f];
		y += fy[f];
	}
	return false;
}

int main(){
	dict['^'] = 0;
	dict['<'] = 1;
	dict['>'] = 2;
	dict['v'] = 3;
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++){
			scanf("%s", graph[i]);
		}
		bool can = true;
		int ans = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if (graph[i][j] == '.') continue;
				if (have(i, j, dict[graph[i][j]])) continue;
				bool ok = false;
				for(int k = 0; k < 4; k++){
					if (have(i, j, k)) ok = true;
				}
				if (!ok) can = false;
				else ans++;
			}
		}
		if (!can) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
