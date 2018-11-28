#include <cstdio>
#include <algorithm>

int T, N, M;
int row[200], col[200], a[200][200];

bool isValid() {
	for (int i=0; i<N; ++i)
		for (int j=0; j<M; ++j)
			if (a[i][j] != std::min(row[i], col[j])) return false;
	return true;
}

int main() {
	scanf("%d", &T);
	for (int t=0; t<T; ++t){
		scanf("%d%d", &N, &M);
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));

		for (int i=0; i<N; ++i) 
			for (int j=0; j<M; ++j) {
				scanf("%d", &a[i][j]);
				if (row[i] < a[i][j]) row[i] = a[i][j];
				if (col[j] < a[i][j]) col[j] = a[i][j];
			}

		printf("Case #%d: ", t+1);
		if (isValid())
			printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
