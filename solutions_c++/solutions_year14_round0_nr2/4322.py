#include <stdlib.h>
#include <stdio.h>

int solve(int ctry){
	double C, F, X, best_time, last_time, gain = 2.0d, T = 0.0d;
	scanf("%lf %lf %lf", &C, &F, &X);

	last_time = best_time = X / gain;
	do {
		best_time = last_time;
		T += C / gain;	// how long it will take to buy the next farm
		gain += F;		// higher gain because of additional farm
		last_time = T + X / gain;	// and when we'll reach the goal with it
	} while (last_time < best_time);
	
	printf("Case #%d: %0.7f\n", ctry, best_time);
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
	if (freopen("B-large.in", "rt", stdin)){
		freopen("B-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-large-practice.in", "rt", stdin)){
		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};