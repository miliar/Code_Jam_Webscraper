/*
Problem
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 ¡¿ N, 3 ¡¿ N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.
Bleatrix must start with N and must always name (i + 1) ¡¿ N directly after i ¡¿ N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:
N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.
Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.
Limits
1 ¡Â T ¡Â 100.

Small dataset
0 ¡Â N ¡Â 200.
Large dataset
0 ¡Â N ¡Â 106.

Sample
5
0
1
2
11
1692

Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076
*/

#include <stdio.h>
#define INT_MAX 2147483647

bool digits[10];

void check_digit(int n) {
	while (n) {
		digits[n % 10] = true;
		n /= 10;
	}
}

bool can_sleep() {
	for (int i = 0; i < 10; i++)
		if (digits[i] == false) return false;

	return true;
}

int main()
{
	FILE *in, *out;
	in = fopen("A-large.in", "r");
	out = fopen("A-large.out", "w");

	if (!in || !out) return 1;

	int N, T;
	int testcase;
	int n;

	fscanf(in, "%d ", &T);
	//fprintf(out, "Test Case : %d\n", T);
	for (testcase = 1; testcase <= T; testcase++) {
		// -------------------------------------------------- //
		// input
		// -------------------------------------------------- //
		fscanf(in, "%d", &N);
		if (N == 0) {
			fprintf(out, "Case #%d: INSOMNIA\n", testcase);
			continue;
		}
		n = 0;
		// -------------------------------------------------- //
		// start here
		// -------------------------------------------------- //
		for (int i = 0; i < 10; i++) digits[i] = false;
		while (n < INT_MAX) {
			n += N;
			check_digit(n);
			if (can_sleep()) break;
		}

		// -------------------------------------------------- //
		// output
		// -------------------------------------------------- //
		fprintf(out, "Case #%d: %d\n", testcase, n);
	}

	fclose(in);
	fclose(out);
	return 0;
}