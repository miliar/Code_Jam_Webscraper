#include <cstdio>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int R,C,M;
int stx,sty;
int fail;
int cell[10][10];
int done[6][6],cnt[6][6];
int fr,bk;
pair<int,int> que[100];

inline bool ok(int x, int y){
	if (cell[x][y] == 1)
		return false;
	int v=1;
	memset(done,0,sizeof(done));
	fr = bk = 0;
	que[bk++] = make_pair(x,y);
	done[x][y] = 1;
	while (fr<bk){
		int nx = que[fr].first;
		int ny = que[fr].second;
		fr++;
		if (cnt[nx][ny] == 0){
			for (int px=-1; px<=1; px++){
				for (int py=-1; py<=1; py++){
					int tx = nx + px;
					int ty = ny + py;
					if (tx<1 || tx>R || ty<1 || ty>C)
						continue;
					if (cell[tx][ty] || done[tx][ty])
						continue;
					que[bk++] = make_pair(tx,ty);
					done[tx][ty] = 1;
					v++;
				}
			}
		}
	}
	return v == R*C-M;
}
inline void check(){
	for (int i=1; i<=R; i++){
		for (int j=1; j<=C; j++){
			cnt[i][j] = 0;
			if (cell[i][j] != 1){
				for (int px = -1; px<=1; px++){
					for (int py = -1; py<=1; py++){
						int nx= i + px;
						int ny = j + py;
						if (nx < 1 || nx > R || ny < 1 || ny > C)
							continue;
						if (cell[nx][ny])
							cnt[i][j]++;
					}
				}
			}
		//	printf("%d ", cnt[i][j]);
		}
		//puts("");
	}
	for (int i=1; i<=R; i++){
		for (int j=1; j<=C; j++){
			if (ok(i,j)){
				stx = i;
				sty = j;
				fail = 0;
				return ;
			}
		}
	}
}
void f(int curR, int curC, int curM){
	if (curM == 0){
		check();
		return ;
	}
	if (curR > R)
		return ;
	if (C*(R-curR) + C - curC + 1 < curM)
		return ;
	
	if (curM > 0){
		cell[curR][curC] = 1;
		if (curC < C)
			f(curR,curC+1,curM-1);
		else
			f(curR+1,1,curM-1);
		if (!fail)
			return ;
	}

	cell[curR][curC] = 0;
	if (curC < C)
		f(curR,curC+1,curM);
	else
		f(curR+1,1,curM);
	if (!fail)
		return ;
}
void solve(int nT){
	printf("Case #%d:\n", nT);
	scanf("%d%d%d", &R, &C, &M);
	if (R == 1){
		for (int i=0; i<M; i++){
			putchar('*');
		}
		for (int i=M+1; i<C; i++){
			putchar('.');
		}
		
		putchar('c');
		puts("");
		return ;
	} else if (C == 1){
		for (int i=0; i<M; i++){
			putchar('*');
			putchar('\n');
		}
		for (int i=M+1; i<R; i++){
			putchar('.');
			putchar('\n');
		}
		putchar('c');
		putchar('\n');
		return ;
	}
	fail = 1;
	memset(cell,0,sizeof(cell));
	f(1,1,M);
	if (fail){
		puts("Impossible");
	} else {
		for (int i=1; i<=R; i++){
			for (int j=1; j<=C; j++){
				if (stx == i && sty == j)
					putchar('c');
				else if (cell[i][j] == 0)
					putchar('.');
				else
					putchar('*');
			}
			puts("");
		}
	}
}

int main(){
	int nT;
	scanf("%d", &nT);
	for (int i=1;i <=nT; i++)
		solve(i);
	return 0;
}