#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

const int N_MAX = 105;
const int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};

int gra[N_MAX][N_MAX];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("pA-large.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int cnt = 1; cnt <= t; cnt++){
		int r, c;
		scanf("%d%d", &r, &c);
		char ipt[N_MAX];
		for(int i = 0; i < r; i++){
			scanf("%s", ipt);
			for(int j = 0; j < c; j++){
				if(ipt[j] == '.')
					gra[i][j] = -1;
				else if(ipt[j] == '^')
					gra[i][j] = 0;
				else if(ipt[j] == 'v')
					gra[i][j] = 1;
				else if(ipt[j] == '<')
					gra[i][j] = 2;
				else if(ipt[j] == '>')
					gra[i][j] = 3;
			}
		}
		int ans = 0;
		bool ok = true;
		for(int i = 0; i < r && ok; i++){
			for(int j = 0; j < c && ok; j++){
				if(gra[i][j] == -1 || gra[i][j] == 100)
					continue;
				int lstx = i, lsty = j, x = i, y = j, vx = dx[gra[i][j]], vy = dy[gra[i][j]];
				bool gg = false;
				while(gra[x][y] != 100){
					if(gra[x][y] != -1){
						vx = dx[gra[x][y]], vy = dy[gra[x][y]];
						gra[x][y] = 100;
						lstx = x, lsty = y;
					}
					x += vx, y += vy;
					if(x < 0 || x >= r || y < 0 || y >= c){
						gg = true;
						break;
					}
				}
				if(gg){
					ans ++;
					gra[lstx][lsty] = -1;
					for(int k = 0; k < 4; k++){
						x = lstx, y = lsty;
						bool ggg = false;
						while(gra[x][y] == -1){
							x += dx[k], y += dy[k];
							if(x < 0 || x >= r || y < 0 || y >= c){
								ggg = true;
								break;
							}
						}
						if(!ggg){
							gra[lstx][lsty] = 100;
							/*for(int ii = 0; ii < r; ii++){
								for(int jj = 0; jj < c; jj++)
									printf("%d", gra[ii][jj]);
								puts("");
							}*/
							break;
						}
					}
					if(gra[lstx][lsty] == -1)
						ok = false;
				}
			}
		}
		printf("Case #%d: ", cnt);
		ok ? printf("%d\n", ans) : puts("IMPOSSIBLE");
	}
	return 0;
}
