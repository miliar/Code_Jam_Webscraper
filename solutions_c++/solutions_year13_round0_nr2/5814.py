#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int N, M;
int A[200][200];
int row[200], col[200];

int main() {
	int TT;
	freopen("B.in", "r", stdin);
	scanf("%d", &TT);
	
	for (int _ = 1;_ <= TT;_ ++) {
		printf("Case #%d: ", _);
		scanf("%d%d", &N, &M);
		for (int i = 0;i < N;i++) {
			for (int j = 0;j < M;j++) {
				scanf("%d", &A[i][j]);
			}
		}
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));
		for (int i = 0;i < N;i++) {
			for (int j = 0;j < M;j++) {
				row[i] = max(row[i], A[i][j]);
				col[j] = max(col[j], A[i][j]);
			}
		}
		for (int i = 0;i < N;i++) {
			for (int j = 0;j < M;j++) {
				if (A[i][j] != min(row[i], col[j]))
				{
					puts("NO");
					goto DIE;
				}
			}
		}
		puts("YES");
DIE:		;
	}

	return 0;
}
