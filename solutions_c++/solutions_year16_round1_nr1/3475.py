#ifdef WIN32
#pragma warning(disable:4996)
#endif

#include <stdio.h>
#include <string.h>

void shift_right(char *s)
{
	int i = strlen(s);
	
	s[i + 1] = '\0';
	while (i > 0)
	{
		s[i] = s[i - 1];
		i--;
	}
}

int main(int argc, char *argv[])
{
	FILE *fp;
	int t = 0;

#ifdef TESTING
	fp = fopen(argv[1], "r");
#else
	fp = stdin;
#endif

	fscanf(fp, "%d", &t);

	char s[1001];
	char output[1001];

	for (int ti = 0; ti < t; ti++)
	{
		fprintf(stdout, "Case #%d: ", ti + 1);
		fscanf(fp, "%s", s);

		output[0] = '\0';

		int i = 0;
		while (s[i] != '\0')
		{
			if (s[i] >= output[0])
			{
				shift_right(output);
				output[0] = s[i];
			}
			else
			{
				output[i] = s[i];
				output[i + 1] = '\0';
			}
			i++;
		}

		output[i] = '\0';

		fprintf(stdout, "%s\n", output);
	}

#ifdef TESTING
	fclose(fp);
#endif
}
