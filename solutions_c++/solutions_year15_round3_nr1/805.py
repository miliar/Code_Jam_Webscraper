#include <cstdio>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out", "w");
	int TC;
	fscanf(fin, "%d", &TC);
	for (int TestCase = 1; TestCase <= TC; TestCase++) {
		int R, C, W;
		fscanf(fin, "%d %d %d", &R, &C, &W);
		int turn = 0;
		turn = (C / W) * R;
		turn += W - 1;
		if (C % W != 0) turn++;
		fprintf(fout, "Case #%d: %d\n", TestCase, turn);
	}
	return 0;
}