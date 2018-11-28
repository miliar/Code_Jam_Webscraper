/*
 * main.cpp
 *
 *  Created on: Apr 27, 2013
 *      Author: hodovan
 */

#include <stdio.h>
#include <fstream>

FILE *in;
FILE *out;

void solveTest(int i)
{
	fprintf(out, "Case #%d: ", (i + 1));
	long long r, t;
	fscanf(in, "%lld %lld\n", &r, &t);

	long long curr_r = r + 1;
	long long prev_r = r;
	int circles = 0;
	while (t > 0) {
		t -= (curr_r * curr_r - prev_r * prev_r);
		if (t >= 0)
			circles++;
		curr_r += 2;
		prev_r += 2;
	}
	fprintf(out, "%lld\n", circles);
}

int main() {
	in = fopen("A-small-attempt0.in", "r");
	out = fopen("output.txt", "w");

	int T = 0;
	fscanf(in, "%d\n", &T);

	for (int i = 0; i < T; ++i)
		solveTest(i);

	fclose(in);
	fclose(out);
}



