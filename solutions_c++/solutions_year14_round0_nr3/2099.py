#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define REP(i, N) for(int i = 0; i < (N); i++)

using namespace std;
char res[55][55];
int d[8][2] = {{1,0},{0,1},{-1,0},{0,-1},{1,1},{-1,1},{1,-1},{-1,-1}};;
bool visited[7][7];
int R, C;
int dfs(int r, int c) {
	visited[r][c] = true;
	int X = 0;
	bool cont = true;
	REP(q, 8) {
		int nr = r+d[q][0], nc = c+d[q][1];
		if(nr < 0 || nc < 0 || nr >= R || nc >= C)
			continue;
		if(res[nr][nc] == '*')
			cont = false;
	}
	if(!cont)
		return 1;
	REP(q, 8) {
		int nr = r+d[q][0], nc = c+d[q][1];
		if(nr < 0 || nc < 0 || nr >= R || nc >= C)
			continue;
		if(!visited[nr][nc]) {
			X += dfs(nr, nc);
		}
	}
	return X+1;
}
int main() {
	int T, testcase=1;
	scanf("%d", &T);
	while(T--) {
		REP(i, 55) REP(j, 55) res[i][j] = '.';
		int M;
		scanf("%d%d%d", &R, &C, &M);
		int Q = R*C-M;
		printf("Case #%d:\n", testcase++);
		bool poss = false;
		REP(i, (1<<(R*C))) {
			int bombs = 0;
			REP(j, R*C) if(i&(1<<j)) bombs++;
			if(bombs != M) continue;
			REP(j, R*C) if(i&(1<<j)) {
				res[j/C][j%C] = '*';
			} else res[j/C][j%C] = '.';
			REP(k, R) REP(j, C) if(res[k][j] == '.') {
				REP(x, R) REP(y, C) visited[x][y] = false;
				int reachable = dfs(k, j);
				if(reachable == Q) {
					res[k][j] = 'c';
					REP(x, R) {
						REP(y, C) printf("%c", res[x][y]);
						printf("\n");
					}
					poss = true;
					k = i = 1<<30;
					break;
				}
			}
		}
		if(!poss) printf("Impossible\n");
	}
	
	return 0;
}
