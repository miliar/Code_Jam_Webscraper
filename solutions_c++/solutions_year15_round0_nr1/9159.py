#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T, smax, sum = 0, res = 0, res1;
	FILE* f = fopen("A-large.in", "r");
	FILE* ff = fopen("A-large.out", "w");
	fscanf(f, "%d", &T);
	char ch;
	for (int ti = 0; ti < T; ti++)
	{
		sum = 0;
		res = 0;
		res1 = 0;
		fscanf(f, "%d", &smax);
		fscanf(f, "%c", &ch);
		for (int si = 0; si <= smax; si++)
		{
			fscanf(f, "%c", &ch);
			res1 = res;
			if (si > sum) res += si - sum;
			
			sum += res - res1 + ch - '0';
		}
		fprintf(ff, "Case #%d: %d\n", ti + 1, res);
	}
	return 0;
}
