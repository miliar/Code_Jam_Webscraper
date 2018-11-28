// Problem B

#include <cstdio>

unsigned short T;
char S[101];

unsigned short filp_pancakes(){
	char prev_p = S[0]; // S length >= 1
	unsigned short flip_count = 0;
	for (unsigned short i = 1; S[i]; ++i){
		if (S[i] != prev_p){
			flip_count++;
			prev_p = S[i];
		}
	}
	if (prev_p == '-') flip_count++;
	return flip_count;
}

int main(){
	FILE *in, *out;
	in = fopen("in", "r");
	out = fopen("out", "w");

	fscanf(in, "%hu", &T);
	for (unsigned short x = 1; x <= T; ++x){
		fscanf(in, "%s", S);
		fprintf(out, "Case #%hu: %hu\n", x, filp_pancakes());
	}
	fclose(out);
	fclose(in);

	return 0;
}