#include <stdlib.h>
#include <stdio.h>
#include <string.h>



char in_S[10002] = {0};
char    S[10002] = {0};

int possible_start_pos[10002] = {0};
int possible_end_pos[10002] = {0};
int possible_start_pos_cnt = 0;
int possible_end_pos_cnt = 0;


char conv_in(char c) {
	switch (c) {
		case 'i':	return 2;
		case 'j':	return 3;
		case 'k':	return 4;
	};
	return 0;
};


char conv_out(char a) {
	switch (a) {
		case  0:	return '0';
		case  1:	return 'P';
		case -1:	return 'M';
		case  2:	return 'i';
		case -2:	return 'I';
		case  3:	return 'j';
		case -3:	return 'J';
		case  4:	return 'k';
		case -4:	return 'K';
	};
	return 'x';
};



inline int sig(char a) {
	return (a < 0) ? 1 : 0;
};


int absd(char a) {
	return (a >= 0) ? a : -a;
};


char lk[5][5] = {
	{0,  0,  0,  0,  0},
	{0,  1,  2,  3,  4},
	{0,  2, -1,  4, -3},
	{0,  3, -4, -1,  2},
	{0,  4,  3, -2, -1}, 
};


char lk_inv[5][5] = {
	{0,  0,  0,  0,  0},
	{0,  1, -2, -3, -4},
	{0, -2,  1, -4,  3},
	{0, -3,  4,  1, -2},
	{0, -4, -3,  2,  1}, 
};




char mul(char a, char b) {
	int s = sig(a) + sig(b);
	a = absd(a);
	b = absd(b);
	char rez = lk[a][b];
	if (s & 1)
		rez *= -1;
	return rez;
};


char div(char a, char b) {
	int s = sig(a) + sig(b);
	a = absd(a);
	b = absd(b);
	char rez = lk_inv[a][b];
	if (s & 1)
		rez *= -1;
	return rez;
};


char mul_range(char* in, int sz, char starting_val = 1) {
	if (sz <= 0)
		return 0;
	char rez = starting_val;
	for (int i = 0; i < sz; i++)
		rez = mul(rez, in[i]);
	return rez;
};




int solve(int ctry){
	memset(S, 0, sizeof(S));
	memset(in_S, 0, sizeof(in_S));

	unsigned int L, X;
	scanf("%u %u\n", &L, &X);
	for (int i = 0; i < L; i++)
		scanf("%c", in_S + i);
	in_S[L] = 0;
	
	for (int i = 0; i < X; i++)
		for (int j = 0; j < L; j++)
			S[i*L + j] = conv_in(in_S[j]);
	in_S[L*X] = 0;

	bool rez = false;
	int size = X * L;
	possible_start_pos_cnt = possible_end_pos_cnt = 0;
	memset(possible_start_pos, 0, sizeof(possible_start_pos));
	memset(possible_end_pos, 0, sizeof(possible_end_pos));
	
	char rez1 = 1;
	for (int i = 0; i < size-2; i++) {
		rez1 = mul(rez1, S[i]);
		if (rez1 == 2) {
			possible_start_pos[possible_start_pos_cnt++] = i + 1;
//			printf("INFO: found possible end position for i: %d\n", i+1);
		};
	};

	char rez2 = 4;
	for (int i = size - 1; i > 1; i--) {
		rez2 = div(rez2, S[i]);
		if (rez2 == 1) {
			possible_end_pos[possible_end_pos_cnt++] = i;
//			printf("INFO: found possible start position for k: %d\n", i);
		};
	};


/*	
	for (int i = 2; i < size; i++) {
		char rez2 = mul_range(S + i, size - i);
		if (rez2 == 4) {
			possible_end_pos[possible_end_pos_cnt++] = i;
//			printf("INFO: found possible start position for k: %d\n", i);
		};
	};	*/
	
/*	for (int i = 0; i < possible_start_pos_cnt; i++) 
		for ( int j = 0; j < possible_end_pos_cnt; j++) {
			if ( (possible_start_pos[i] < possible_end_pos[j]) &&
				(mul_range(S + possible_start_pos[i], possible_end_pos[j] - possible_start_pos[i]) == 3)) {
					rez = true; 
					goto finish;
			};
		};
*/
/*
	for (int i = possible_start_pos_cnt - 1; i >= 0; i--) 
		for ( int j = possible_end_pos_cnt - 1; j >= 0; j--) {
			if ( (possible_start_pos[i] < possible_end_pos[j]) &&
				(mul_range(S + possible_start_pos[i], possible_end_pos[j] - possible_start_pos[i]) == 3)) {
					rez = true; 
					goto finish;
			};
		};
*/		
	for (int i = possible_start_pos_cnt - 1; i >= 0; i--) {
		int curr_pos = possible_start_pos[i];
		char curr_val = 1;
		for ( int j = possible_end_pos_cnt - 1; j >= 0; j--) {	// in ascending order of offsets
			int end_pos = possible_end_pos[j];
			if (curr_pos >= end_pos)	// skipping too early entries
				continue;
			curr_val = mul_range(S + curr_pos, end_pos - curr_pos, curr_val);
			curr_pos = end_pos;
			if (curr_val == 3) {
				rez = true; 
				goto finish;
			};
		};
	};

	
finish:
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
	if (freopen("C-small-attempt2.in", "rt", stdin)){
		freopen("C-small-attempt2.out", "wt", stdout);
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
