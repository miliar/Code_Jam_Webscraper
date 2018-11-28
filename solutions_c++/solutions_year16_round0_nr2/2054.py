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
	fin = fopen("B-large.in", "r");
	fout = fopen("B-large.out", "w");
	int n;
	fscanf(fin, "%d", &n);
	for (int t = 1; t <= n; ++t) {
		fscanf(fin, "%s", &s);
		char last = '+';
		int cnt = 0;
		for (int i = strlen(s) - 1; i >= 0; --i) {
			if (s[i] != last) {
				++cnt;
				last = s[i];
			}
		}

		fprintf(fout, "Case #%d: %d\n", t, cnt);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}