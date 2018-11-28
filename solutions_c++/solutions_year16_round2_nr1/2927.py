#ifdef WIN32
#pragma warning(disable:4996)
#endif

#include <stdio.h>
#include <string.h>


void count_alphabets(char *s, int *count)
{
	for (int i = 0; s[i] != '\0'; i++)
	{
		count[s[i] - 'A']++;
	}
}

int main(int argc, char *argv[])
{
	FILE *fp;
	int t = 0;
	char s[2001];
	int count[26];
	int count_nums[10];

#ifdef TESTING
	fp = fopen(argv[1], "r");
#else
	fp = stdin;
#endif

	fscanf(fp, "%d", &t);

	for (int ti = 0; ti < t; ti++)
	{
		fprintf(stdout, "Case #%d: ", ti + 1);

		memset(s, 0, sizeof(s));
		memset(count, 0, sizeof(count));
		memset(count_nums, 0, sizeof(count_nums));

		fscanf(fp, "%s", s);
		count_alphabets(s, count);

		//0
		count_nums[0] = count['Z' - 'A'];
		count['E' - 'A'] -= count_nums[0];
		count['R' - 'A'] -= count_nums[0];
		count['O' - 'A'] -= count_nums[0];

		//2
		count_nums[2] = count['W' - 'A'];
		count['T' - 'A'] -= count_nums[2];
		count['O' - 'A'] -= count_nums[2];

		//4
		count_nums[4] = count['U' - 'A'];
		count['F' - 'A'] -= count_nums[4];
		count['O' - 'A'] -= count_nums[4];
		count['R' - 'A'] -= count_nums[4];

		//6
		count_nums[6] = count['X' - 'A'];
		count['S' - 'A'] -= count_nums[6];
		count['I' - 'A'] -= count_nums[6];

		//8
		count_nums[8] = count['G' - 'A'];
		count['E' - 'A'] -= count_nums[8];
		count['I' - 'A'] -= count_nums[8];
		count['H' - 'A'] -= count_nums[8];
		count['T' - 'A'] -= count_nums[8];

		//1
		count_nums[1] = count['O' - 'A'];
		count['N' - 'A'] -= count_nums[1];
		count['E' - 'A'] -= count_nums[1];

		//3
		count_nums[3] = count['H' - 'A'];
		count['T' - 'A'] -= count_nums[3];
		count['R' - 'A'] -= count_nums[3];
		count['E' - 'A'] -= 2 * count_nums[3];

		//5
		count_nums[5] = count['F' - 'A'];
		count['I' - 'A'] -= count_nums[5];
		count['V' - 'A'] -= count_nums[5];
		count['E' - 'A'] -= count_nums[5];

		//7
		count_nums[7] = count['V' - 'A'];
		count['S' - 'A'] -= count_nums[7];
		count['E' - 'A'] -= 2 * count_nums[7];
		count['N' - 'A'] -= count_nums[7];

		//9
		count_nums[9] = count['I' - 'A'];

		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < count_nums[i]; j++)
			{
				fprintf(stdout, "%c", '0' + i);
			}
		}

		fprintf(stdout, "\n");
	}

#ifdef TESTING
	fclose(fp);
#endif
}
