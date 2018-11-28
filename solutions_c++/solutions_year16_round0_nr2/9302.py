#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int solve(int ctry){
	char s[110];
	if (ctry == 1)
		fgets(s, 105, stdin);
	fgets(s, 105, stdin);
//	printf("INFO: string is %s\n", s);
	int groups = 0;
	int i = 0;
	for (; (s[i] == '+') || (s[i] == '-') ; i++) 
		if (!i) 
			groups = 1;
		else 
			if (s[i] != s[i-1])
				groups++;
	if (s[i-1] == '+')
		groups--;
	printf("Case #%d: %d\n", ctry, groups);
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
	if (freopen("B-small-attempt0.in", "rt", stdin)){
		freopen("B-small-attempt0.out", "wt", stdout);
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