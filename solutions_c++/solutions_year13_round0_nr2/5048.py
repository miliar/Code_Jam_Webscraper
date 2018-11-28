#include <stdio.h>


#define MAX_N	100
#define	MAX_M	100

int main(int argc, char *argv[]) {
	int max_tc, tc = 1;
	int N, M;
	int row_max[MAX_N];	// max height of each row.
	int col_max[MAX_M];	// max height of each col.
	int lawn[MAX_N][MAX_M];

	scanf("%d", &max_tc);
	while(max_tc--) {
		// init data
		bool result = false;
		int max_height = -1;
		for (int i = 0; i < MAX_N; i++)
			row_max[i] = -1;
		for (int i = 0; i < MAX_M; i++)
			col_max[i] = -1;
		scanf("%d %d", &N, &M);

		// get data, 
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				scanf("%d", &lawn[i][j]);
			}
		}
		// find max height of each row and col
		for (int i = 0; i < N; i++) {
			max_height = -1;
			for (int j = 0; j < M; j++) {
				if (lawn[i][j] > max_height)
					max_height = lawn[i][j];
			}
			row_max[i] = max_height;
		}
		for (int i = 0; i < M; i++) {
			max_height = -1;
			for (int j = 0; j < N; j++) {
				if (lawn[j][i] > max_height)
					max_height = lawn[j][i];
			}
			col_max[i] = max_height;
		}

		// check if possible
		result = true;
		for (int i = 0; i < N && result == true; i++) {
			for (int j = 0; j < M && result == true; j++) {
				if (!(lawn[i][j] == row_max[i] || lawn[i][j] == col_max[j]))
					result = false;
			}
		}

		printf("Case #%d: ", tc++);
		if (result)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}