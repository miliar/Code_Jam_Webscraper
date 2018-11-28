#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

enum {CHEAT, BAD, NO};
unsigned setBits(unsigned x){
	unsigned ret;
	ret = 1 << (x - 1);
	return ret;
}

unsigned countBits(unsigned x){
	unsigned i = 0u, mask = 1u, len = sizeof(unsigned)<<3, j;
	for (j = 0; j < len; ++j){
		if ((x&mask) != 0){
			++i;
		}
		mask <<= 1;
	}
	return i;
}

void print(FILE *f, unsigned ans, unsigned flag, int caseno){
	unsigned mask = 1u, i = 1;
	fprintf(f, "Case #%d: ", caseno + 1);
	if (flag == BAD){
		fprintf(f, "Bad magician!\n");
	}
	else if (flag == CHEAT){
		fprintf(f, "Volunteer cheated!\n");
	}
	else{
		while (!(mask&ans)){
			i++;
			mask <<= 1;
		}
		fprintf(f, "%d\n", i);
	}
}

int main(){
	unsigned a[4][4], b[4][4];
	unsigned n1, n2, ans, flag, bits;
	int T, i, a1, a2, j, k;
	FILE *f, *g;
	f = fopen("A-small-attempt0.in", "r");
	g = fopen("A-small-attempt0.out", "w");
	fscanf(f, "%d", &T);
	for (i = 0; i < T; ++i){
		n1 = n2 = 0u;
		fscanf(f, "%d", &a1);
		for (j = 0; j < 4; ++j){
			for (k = 0; k < 4; ++k){
				fscanf(f, "%d", &a[j][k]);
			}
		}
		fscanf(f, "%d", &a2);
		for (j = 0; j < 4; ++j){
			for (k = 0; k < 4; ++k){
				fscanf(f, "%d", &b[j][k]);
			}
		}
		for (j = 0; j < 4; ++j){
			n1 |= setBits(a[a1 - 1][j]);
			n2 |= setBits(b[a2 - 1][j]);
		}
		ans = n1 & n2;
		bits = countBits(ans);
		if (bits == 0){
			flag = CHEAT;
		}
		else if (bits == 1){
			flag = NO;
		}
		else{
			flag = BAD;
		}
		print(g, ans, flag, i);

	}
	fclose(f);
	fclose(g);
	return 0;
}