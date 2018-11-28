#include <stdio.h>
#include <memory.h>
#include <string>

int n;
int result;

bool visit[10];

using namespace std;

FILE* fin = fopen("A-large.in", "r");
FILE* fout = fopen("A-large.out", "w");

void initialize()
{
	result = 0;
	memset(visit, 0, sizeof(visit));
}

void input()
{
	fscanf(fin, "%d", &n);
}

int process()
{
	for (int i = 1 ; i < 1000 ; i ++)
	{
		string a = to_string(n * i);

		for (int j = 0; j < a.size(); j++)
		{
			visit[a.at(j) - '0'] = true;
		}

		bool fetched = false;
		for (int j = 0; j < 10; j++)
		{
			if (visit[j] == false)
			{
				fetched = true;
			}
		}

		if (!fetched)
		{
			result = n * i;
			return result;
		}
	}

	return 0;
}

void output(int i)
{
	fprintf(fout, "Case #%d: %d\n", i + 1, result);
}

int main(void)
{
	int t;
	fscanf(fin, "%d", &t);

	for (int i = 0; i < t; i++)
	{
		initialize();
		input();
		if (process() > 0)
		{
			output(i);
		}
		else
		{
			fprintf(fout, "Case #%d: INSOMNIA\n",i+1);
		}
	}
	return 0;
}