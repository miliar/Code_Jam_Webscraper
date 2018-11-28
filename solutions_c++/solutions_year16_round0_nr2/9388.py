#define _CRT_SECURE_NO_WARNINGS


#include <cstdio>
#include <vector>

using namespace std;


void do_work(int c, vector<int> l)
{
	printf("Case #%d: ", c+1);
	int bad = 0;

	int flips = 0;
	vector<int>::reverse_iterator i;
	for (i = l.rbegin(); i != l.rend(); ++i)
	{
		if (*i == bad)
		{
			bad = !bad;
			flips++;
		}
	}
	printf("%d\n", flips);
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

	int nr_cases = 0;
	int cur_n;
	fscanf(f, "%d\n", &nr_cases);
	vector<vector<int> > cases;
	char buf[1024];
	for (int i = 0; i < nr_cases; ++i)
	{
		fgets(buf, sizeof(buf), f);
		vector<int> tmp;
		for (int j = 0; j < strlen(buf); ++j)
			if (buf[j] == '+')
				tmp.push_back(1);
			else
				if(buf[j] != '\n') // lags sometimes
					tmp.push_back(0);
		cases.push_back(tmp);
	}
	fclose(f);

	for (int i = 0; i < nr_cases; ++i)
	{
		do_work(i, cases[i]);
	}
	scanf("");
	return 0;
}