#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a < b ? b : a)

set<string> was;

bool print_binary(int n, int len, char *s) {
	while (len) {
		if (n & 1)
			s[len - 1] = '1';
		else
			s[len - 1] = '0';
		len--;
		n >>= 1;
	}
	return n == 0;
}

void execute_next(int test, FILE *f, FILE *g) {
	int n, J;
	fscanf(f, "%d %d\n", &n, &J);
	fprintf(g, "Case #%d:\n", test + 1);

	char block[70];
	char var[40];
	for (int len = 2; len <= n / 2; len++) {
		if (len > 10)
			break;
		block[0] = '1';
		block[len - 1] = '1';
		block[len] = 0;
		int cnt = (n - len * 2) / len;
		if (cnt > 32)
			continue;
		int remain = n - (cnt + 2) * len;

		for (int i = 0; print_binary(i, len - 2, block + 1); i++) {
			int divisor[11];
			for (int b = 2; b <= 10; b++) {
				divisor[b] = 0;
				int base = 1;
				for (int k = 0; k < len; k++) {
					bool one = block[len - k - 1] == '1';
					divisor[b] += base * one;
					base *= b;
				}
			}
			
			for (int j = 0; print_binary(j, cnt, var); j++) {
				string s = "";
				s.append(block);
				for (int k = 0; k < cnt; k++) {
					if (var[k] == '1')
						s.append(block);
					else {
						for (int l = 0; l < len; l++)
							s.append("0");
					}
				}
				for (int l = 0; l < remain; l++)
					s.append("0");
				s.append(block);
				if (was.count(s) > 0)
					continue;
				was.insert(s);
				fprintf(g, "%s ", s.c_str());
				for (int b = 2; b <= 10; b++)
					fprintf(g, "%d ", divisor[b]);
				fprintf(g, "\n");
				J--;
				if (J <= 0)
					break;
			}
			if (J <= 0)
				break;
		}
		if (J <= 0)
			break;
	}

	if (J > 0) {
		printf("Attention!\n");
	}
	printf("%d remain = %d\n", test + 1, J);
}

int main(int argc, char* argv[])
{
	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;
	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		execute_next(test, f, g);
	}
	fclose(f);
	fclose(g);
	return 0;
}

