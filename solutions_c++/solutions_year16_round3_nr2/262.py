#include <cstdio>
#include <memory.h>

using namespace std;

int main()
{
	FILE *in = fopen("input.txt", "rt");
	FILE *out = fopen("output.txt", "wt");

	int T, B;
	long long M, temp;
	int d[50][50];
	int bit[100];

	fscanf(in, "%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		fscanf(in, "%d %lld", &B, &M);
		
		memset(d, 0, sizeof(d));
		for (int i = 1; i < B; ++i)
			for (int j = i+1; j < B; ++j)
				d[i][j] = 1;

		memset(bit, 0, sizeof(bit));

		temp = 1;
		for (int i = 1; i < B - 1; ++i)
			temp *= 2ll;

		if (temp < M)
		{
			fprintf(out, "Case #%d: IMPOSSIBLE\n", t);
			continue;
		}

		if (temp == M)
		{
			fprintf(out, "Case #%d: POSSIBLE\n", t);
			for (int j = 1; j < B; ++j)
				d[0][j] = 1;
			for (int i = 0; i < B; ++i)
			{	
				for (int j = 0; j < B; ++j)
				{
					fprintf(out, "%d", d[i][j]);
				}
				fprintf(out, "\n");
			}
			continue;
		}

		int k = B - 1;
		while (0 < M)
		{
			d[0][k - 1] = (M & 1);
			M >>= 1;
			k--;
		}

		fprintf(out, "Case #%d: POSSIBLE\n", t);
		for (int i = 0; i < B; ++i)
		{
			for (int j = 0; j < B; ++j)
				fprintf(out, "%d", d[i][j]);
			fprintf(out, "\n");
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}