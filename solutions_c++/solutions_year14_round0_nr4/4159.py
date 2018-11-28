#include <stdlib.h>
#include <stdio.h>

void sort(double* d, int n) {
	for (int i = 0; i < n-1; i++)
		for (int j = i+1; j < n; j++) 
			if (d[i] > d[j]) {
				double t = d[i];
				d[i] = d[j];
				d[j] = t;
			};
};


int get_score(double *d1, double* d2, int N) {
	int i = 0, K_pos = 0, score = 0;
	for (i = 0; i < N; i++) {	// picking blocks in ascending order, and finding Ken's response
		while (d1[i] > d2[K_pos]) // skipping all smaller
			K_pos++;
		if (K_pos == N)	// not a real block! everything from the current to the end is ok
			return score;
		K_pos++;	// and consuming it
		score++;
	};
	return score;
};

int solve(int ctry){
	int N = 0;
	double naomi[1001], ken[1001];
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%lf", naomi + i);
	for (int i = 0; i < N; i++)
		scanf("%lf", ken + i);
	sort(naomi, N);
	sort(ken, N);
	naomi[N] = ken[N] = 1.0d;	// santinel
/*	for (int i = 0; i < N; i++)
		printf("%0.3f ", naomi[i]);
	printf("\n");
	for (int i = 0; i < N; i++)
		printf("%0.3f ", ken[i]);
	printf("\n");	*/
	
/*	// score at simple war
	int normal_score = 0;
	int i = 0, K_pos = 0;
	for (i = 0; i < N; i++) {	// picking blocks in ascending order, and finding Ken's response
		while (naomi[i] > ken[K_pos])	// skipping all smaller
			K_pos++;
		K_pos++;	// and consuming it
		if (K_pos == N)
			break;
	};
	int score_WAR = N - i = 1;
*/

	int score_WAR = N - get_score(naomi, ken, N);
	int score_DWAR = get_score(ken, naomi, N);
	
	printf("Case #%d: %d %d\n", ctry, score_DWAR, score_WAR);
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
	if (freopen("D-small-attempt0.in", "rt", stdin)){
		freopen("D-small-attempt0.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("D-large.in", "rt", stdin)){
		freopen("D-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};