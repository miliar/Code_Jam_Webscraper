#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

inline char is_palindrome(long x) {
	char digits[32];
	sprintf(digits, "%ld", x);
	int len = strlen(digits);
	for (int i=0; i<len/2; i++) if (digits[i]!=digits[len-1-i]) return 0;
	return 1;
}

int main(int argc, char **argv) {
	if (argc!=3) {
		printf("provide input and output file names as command line parameters\n");
	}
	FILE *fp_in, *fp_out;
	if ((fp_in=fopen(argv[1],"r"))==NULL) { printf("can't open file %s\n", argv[1]); exit(1); }
	if ((fp_out=fopen(argv[2],"w"))==NULL) { printf("can't open file %s\n", argv[2]); exit(1); }
	
	int num_cases;
	fscanf(fp_in, "%d\n", &num_cases);
	
	long A, B;
	long sqrtA, sqrtB, count, test;
	for (int test_case=1; test_case<=num_cases; test_case++) {
		fscanf(fp_in, "%ld %ld\n", &A, &B);
		sqrtA = ceil(sqrt((double)A));
		sqrtB = floor(sqrt((double)B));
		
		count = 0;
		for (test=sqrtA; test<=sqrtB; test++) {
			if (is_palindrome(test) && is_palindrome(test*test)) count++;
		}
		
		fprintf(fp_out, "Case #%d: %ld\n", test_case, count);
	}
	
	
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
