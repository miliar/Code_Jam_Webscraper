#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  

using namespace std; 
typedef long long ll; 
typedef unsigned long long llu; 
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define memset0(x) memset(x, 0, sizeof (x));
int TC, TCC;

int M, R, C, S;
int A[100];
int D[100][100], V[100][100];
const int dx[] = {-1, 0, 1, -1, 1, -1, 0, 1}, dy[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int par[10000];

void init () {
	memset0(A);
	for(int i = 0; i < 10000; i++) par[i] = i;
}

int uf (int x) {
	return par[x] == x ? x : (par[x] = uf(par[x]));
}

void solve () {
	scanf("%d%d%d", &R, &C, &M);
	S = R*C;

	for(int i = 0; i < M; i++) A[i] = 1;
	reverse(A, A+S);


	do {
		for(int i = 0; i < S; i++) D[i/C][i%C] = A[i], par[i] = i;
		
		for(int x = 0; x < R; x++) for(int y = 0; y < C; y++) {
			V[x][y] = 0;
			for(int d = 0; d < 8; d++) {
				int xx = x+dx[d], yy = y+dy[d];
				if(xx < 0 || yy < 0 || xx >= R || yy >= C) continue;
				V[x][y] += D[xx][yy];
			}
		}
		
		for(int x = 0; x < R; x++) for(int y = 0; y < C; y++) if(D[x][y] == 0 && V[x][y] == 0) {
			for(int d = 0; d < 8; d++) {
				int xx = x+dx[d], yy = y+dy[d];
				if(xx < 0 || yy < 0 || xx >= R || yy >= C || D[xx][yy] == 1) continue;
				par[xx*C+yy] = uf(x*C+y);
			}
		}

		bool chk = true; int pp = -1, rx = -1, ry = -1, c = 0;
		for(int x = 0; x < R && chk; x++) for(int y = 0; y < C && chk; y++) if(D[x][y] == 0) {
			int p = uf(x*C+y); ++c;
			if(pp == -1) pp = p; else if(pp != p) chk = false;
			if(rx < 0 && V[x][y] == 0) rx = x, ry = y;
		}

		if(chk && c == S-M && pp != -1) {
			printf("Case #%d:\n", TCC);
			for(int i = 0; i < R; i++) {
				for(int j = 0; j < C; j++) {
					if((rx >= 0 && rx == i && ry == j) || (rx < 0 && pp == i*C+j)) putchar('c');
					else putchar(D[i][j] ? '*' : '.');
				}
				puts("");
			}
			return;
		}
	}while(next_permutation(A, A+S));
	
			printf("Case #%d:\nImpossible\n", TCC);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &TC);
	while(++TCC <= TC) {
		init();
		solve();
	}
	return 0;
}