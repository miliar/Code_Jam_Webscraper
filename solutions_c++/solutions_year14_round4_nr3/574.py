#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#define N_MAX 510
using namespace std;

bool gra[N_MAX][N_MAX];

int H, W, B;
bool dfs(int vx, int vy, int px, int py){
	if(!gra[px][py]) return false;
	gra[px][py] = false;
	if(py == H) return true;
	swap(vx, vy), vx = -vx;
	if(gra[px + vx][py + vy]){
		if( dfs(vx, vy, px + vx, py + vy) ) return true;
	}
	swap(vx, vy), vy = -vy;
	if(gra[px + vx][py + vy]){
		if( dfs(vx, vy, px + vx, py + vy) ) return true;
	}
	swap(vx, vy), vy = -vy;
	if(gra[px + vx][py + vy]){
		if( dfs(vx, vy, px + vx, py + vy) ) return true;
	}
	return false;
}

void print_map(){
	for(int j = H; j > 0; j--){
		for(int i = 1; i <= W; i++) printf("%d", gra[i][j] ? 1 : 0);
		puts("");
	}
	puts("");
	return;
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cnt = 1; cnt <= T; cnt++){
		printf("Case #%d: ", cnt);
		scanf("%d%d%d", &W, &H, &B);
		memset(gra, false, sizeof(gra));
		for(int i = 1; i <= W; i++){
			for(int j = 1; j <= H; j++) gra[i][j] = true;
		}
		for(int i = 0; i < B; i++){
			int x0, y0, x1, y1;
			scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
			for(int k = x0 + 1; k <= x1 + 1; k++){
				for(int j = y0 + 1; j <= y1 + 1; j++) gra[k][j] = false;
			}
		}
		int ans = 0;
		for(int i = 1; i <= W; i++){
			if(dfs(0, 1, i, 1)) ans++;
		}
		printf("%d\n", ans);
	}
	return 0;
}
