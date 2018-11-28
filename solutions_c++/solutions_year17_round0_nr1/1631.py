// Lupus Nocawy
// 2017-04-08
// Google Code Jam
// Qualification Round 2017
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/3264486/dashboard
// Problem A. Oversized Pancake Flipper

#include <cstdio>
#include <cstring>
using namespace std;

void inline flip(char &c){
	c = '+'+'-' - c;
}

void flipK(char *s, int k){
	while(k--){
		flip(*s);
		s++;
	}
}

int solve(int c){
	char S[1001];
	int K;
	scanf("%s %d ", S, &K);
	int len = strlen(S);
	int flips = 0;
	// Start at the front and flip at each occurence of '-', until you can't flip more
	// It should work, because each '-' has to be flipped, and flipping anything to the left is pointless.
	for(int i=0; i < len - (K-1); ++i){
		if(S[i]=='-'){
			flipK(S+i,K);
			flips++;
		}
	}
	// check if the whole string is correctly flipped (all chars are ++++)
	for(int i=len-K; i<len; ++i){
		if(S[i]=='-')
			return -1;
		}
		return flips;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		int result = solve(c);
		if(result == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", result);
	}
	return 0;
}
