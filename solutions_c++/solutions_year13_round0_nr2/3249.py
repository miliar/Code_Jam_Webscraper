#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_SZ 100

unsigned int N, M, lawn[MAX_SZ][MAX_SZ], lawn_aux[MAX_SZ][MAX_SZ];

void rotate() {
	memcpy(lawn_aux, lawn, sizeof(lawn));
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			lawn[j][i] = lawn_aux[i][j];
	unsigned t = N;
	N = M;
	M = t;
};



int solve(int ctry){
	scanf("%u %u", &N, &M);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			scanf("%u", &lawn[i][j]);

	bool rez = true;
	for (int rot = 0; rez && rot < 4; rotate(),rot++) {
		for (int i = 0; i < N; i++) {	// on each horizontal line
			int mx = lawn[i][0];
			for (int j = 1; j < M; j++)
				if (lawn[i][j] > mx)
					mx = lawn[i][j];
			for (int j = 0; j < M; j++)	
				if (mx > lawn[i][j]) { // if a value is smaller than the max of the current horizontal line, then it should have been cut by a vertical pass
					for (int t = 0; t < N; t++)	// there should be no values larger !
						if (lawn[t][j] > lawn[i][j])
							rez = false;
				};
		};
	};
	printf("Case #%d: %s\n", ctry, rez?"YES":"NO");
};


int main(){

	if (freopen("test.in", "rt", stdin)){
//		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("B-small-attempt1.in", "rt", stdin)){
		freopen("B-small-attempt1.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("B-large.in", "rt", stdin)){
		freopen("B-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};