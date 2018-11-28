#include <cstdio>
#include <cstring>
#include <algorithm>

int N, M;
int A[100][100];
int Rmax[100];
int Cmax[100];

bool calc() {
	for (int i = 0; i < N; ++ i)
		for (int j = 0; j < M; ++ j)
			if (A[i][j] != std::min(Rmax[i], Cmax[j]))
				return false;
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tcase = 0; tcase < T; ++ tcase) {
		scanf("%d%d", &N, &M);
		memset(Rmax, 0, sizeof(Rmax));
		memset(Cmax, 0, sizeof(Cmax));
		for (int i = 0; i < N; ++ i)
			for (int j = 0; j < M; ++ j) {
				scanf("%d", &A[i][j]);
				if (Rmax[i] < A[i][j]) Rmax[i] = A[i][j];
				if (Cmax[j] < A[i][j]) Cmax[j] = A[i][j];
			}
		printf("Case #%d: %s\n", tcase+1, calc()?"YES":"NO");
	}
	return 0;
}
