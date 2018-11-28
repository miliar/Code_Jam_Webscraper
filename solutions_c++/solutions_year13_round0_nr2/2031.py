#include <cstdio>
#define N 100

int n, m;
int T[N][N];
int M_COL[N];
int M_ROW[N];

int main() {

	
	int t, n, m;

	scanf("%d", &t);

	for (int z = 1; z <= t; ++ z) {

	scanf("%d%d", &n, &m);

	for (int i = 0; i < n; ++ i) 
		for (int j = 0; j < m; ++ j) {
			scanf("%d", &T[i][j]);
		}

	for (int i = 0; i < n; ++ i) {
		M_ROW[i] = T[i][0];
		for (int j = 1; j < m; ++ j) 
			if (M_ROW[i] < T[i][j]) {
				M_ROW[i] = T[i][j];
			}				
	}
	
	for (int j = 0; j < m; ++ j) {
		M_COL[j] = T[0][j];
		for (int i = 1; i < n; ++ i) 
			if (M_COL[j] < T[i][j]) {
				M_COL[j] = T[i][j];
			}				
	}
/*	
	for (int i = 0; i < n; ++ i) {
	    printf("%d ", M_ROW[i]);
	}
	printf("\n");
	for (int j = 0; j < m; ++ j) {
	    printf("%d ", M_COL[j]);
	}
	*/
	bool feasible = true;
	for (int i = 0; i < n; ++ i) 
		for (int j = 0; j < m; ++ j) {
			if (T[i][j] < M_ROW[i] && T[i][j] < M_COL[j]) {
				feasible = false;
				break;
			}
		}
	printf("Case #%d: ", z);
	if (feasible) {
		printf("YES\n");	
	} else {
		printf("NO\n");
	}
	}
	return 0;
}
