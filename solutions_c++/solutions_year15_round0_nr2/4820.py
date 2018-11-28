#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)

#define max_inp 1005

void run_test(int test){
	int diners;
	scanf("%d", &diners);
	int p[max_inp];
	for(int n = 0; n < max_inp; ++n)
		p[n] = 0;
	for(int n = 0; n < diners; ++n){
		int num;
		scanf("%d", &num);
		p[num]++;
	}
	
	int moves = 0, sp = max_inp-1, turns;
	if(p[9] == 1){
		p[9]--;
		p[6]++;
		p[3]++;
		moves++;
	}
	while(p[sp] == 0)
		sp--;
	turns = sp+moves;
	while(sp > 1){
		p[sp]--;
		p[(sp+1)/2]++;
		p[sp/2]++;
		while(p[sp] == 0)
			sp--;
		moves++;
		turns = MIN(turns, sp+moves);
	}
	printf("Case #%d: %d\n", test, turns);
}

int main(){
	int tests;
	scanf("%d", &tests);
	for(int n = 0; n < tests; ++n)
		run_test(n+1);
}
