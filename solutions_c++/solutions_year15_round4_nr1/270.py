#include<cstdio>

const int go[4][2] = {0, 1, 1, 0, 0, -1, -1, 0};

int T, n, m;
char g[111][111];

int chk(int x, int y, char ch) {
	int dir;
	if(ch == '>') dir = 0;
	else if(ch == 'v') dir = 1;
	else if(ch == '<') dir = 2;
	else dir = 3;
	int xx = x+go[dir][0], yy = y + go[dir][1];
	while(xx>=0 && xx < n && yy>=0 && yy<m) {
		if(g[xx][yy] != '.') return 0;
		xx += go[dir][0];yy+=go[dir][1];
	}
	
	for(int dir = 0;dir < 4; dir ++) {
		xx = x+go[dir][0], yy = y + go[dir][1];
		while(xx>=0 && xx < n && yy>=0 && yy<m) {
			if(g[xx][yy] != '.') return 1;
			xx += go[dir][0];yy+=go[dir][1];
		}
	}
	
	return -1;
}

int main() {
	scanf("%d", &T);
	for(int _=1; _<=T; _++) {
		printf("Case #%d: ", _);
		int ans = 0;
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++) scanf("%s", g[i]);
		for(int i=0;i<n && ans >= 0;i++)
			for(int j=0;j<m && ans >= 0;j++)
				if(g[i][j] != '.') {
					int t = chk(i, j, g[i][j]);
					if(t<0) ans = -1;
					else ans += t;
				}
		if(ans<0) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	
	return 0;
}