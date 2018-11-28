
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
#include <functional>
#include <iostream>
#define INF 987654321

using namespace std;

FILE *infile;
FILE *outfile;

int check[10];
int main()
{
	infile = fopen("A-small-attempt0.in", "r+");
	outfile = fopen("outfile.txt", "w+");

	int T; //testcase
	int N;
	int real_N;
	int i = 1;
	int how_check = 0;

	fscanf(infile, "%d", &T);
	for (i = 1; i <= T; i++) {
		int j = 1;
		for (int k = 0; k <= 9; k++) check[k] = 0;
		how_check = 0;
		fscanf(infile, "%d", &N);
		real_N = N;

		if (N == 0) {
			fprintf(outfile, "Case #%d: INSOMNIA\n", i);
		}
		else {
			while (1) {
				N = real_N*j;
				while (N > 0) {
					if (check[N % 10] == 0) {
						check[N % 10] = 1;
						how_check += 1;
					}
					N = N / 10;
				}

				if (how_check == 10) {
					fprintf(outfile, "Case #%d: %d\n", i, real_N*j);
					break;
				}
				j++;
			}
		}
	}
	fclose(infile);
	fclose(outfile);
	return 0;
}

