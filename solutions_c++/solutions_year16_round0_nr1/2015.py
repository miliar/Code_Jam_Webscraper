#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
using namespace std;

char s[102];

int main()
{
	FILE *fin, *fout;
	fin = fopen("A-large.in", "r");
	fout = fopen("A-large.out", "w");
	int t;
	fscanf(fin, "%d", &t);
	for (int r = 1; r <= t; ++r) {
		int flag = 1023;
		int n;
		fscanf(fin, "%d", &n);
		if (n == 0) {
			fprintf(fout, "Case #%d: INSOMNIA\n", r);
			continue;
		}
		for (int i = 1; ; ++i) {
			int num = n * i;
			while (num) {
				int dig = num % 10;
				flag &= ~(1 << dig);
				num /= 10;
			}
			if (!flag) {
				fprintf(fout, "Case #%d: %d\n", r, n * i);
				break;
			}
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}