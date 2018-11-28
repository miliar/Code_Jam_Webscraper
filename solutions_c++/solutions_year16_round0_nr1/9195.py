#include <stdlib.h>
#include <stdio.h>

int solve(int ctry){
	unsigned int n, r = 0;
	scanf("%u", &n);
	int used = 0, lim = 100;
	
	for (r = n; used != 0x3FF; r+=n) {
		for (int t = r; t; t /= 10) 
			used |= 1 << (t % 10);
		lim--;
		if (!lim)
			break;
	};
	if (!lim)
		printf("Case #%d: INSOMNIA\n", ctry);
	else
		printf("Case #%d: %d\n", ctry, r - n);

	return 0;
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