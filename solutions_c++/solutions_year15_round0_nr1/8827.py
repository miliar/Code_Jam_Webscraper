#include<stdio.h>


int main(){
	FILE *infile = fopen("E:\\1.in", "r");
	FILE *outfile = fopen("E:\\1.out", "w");
	long long n;
	long long sm;
	char str[1005];
	fscanf(infile,"%lld", &n);
	for (long long i = 1; i <= n; ++i){
		fscanf(infile, "%lld",&sm);
		long long need = 0;
		fscanf(infile,"%s", str);
		int last = str[0] - '0';
		for (long long j = 1; j <= sm; ++j){
			if (last < j){
				long long k = j - last;
				need += k;
				last += k;
			}
			last  += str[j] - '0';
		}
		fprintf(outfile, "Case #%lld: %lld\n", i, need);
	}
	fclose(infile);
	fclose(outfile);
	return 0;
}