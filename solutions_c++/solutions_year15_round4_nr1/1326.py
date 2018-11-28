#include<cstdio>

char map[110][110];

int dy[4] = {0,0,-1,1};
int dx[4] = {-1,1,0,0};

int main() {
	int T; scanf("%d", &T);
	for(int _ = 0; _ < T; _++) {
		int R, C; scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++)
			scanf(" %s", map[i]);
		bool good = 1;
		int res = 0;
		for(int i = 0; i < R && good; i++)
			for(int j = 0; j < C && good; j++) {
				int rdir;
				switch(map[i][j]) {
					case '.': continue; break;
					case '<': rdir = 0; break;
					case '>': rdir = 1; break;
					case '^': rdir = 2; break;
					case 'v': rdir = 3; break;
				}
				bool vgood = 0;
				bool found = 0;
				for(int dir = 0; dir < 4; dir++) {
					int y = i; int x = j;
					while((y += dy[dir]),(x += dx[dir]), (y>=0 && y < R && x >= 0 && x < C)) {
						if(map[y][x] != '.') {
							found = 1;
							if(dir == rdir) {
								vgood = 1;
								break;
							}
							else
								continue;
						}
					}
				}
				if(!found)
					good = 0;
				else
					if(!vgood)
						res++;
			}
		if(good)
			printf("Case #%d: %d\n", _+1, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", _+1);
	}
	return 0;
}
