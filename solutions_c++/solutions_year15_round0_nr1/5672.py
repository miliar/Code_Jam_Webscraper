#include <cstdio>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out", "w");
	int T;
	fscanf(fin, "%d", &T);
	for (int TestCase = 1; TestCase <= T; TestCase++) {
		int N;
		int human = 0;
		int Result = 0;
		char value[1020];
		fscanf(fin, "%d %s", &N, value);
		for (int i = 0; i <= N; i++) {
			if (human < i) {
				Result += i - human;
				human = i;
			}
			human += value[i] - '0';
		}
		fprintf(fout, "Case #%d: %d\n", TestCase, Result);
	}

	return 0;
}