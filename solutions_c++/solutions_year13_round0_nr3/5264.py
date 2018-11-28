// P3_FairSquare.cpp : Defines the entry point for the console application.
//

//

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <hash_map>
#include <hash_set>

using namespace std;

hash_set<long> pals;

bool isPalin(long long int x) {
	if (pals.find(x) != pals.end())
		return true;
	if (x < 0) return false;
	int div = 1;
	while (x / div >= 10) {
		div *= 10;
	}        
	while (x != 0) {
		int l = x / div;
		int r = x % 10;
		if (l != r) return false;
		x = (x % div) / 10;
		div /= 100;
	}
	pals.insert(x);
	return true;
}

int solve(long long int A, long long int B)
{
	long long int n;
	int s;
	int cnt;

	cnt = 0;
	for (n=A; n<=B; n++) {
		if (isPalin(n)) {
			s = sqrt(n);
			if ((s*s != n) && ((s+1)*(s+1) != n) && ((s-1)*(s-1) != n))
				continue;
			if (isPalin(s)) {
				++cnt;
				printf("%d => %d \n", s, n);
			}
		}
	}

	return cnt;
}

int main(int argc, char* argv[])
{
	FILE *fpi;
	FILE *fpo;
	char line[1025];
	int T;
	long long int A, B;
	int i;

	fpi = fopen("C-small-attempt0.in", "r");
	fpo = fopen("C-small-attempt0.out", "w");;

	fgets(line, 1024, fpi);
	sscanf(line, "%d", &T);

	for (i=0; i<T; i++) {
		fgets(line, 1024, fpi);
		sscanf(line, "%lld %lld", &A, &B);
		fprintf(fpo, "Case #%d: %d\n", i+1, solve(A, B));
	}

	fclose(fpi);
	fclose(fpo);
	return 0;
}

