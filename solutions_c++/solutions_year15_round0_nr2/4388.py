#include <cstdio>
#include <memory>
#include <set>
#include <algorithm>

int p[1005], num[1005], dp[1005][1005];
FILE *fin, *fout;
std::set<int> dataset;
int d, t, tmp, min, max, start;

int main()
{
	fin = fopen("a.in", "r");
	fout = fopen("a.out", "w");

	fscanf(fin, "%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		fscanf(fin, "%d", &d);
		memset(dp, -1, sizeof(dp));
		memset(num, 0, sizeof(num));
		dataset.clear();
		max = 0;

		for (int i = 0; i < d; i++)
		{
			fscanf(fin, "%d", &p[i]);
			num[p[i]] ++;
			dataset.insert(p[i]);
		}



		auto &iter = dataset.begin();
		for (int j = 0; j < *iter; j++)
		{
			if (*iter % (j + 1) == 0)
				tmp = *iter / (j + 1);
			else
				tmp = *iter / (j + 1) + 1;
			dp[0][j * num[*iter]] = tmp;
		}

		start = 0;
		iter++;
		for (int i = 1; iter != dataset.end(); iter++, i++)
		{
			for (int j = 0; j <= 54; j++)
			{
				min = 0xffffff;
				for (int k = 0; k < *iter; k++)
				{
					if (j - k * num[*iter] < 0)
						break;
					if (i < 1 || dp[i - 1][j - k * num[*iter]] == -1)
						continue;
					if (*iter % (k + 1) == 0)
						tmp = *iter / (k + 1);
					else
						tmp = *iter / (k + 1) + 1;

					min = std::min(min, std::max(dp[i - 1][j - k * num[*iter]], tmp));
				}
				dp[i][j] = min;
			}
		}

		min = 0xffffff;
		for (int j = 0; j <= 54; j++)
			if (dp[dataset.size() - 1][j] != -1)
			min = std::min(dp[dataset.size() - 1][j] + j, min);

		fprintf(fout, "Case #%d: %d\n", tt + 1, min);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}