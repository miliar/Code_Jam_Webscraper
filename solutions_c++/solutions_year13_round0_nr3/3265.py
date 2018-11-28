#include<stdio.h>
#include<string.h>
#define MAXN 1000

FILE *in;
FILE *out;
int result[5] = {1, 4, 9, 121, 484};

int main(){

	int t, i, test, down, up;
	int final = 0;

	in = fopen("C-small-attempt0.in", "r");
	out = fopen("C-small-attempt0.out", "w");

	fscanf(in, "%d", &t);
	for(test=0 ; test < t ; test++){
		fscanf(in, "%d%d", &down, &up);
		for(i=0 ; i < 5; i++){
			if(result[i] >= down && result[i] <= up)
				final++;
		}
		fprintf(out, "Case #%d: %d\n", test+1, final);
		final = 0;
	}

	return 0;
}