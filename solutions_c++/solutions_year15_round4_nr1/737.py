#include <cstdio>
#include <cstring>

const int MAXN = 105;
const int MAXM = 105;
const int Way[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int ans;
int N, M, T;
char Gr[MAXN][MAXM];

void check(int x, int y){
	if(ans == -1)
		return ;
	int dx, dy;
	if(Gr[x][y] == '^'){
		dx = -1;
		dy = 0;
	} else if(Gr[x][y] == '>'){
		dx = 0;
		dy = 1;
	} else if(Gr[x][y] == 'v'){
		dx = 1;
		dy = 0;
	} else {
		dx = 0;
		dy = -1;
	}
	int nowx = x + dx, nowy = y + dy;
	while(nowx >= 0 && nowx < N && nowy >= 0 && nowy < M && Gr[nowx][nowy] == '.'){
		nowx += dx;
		nowy += dy;
	}
	if(nowx < 0 || nowx >= N || nowy < 0 || nowy >= M)
		ans++;
	else
		return;
	for(int i = 0; i < 4; ++i)
		if(!(Way[i][0] == dx && Way[i][1] == dy)){
			nowx = x + Way[i][0];
			nowy = y + Way[i][1];
			while(nowx >= 0 && nowx < N && nowy >= 0 && nowy < M && Gr[nowx][nowy] == '.'){
				nowx += Way[i][0];
				nowy += Way[i][1];
			}
			if(nowx < 0 || nowx >= N || nowy < 0 || nowy >= M)
				continue;
			return ;
		}
	ans = -1;
	return ;
}

int main(){
	scanf("%d", &T);
	for(int xx = 1; xx <= T; ++xx){
		scanf("%d%d", &N, &M);
		for(int i = 0; i < N; ++i)
			scanf("%s", Gr[i]);
		ans = 0;
		for(int i = 0; i < N; ++i){
			if(ans == -1)
				break;
			for(int j = 0; j < M; ++j)
				if(Gr[i][j] != '.'){
					check(i, j);
					if(ans == -1)
						break;
				}
		}
		printf("Case #%d: ", xx);
		if (ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}
