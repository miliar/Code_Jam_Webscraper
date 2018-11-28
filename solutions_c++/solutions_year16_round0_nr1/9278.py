#define _CRT_SECURE_NO_WARNINGS


#include <cstdio>
#include <vector>

using namespace std;


void do_work(int c, long N)
{
	long cur = N;
	int digits[10] = { 0,0,0,0,0,0,0,0,0,0 };
	int found = 0;
	printf("Case #%d: ", c+1);
	if (N == 0)
	{
		printf("INSOMNIA\n");
		return;
	}
	while (found < 10)
	{
		long work = cur;
		while (work > 0)
		{
			int digit = work % 10;
			if (digits[digit] == 0)
			{
				digits[digit] = 1;
				found++;
			}
			if (found >= 10)
			{
				printf("%d\n", cur);
				return;
			}
			work = work / 10;
		}
		cur += N;
	}
}

int main()
{
	FILE *f;
	f = fopen("input.in", "r");
	if (!f)
	{
		fprintf(stderr, "Cannot read from input\n");
		return 1;
	}

	int nr_cases=0;
	long cur_n;
	fscanf(f, "%d\n", &nr_cases);
	vector<long> cases;
	for (int i = 0; i < nr_cases; ++i)
	{
		fscanf(f, "%ld\n", &cur_n);
		cases.push_back(cur_n);
	}
	fclose(f);

	for (int i = 0; i < nr_cases; ++i)
	{
		do_work(i, cases[i]);
	}
	scanf("");
	return 0;
}