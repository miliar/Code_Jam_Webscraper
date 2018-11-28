#include<stdio.h>
#include<stdlib.h>
#include<string.h>
long long int testcase, a, b = 1;
char s[10000];
int main(){
	FILE *f, *z;
	f = fopen("A-large.in", "r");
	z = fopen("output.txt", "w");
	fscanf(f, "%lld", &testcase);
	while (testcase--){
		long long int count = 0, number = 0;
		fscanf(f, "%d %s", &a, s);
		long long int temp = strlen(s);
		for (long long int i = 0; i < temp; i++){
			number += s[i] - '0';
			if (number <= i + 1){
				count += i + 1 - number;
				number = i + 1;
			}
		}
		fprintf(z, "Case #%lld: %lld\n", b++, count);
	}
	fclose(f);
	fclose(z);
}