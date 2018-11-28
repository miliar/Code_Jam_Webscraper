#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string.h>
#include <queue>
#define PII pair<int, int>
#define MP make_pair
#define x first
#define y second

using namespace std;

queue<PII> Q;
int R, C, M;
int ok;
int h[10][10], ans[10][10], hh[10][10];
const int x[8] = {0, 0, 1, 1, 1, -1, -1, -1};
const int y[8] = {1, -1,0, 1, -1, 0, 1, -1};

bool Inside(PII x){
	return (x.x >= 0 && x.x < R && x.y >= 0 && x.y < C);
}

bool isok(int i, int j){
	for (int k = 0; k < 8; k ++){
		if (Inside(MP(i + x[k], j + y[k])) && 	
			h[i + x[k]][j + y[k]])
			return 0;
	}
	return 1;
}

int Ans[10];
int vis[10][10];

void dfs(int curR, int curM){
	if (curR == R){
		if (curM != 0) return ;
		memset(hh, 0, sizeof(hh));
		for (int i = 0; i < R; i ++)	
			for (int j = 0; j < C; j ++)
				if (isok(i, j) && !h[i][j]) hh[i][j] = 1;
		while (!Q.empty()) Q.pop();
		if (hh[R - 1][C - 1] == 0){
			if (R * C - M == 1){
				ok = 1; return ;	
			}
			return ;
		}
		int S = 1;
		Q.push(PII(R - 1, C - 1));
		hh[R - 1][C - 1] = 0;
		memset(vis, 0, sizeof(vis));
		vis[R - 1][C - 1] = 1;
		while (!Q.empty()){
			PII cur = Q.front();
			for (int i = 0; i < 8; i ++){
				PII nxt;	
				nxt.x = cur.x + x[i];
				nxt.y = cur.y + y[i];
				if (Inside(nxt)){
					if (hh[nxt.x][nxt.y]){
						Q.push(nxt);
						S ++;
						hh[nxt.x][nxt.y] = 0;
						vis[nxt.x][nxt.y] = 1;
					}
					else 
						if (!h[nxt.x][nxt.y] && !vis[nxt.x][nxt.y]){
							vis[nxt.x][nxt.y] = 1;
							S ++;
						} 
				}
			}
			Q.pop();	
		}
		if (S == R * C - M) {
			ok = 1; 
					return;
		}
	}else{
		for (int i = 0; i <= min(C, curM); i ++){
			if (curR == R - 1 && i == C) break;
			for (int j = 0; j < i; j ++)
				h[curR][j] = 1;
			Ans[curR] = i;
			dfs(curR + 1, curM - i);
			if (ok){
				return;
			}
			for (int j = 0; j < i; j ++)
				h[curR][j] = 0;
		}	
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i ++){
		scanf("%d %d %d", &R, &C, &M);
		memset(h, 0, sizeof(h));
		ok = 0;
		dfs(0, M);
		printf("Case #%d:\n", i + 1);

		if (ok) for (int j = 0; j < R; j ++){
					for (int k = 0; k < C; k ++)
						if (h[j][k])
							printf("*");
						else{
							if (j == R - 1 && k == C - 1)	
								printf("c");
							else printf(".");
						}
					printf("\n");
				}
		else printf("Impossible\n");
	}
}

