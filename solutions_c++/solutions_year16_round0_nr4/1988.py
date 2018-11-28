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


int main()
{
	FILE *fin, *fout;
	fin = fopen("D-large.in", "r");
	fout = fopen("D-large.out", "w");
	int t;
	fscanf(fin, "%d", &t);
	for (int r = 1; r <= t; ++r) {
		int k, c, s;
		fscanf(fin, "%d%d%d", &k, &c, &s);
		if (s * c < k) {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", r);
			continue;
		}
		fprintf(fout, "Case #%d:", r);
		int i, j;
		for (i = 0; i < k - c; i += c) {
			long long num = 0;
			for (j = i; j < i + c; ++j) {
				num = num * k + j;
			}
			fprintf(fout, " %lld", num + 1);
		}
		long long num = 0;
		for (j = i ; j < k; ++j) {
			num = num * k + j;
		}
		fprintf(fout, " %lld\n", num + 1);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}