#include<stdio.h>
int TT, TC, n, m, dir[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} }, P[256];
bool v[110][110];
char p[110][110];
int Danger(int x, int y){
	int dx = dir[P[p[x][y]]][0], dy = dir[P[p[x][y]]][1];
	while (1){
		x += dx, y += dy;
		if (p[x][y] != '.')break;
		if (x >= 1 && x <= n && y >= 1 && y <= m)continue;
		break;
	}
	if (x >= 1 && x <= n && y >= 1 && y <= m)return 0;
	return 1;
}
int main(){
	int i, j, c, ck, Res;
	char t;
	P['^'] = 0;
	P['v'] = 1;
	P['<'] = 2;
	P['>'] = 3;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d%d", &n, &m);
		for (i = 1; i <= n; i++)scanf("%s", p[i] + 1);
		ck = 0;
		Res = 0;
		for (i = 1; i <= n; i++){
			for (j = 1; j <= m; j++){
				if (p[i][j] != '.'){
					if (Danger(i, j)){
						c = 0;
						t = p[i][j];
						p[i][j] = '^';
						c += Danger(i, j);
						p[i][j] = 'v';
						c += Danger(i, j);
						p[i][j] = '>';
						c += Danger(i, j);
						p[i][j] = '<';
						c += Danger(i, j);
						p[i][j] = t;
						if (c == 4)ck = 1;
						Res++;
					}
				}
			}
		}
		if (ck)printf("IMPOSSIBLE\n");
		else printf("%d\n", Res);
	}
}