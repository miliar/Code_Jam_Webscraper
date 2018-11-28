#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>

const int N_MAX = 1020;

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
int N;
std::vector<double> girl;
std::vector<double> boy;
int result1 = 0, result2 = 0;

int main()
{
	fscanf(f, "%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		fscanf(f, "%d", &N);

		girl.clear();
		boy.clear();
		for (int i = 0; i < N; ++i)
		{
			double x;
			fscanf(f, "%lf", &x);
			girl.push_back(x);
		}
		for (int i = 0; i < N; ++i)
		{
			double x;
			fscanf(f, "%lf", &x);
			boy.push_back(x);
		}

		sort(girl.begin(), girl.end());
		sort(boy.begin(), boy.end());

		result1 = 0;
		result2 = 0;

		int j = N - 1;
		for (int i = N - 1; i >= 0; --i)
		{
			if (girl[i] > boy[j])
			{
				result2++;
			}
			else
			{
				j--;
			}
		}

		j = 0;
		for (int i = 0; i < N; ++i)
		{
			if (girl[i] > boy[j])
			{
				result1++;
				j++;
			}
		}

		fprintf(g, "Case #%d: %d %d\n", t, result1, result2);
	}

	fclose(f);
	fclose(g);
}