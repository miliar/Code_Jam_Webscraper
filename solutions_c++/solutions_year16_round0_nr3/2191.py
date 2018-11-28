#include <iostream>
#include <stdio.h>

using namespace std;

long long isPrime(long long n) {
	if (n<2 || (!(n&1) && n != 2))
		return 2;
	for (long long i = 3; i*i <= n; i += 2) {
		if (!(n%i))
			return i;
	}
	return 0;
}
long long base(long long a, int b) {
	long long res = 0;
	long long bs = 1;
	for (int i = 0; i < 16; i++) {
		if (a&(1 << i))
			res = res + bs;
		bs = bs*b;
	}
	return res;
}

long long cal(long long k) {
	int i;
	for (; true; k += 2) {
		for (i = 2; i < 11; i++) {
			if (isPrime(base(k, i))==0)
				break;
		}
		if (i == 11)
			return k;
	}
	return k;
}

int main() {
	FILE *fpi;
	FILE *fpo;
	char k[105];
	int n=50;
	int i = 1;
	fpi = fopen("input.txt", "r");
	//fscanf(fpi, "%d", &n);
	//fgets(k, 104, fpi);
	fpo = fopen("output.txt", "w");
	fprintf(fpo, "Case #1\n");
	long long r = 0x8001;
	while (n--) {
		r = cal(r);
		fprintf(fpo, "%llu", base(r,10));
		for (int i = 2; i <=10; i++) {
			fprintf(fpo, " %llu", isPrime(base(r, i)));
		}
		fprintf(fpo, "\n");
		r = r + 2;
	}
	fclose(fpi);
	fclose(fpo);
	return 0;
}

