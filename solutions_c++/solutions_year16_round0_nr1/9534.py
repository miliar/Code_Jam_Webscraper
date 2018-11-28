// Problem A

#include <cstdio>

bool digit[10];
unsigned short digit_count;

void init_digit(){
	for (unsigned short i = 0; i < 10; ++i) digit[i] = 0;
	digit_count = 10;
}

bool check_digit(unsigned short d){
	if (!digit[d]){
		digit_count--;
		digit[d] = true;
		if (!digit_count)
			return true;
	}
	return false;
}

unsigned int check_N(unsigned int &N){
	for (unsigned short i = 1; i <= 100; ++i){
		unsigned int M = N * i;
		while ((M % 10) || (M / 10)){
			if (check_digit(M % 10))
				return N * i;
			M /= 10;
		}
	}
	return -1;
}

int main(){
	FILE *in, *out;
	in = fopen("in", "r");
	out = fopen("out", "w");

	unsigned short T;
	unsigned int N;
	fscanf(in, "%hu", &T);
	for (unsigned short x = 1; x <= T; ++x){
		fscanf(in, "%u", &N);
		init_digit();
		unsigned int y = check_N(N);
		if (y == -1)
			fprintf(out, "Case #%hu: INSOMNIA\n", x);
		else
			fprintf(out, "Case #%hu: %u\n", x, y);
	}
	fclose(out);
	fclose(in);

	return 0;
}