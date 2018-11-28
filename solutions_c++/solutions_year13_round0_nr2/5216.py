#include <stdio.h>

int q[110][110], max_x[110], max_y[110];

FILE *in = fopen("B-large.in", "r");
FILE *out = fopen("B-large.out", "w");

int main(){

	int T;
	fscanf(in, "%d", &T);

	int test;
	
	for (test = 1; test <= T; test++){
	
		int n, m, check = 0;

		fscanf(in, "%d %d", &n, &m);

		int i, j;
		for (i = 1; i <= n; i++){
		
			for (j = 1; j <= m; j++){
			
				fscanf(in, "%d", &q[i][j]);
				if (max_x[i] < q[i][j]) max_x[i] = q[i][j];
				if (max_y[j] < q[i][j]) max_y[j] = q[i][j];
			
			}
		
		}

		for (i = 1; i <= n; i++){
		
			for (j = 1; j <= m; j++){
			
				if (q[i][j] < max_x[i] && q[i][j] < max_y[j]) {check = 1; break;}
			
			}
		
		}
		
		if (check == 1) fprintf(out, "Case #%d: NO\n", test);
		else fprintf(out, "Case #%d: YES\n", test);

		for (i = 1; i <= 103; i++){
			
			max_x[i] = 0;
			max_y[i] = 0;

		}

	}

}