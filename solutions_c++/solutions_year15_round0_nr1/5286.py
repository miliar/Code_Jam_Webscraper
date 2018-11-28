#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

char num;
int T, N, i, j, totalPeople = 0, extra = 0;

int main() {
	FILE* in = fopen("input.txt", "r");
	FILE* out = fopen("output.txt", "w");
	fscanf(in, "%d", &T);

	for (i = 0; i < T; i++) {
		extra = 0;
		totalPeople = 0;
		fscanf(in, "%d", &N);
		fscanf(in, "%c", &num);
		for (j = 0; j <= N; j++) {
			fscanf(in, "%c", &num);
			int numPeople = num - '0';
			if (totalPeople < j) {
				extra += j - totalPeople;
				totalPeople += j - totalPeople;
			}
			totalPeople += numPeople;
		}
		fprintf(out, "Case #%d: %d\n", i+1, extra);
	}

	fclose(in);
	fclose(out);

	return 0;
}