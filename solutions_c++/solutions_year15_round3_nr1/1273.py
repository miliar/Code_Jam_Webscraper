#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("A-large.out", "w");

	int t;
	fscanf(in, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int r, c, w;
		fscanf(in, "%d %d %d", &r, &c, &w);

		int ans = r*(c / w);
		
		if (c%w == 0)
		{
			ans += w - 1;
		}
		else
		{
			ans += w;
		}
		
		fprintf(out, "Case #%d: %d\n", i, ans);
	}

	return 0;
}