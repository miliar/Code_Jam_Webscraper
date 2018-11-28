#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


bool is_palin_s(char* s) {
	char* e = s + strlen(s) - 1;
	while (s < e) {
		if (*s != *e)
			return false;
		s++;
		e--;
	};
	return true;
};


bool is_palin_n(long long int n) {
	char s[32];
	sprintf(s, "%I64d", n);
	return is_palin_s(s);
};



int solve(int ctry){
	long long int A, B;
	scanf("%I64d %I64d", &A, &B);
	int rez = 0;
	int A1 = (int)floor(sqrt((double)A));
	int B1 = (int)ceil(sqrt((double)B));
	for (int i = A1; i <= B1; i++) {
		if (is_palin_n(i)) {
			long long int isq = i;
			isq *= isq;
			if (isq >= A && isq <= B && is_palin_n(isq))
				rez++;
		};
	};
//	printf("Case #%d: is palin : %d %d\n", ctry, is_palin_n(A), is_palin_n(B));
	printf("Case #%d: %d\n", ctry, rez);
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
	if (freopen("C-small-attempt0.in", "rt", stdin)){
		freopen("C-small-attempt0.out", "wt", stdout);
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