#include<stdio.h>

int A[128][128], B[128][128];
int T, TT, R, C;

int main() {
	scanf("%d", &TT);
	for(int T = 1; T <= TT; ++T) {
		scanf("%d %d", &R, &C);
		for(int i = 0; i < R; ++i)
			for(int j = 0; j < C; ++j)
				scanf("%d", &A[i][j]);
		for(int i = 0; i < R; ++i)
			for(int j = 0; j < C; ++j)
				B[i][j] = 100;
		for(int i = 0; i < R; ++i) {
			int mx = -1;
			for(int j = 0; j < C; ++j)
				if(A[i][j] > mx) mx = A[i][j];
			for(int j = 0; j < C; ++j)
				if(mx < B[i][j]) B[i][j] = mx;
		}
		for(int i = 0; i < C; ++i) {
			int mx = -1;
			for(int j = 0; j < R; ++j)
				if(A[j][i] > mx) mx = A[j][i];
			for(int j = 0; j < R; ++j)
				if(mx < B[j][i]) B[j][i] = mx;
		}
		bool ok = true;
		for(int i = 0; i < R; ++i)
			for(int j = 0; j < C; ++j)
				if(A[i][j] != B[i][j]) ok = false;
		printf("Case #%d: ", T);
		puts(ok?"YES":"NO");
	}
}
