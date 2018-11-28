#include <stdio.h>
#include <string.h>

int n;
int result;
char map[105];

FILE* fin = fopen("B-large.in", "r");
FILE* fout = fopen("B-large.out", "w");

void initialize()
{
	result = 0;
	memset(map, 0, sizeof(map));
}

void input()
{
	fscanf(fin, "%s", &map);
}

void process()
{
	result = 1;
	char current = map[0];
	for (int i = 1; i < strlen(map); i++)
	{
		if (current != map[i])
		{
			result++;
			current = map[i];
		}
	}
	
	if (map[strlen(map) - 1] == '+')
		result--;
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
		process();
		output(i);
	}
	return 0;
}