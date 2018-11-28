#include <stdlib.h>
#include <stdio.h>

int max(int a, int b) {
	return (a > b) ? a : b;
};

int s_cnts[1001];

int solve(int ctry){
	unsigned int Smax;
	scanf("%u ", &Smax);
	int needed = 0, found_until_here = 0;
	for (int i = 0; i <= Smax; i++) {
		char c;
		scanf("%c", &c);
		s_cnts[i] = c - '0';
		
		needed = max(needed, i - found_until_here);
		found_until_here += s_cnts[i];
	};
	
	printf("Case #%d: %d\n", ctry, needed);
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
	if (freopen("A-small-attempt0.in", "rt", stdin)){
		freopen("A-small-attempt0.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-large.in", "rt", stdin)){
		freopen("A-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};